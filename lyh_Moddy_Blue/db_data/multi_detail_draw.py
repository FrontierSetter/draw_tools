import sys
import plotly
import plotly_express as px
from plotly.subplots import make_subplots
import time
import os
import functools
import argparse


def stampToTime(ts):
    timeArray = time.localtime(ts)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime


# https://plotly.com/python-api-reference/generated/plotly.figure_factory.create_gantt.html
# https://plotly.com/python-api-reference/generated/plotly.express.timeline.html#plotly.express.timeline

hySizeSuffix = "_total_hy_size"
hyCntSuffix = "_total_hy_cnt"
accessSizeSuffix = "_total_access_size"
accessCntSuffix = "_total_access_cnt"
suffixArr = [hySizeSuffix, hyCntSuffix, accessSizeSuffix, accessCntSuffix]

hyRatioArr = []
iopsArr = []
bandwidthArr = []

# 主逻辑
parser = argparse.ArgumentParser(description='画性能图')
parser.add_argument('-f','--file', help='输入的log文件')

args = parser.parse_args()
print(args)

inHySizeFile = open(args.file+hySizeSuffix+".csv", 'r', encoding='utf-8')
inHyCntFile = open(args.file+hyCntSuffix+".csv", 'r', encoding='utf-8')
inAccessSizeFile = open(args.file+accessSizeSuffix+".csv", 'r', encoding='utf-8')
inAccessCntFile = open(args.file+accessCntSuffix+".csv", 'r', encoding='utf-8')

lineNameArr = inHySizeFile.readline().strip('\n').split(',')
inHyCntFile.readline()
inAccessSizeFile.readline()
inAccessCntFile.readline()

preArrHySize = [float(x) for x in inHySizeFile.readline().strip('\n').split(',')]
preArrHyCnt = [float(x) for x in inHyCntFile.readline().strip('\n').split(',')]
preArrAccessSize = [float(x) for x in inAccessSizeFile.readline().strip('\n').split(',')]
preArrAccessCnt = [float(x) for x in inAccessCntFile.readline().strip('\n').split(',')]

while True:
    curLineHySize = inHySizeFile.readline()
    curLineHyCnt = inHyCntFile.readline()
    curLineAccessSize = inAccessSizeFile.readline()
    curLineAccessCnt = inAccessCntFile.readline()
    if curLineHySize == '':
        break
    
    curArrHySize = [float(x) for x in curLineHySize.strip('\n').split(',') if x != '']
    curArrHyCnt = [float(x) for x in curLineHyCnt.strip('\n').split(',') if x != '']
    curArrAccessSize = [float(x) for x in curLineAccessSize.strip('\n').split(',') if x != '']
    curArrAccessCnt = [float(x) for x in curLineAccessCnt.strip('\n').split(',') if x != '']

    if len(curArrHySize) != len(lineNameArr) or len(curArrHyCnt) != len(lineNameArr) or len(curArrAccessSize) != len(lineNameArr) or len(curArrAccessCnt) != len(lineNameArr):
        break

    # 统计回源率
    curHyRatioDict = {}
    for i in range(1, len(lineNameArr)):
        curHyRatioDict[lineNameArr[i]] = (curArrHySize[i]-preArrHySize[i])/(curArrAccessSize[i]-preArrAccessSize[i])*100

    curHyRatioDict[lineNameArr[0]] = stampToTime(int(curArrHySize[0]))
    hyRatioArr.append(curHyRatioDict)

    # 统计IO次数
    curIopsDict = {}
    for i in range(1, len(lineNameArr)):
        curIopsDict[lineNameArr[i]+"_R"] = (curArrAccessCnt[i]-preArrAccessCnt[i])/60
        curIopsDict[lineNameArr[i]+"_W"] = (curArrHyCnt[i]-preArrHyCnt[i])/60

    curIopsDict[lineNameArr[0]] = stampToTime(int(curArrHySize[0]))
    iopsArr.append(curIopsDict)

    # 统计IO带宽
    curBandwidthDict = {}
    for i in range(1, len(lineNameArr)):
        curBandwidthDict[lineNameArr[i]+"_R"] = (curArrAccessSize[i]-preArrAccessSize[i])/60/1024/1024
        curBandwidthDict[lineNameArr[i]+"_W"] = (curArrHySize[i]-preArrHySize[i])/60/1024/1024

    curBandwidthDict[lineNameArr[0]] = stampToTime(int(curArrHySize[0]))
    bandwidthArr.append(curBandwidthDict)

    preArrHySize = curArrHySize
    preArrHyCnt = curArrHyCnt
    preArrAccessSize = curArrAccessSize
    preArrAccessCnt = curArrAccessCnt
    
# 构造图例
xItem = lineNameArr[0]
lineItemArrNormal = lineNameArr[1:]
lineItemArrIO = []
for i in range(1, len(lineNameArr)):
    lineItemArrIO.append(lineNameArr[i]+"_R")
    lineItemArrIO.append(lineNameArr[i]+"_W")

hyRatioPlot = px.line(hyRatioArr, x = xItem, y = lineItemArrNormal, labels = {xItem: 'time', 'value': 'hy_ratio (%)'}) 
iopsPlot = px.line(iopsArr, x = xItem, y = lineItemArrIO, labels = {xItem: 'time', 'value': 'IOPS (#/s)'}) 
bandwidthPlot = px.line(bandwidthArr, x = xItem, y = lineItemArrIO, labels = {xItem: 'time', 'value': 'IO bandwidth (GB/s)'}) 


# fig = make_subplots(rows=3, cols=1,subplot_titles=("HY Ration", "IO cnt", "IO bandwidth"), shared_xaxes=True)

# for trace in range(len(hyRatioPlot["data"])):
#     fig.append_trace(hyRatioPlot["data"][trace], row=1, col=1)

# for trace in range(len(iopsPlot["data"])):
#     fig.append_trace(iopsPlot["data"][trace], row=2, col=1)

# for trace in range(len(bandwidthPlot["data"])):
#     fig.append_trace(bandwidthPlot["data"][trace], row=3, col=1)

plotly.offline.plot(hyRatioPlot, filename='%s_hy_ratio.html' % (args.file), auto_open=False)
plotly.offline.plot(iopsPlot, filename='%s_iops.html' % (args.file), auto_open=False)
plotly.offline.plot(bandwidthPlot, filename='%s_ioband.html' % (args.file), auto_open=False)

fichier_html_graphs=open("%s_all.html" % (args.file),'w')
fichier_html_graphs.write("<html><head></head><body>"+"\n")
fichier_html_graphs.write("  <object data=\""+'%s_hy_ratio.html' % (args.file)+"\" width=\"100%\" height=\"33%\"></object>"+"\n")
fichier_html_graphs.write("  <object data=\""+'%s_iops.html' % (args.file)+"\" width=\"100%\" height=\"33%\"></object>"+"\n")
fichier_html_graphs.write("  <object data=\""+'%s_ioband.html' % (args.file)+"\" width=\"100%\" height=\"33%\"></object>"+"\n")
fichier_html_graphs.write("</body></html>")
fichier_html_graphs.close()
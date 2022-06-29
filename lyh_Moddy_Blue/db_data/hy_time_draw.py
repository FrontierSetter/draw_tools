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

dataArr = []

# 主逻辑
parser = argparse.ArgumentParser(description='画性能图')
parser.add_argument('-f','--file', help='输入的log文件')

args = parser.parse_args()
print(args)

inHyFile = open(args.file+"_hy.csv", 'r', encoding='utf-8')
inAccessFile = open(args.file+"_access.csv", 'r', encoding='utf-8')

lineNameArr = inHyFile.readline().strip('\n').split(',')
inAccessFile.readline()

preArrHy = [float(x) for x in inHyFile.readline().strip('\n').split(',')]
preArrAccess = [float(x) for x in inAccessFile.readline().strip('\n').split(',')]

while True:
    curLineHy = inHyFile.readline()
    curLineAccess = inAccessFile.readline()
    if curLineHy == '':
        break
    
    curArrHy = [float(x) for x in curLineHy.strip('\n').split(',') if x != '']
    curArrAccess = [float(x) for x in curLineAccess.strip('\n').split(',') if x != '']

    if len(curArrHy) != len(lineNameArr) or len(curArrAccess) != len(lineNameArr):
        break

    curDict = {}
    # print(lineNameArr)
    # print(curArrHy)
    # print(curArrAccess)
    for i in range(1, len(lineNameArr)):
        curDict[lineNameArr[i]] = (curArrHy[i]-preArrHy[i])/(curArrAccess[i]-preArrAccess[i])*100

    curDict[lineNameArr[0]] = stampToTime(int(curArrHy[0]))
    dataArr.append(curDict)

    preArrHy = curArrHy
    preArrAccess = curArrAccess
    
    
linePlot = px.line(dataArr, x = lineNameArr[0], y = lineNameArr[1:]) 

plotly.offline.plot(linePlot, filename='hy_rate_%s.html' % (args.file))

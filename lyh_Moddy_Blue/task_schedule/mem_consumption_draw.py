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
"""
df = [dict(Task="Job A", Start='2009-01-01',
           Finish='2009-02-30', Resource='Apple'),
      dict(Task="Job B", Start='2009-03-05',
           Finish='2009-04-15', Resource='Grape'),
      dict(Task="Job C", Start='2009-02-20',
           Finish='2009-05-30', Resource='Banana')]
"""
gantDataArr = []
cacheNameArr = []
stateNameArr = ['Load', 'Consume', 'Save']

memDataDict = []

# 主逻辑
parser = argparse.ArgumentParser(description='画性能图')
parser.add_argument('-f','--file', help='输入的log文件')

args = parser.parse_args()
print(args)

targetFile = args.file
inFile = open(targetFile, mode='r', encoding='UTF-8')
(filepath, tempfilename) = os.path.split(targetFile)
(filename, extension) = os.path.splitext(tempfilename)


while True:
    curLine = inFile.readline()
    if curLine == '':
        break
    
    curTime = stampToTime(int(curLine.strip('\n')))
    curLine = inFile.readline()
    # 处理dram
    curLine = inFile.readline()
    curArr = [x for x in curLine.strip('\n').split(' ') if x != '']
    curRam = float(curArr[2])/1024/1024/1024
    curCache = float(curArr[5])/1024/1024/1024
    # 处理swap
    curLine = inFile.readline()
    curArr = [x for x in curLine.strip('\n').split(' ') if x != '']
    curSwap = float(curArr[2])/1024/1024/1024

    memDataDict.append({
        'time': curTime,
        'anon': curRam,
        'cache': curCache,
        'swap': curSwap,
        'dram': curRam+curCache,
        'total': curRam+curCache+curSwap
    })


linePlot = px.line(memDataDict, x = 'time', y = ['anon', 'cache', 'swap', 'dram', 'total']) 

plotly.offline.plot(linePlot, filename='mem_%s.html' % (filename))

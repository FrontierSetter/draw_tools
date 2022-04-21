import sys
import plotly
import plotly_express as px
from plotly.subplots import make_subplots
import time
import os
import functools


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
targetFile = sys.argv[1]
inFile = open(targetFile, mode='r', encoding='UTF-8')
(filepath, tempfilename) = os.path.split(targetFile)
(filename, extension) = os.path.splitext(tempfilename)


while True:
    curLine = inFile.readline()
    if curLine == '':
        break

    if 'consume_end' in curLine:
        curArr = curLine.strip('\n').split(' ')

        curCache = curArr[1]
        if curCache not in cacheNameArr:
            cacheNameArr.append(curCache)
        curTarget = curArr[3]

        curTimeArr = curArr[8].split(',')

        gantDataArr.append({
            'Task': curCache,
            'Start': stampToTime(int(curTimeArr[0])),
            'Finish': stampToTime(int(curTimeArr[1])),
            'Resource': 'Load',
            'Time': int(curTimeArr[1])-int(curTimeArr[0]),
            'Target': curTarget,
        })
        gantDataArr.append({
            'Task': curCache,
            'Start': stampToTime(int(curTimeArr[2])),
            'Finish': stampToTime(int(curTimeArr[3])),
            'Resource': 'Consume',
            'Time': int(curTimeArr[3])-int(curTimeArr[2]),
            'Target': curTarget,
        })
        gantDataArr.append({
            'Task': curCache,
            'Start': stampToTime(int(curTimeArr[4])),
            'Finish': stampToTime(int(curTimeArr[5])),
            'Resource': 'Save',
            'Time': int(curTimeArr[5])-int(curTimeArr[4]),
            'Target': curTarget,
        })
    elif 'memory_consumption' in curLine:
        curArr = curLine.strip('\n').split(' ')
        # print(curArr)

        curTime = stampToTime(int(curArr[2]))
        curRam = float(curArr[3].split(',')[0])/1024/1024/1024
        curCache = float(curArr[4].split(',')[0])/1024/1024/1024
        curSwap = float(curArr[5].split(',')[0])/1024/1024/1024

        memDataDict.append({
            'time': curTime,
            'anon': curRam,
            'cache': curCache,
            'swap': curSwap,
            'dram': curRam+curCache,
            'total': curRam+curCache+curSwap
        })

        # memDataDict.append({
        #     'time': None,
        #     'anon': None,
        #     'cache': None,
        #     'swap': None,
        #     'dram': None,
        #     'total': curRam+curCache+curSwap
        # })


def sortCache(c1, c2):
    n1 = c1.split('_')[0]
    n2 = c2.split('_')[0]

    if n1 == n2:
        capatity1 = int(c1.split('_')[1][:-1])
        capatity2 = int(c2.split('_')[1][:-1])
        if capatity1 > capatity2:
            return 1
        else:
            return -1        
    else:
        if n1 > n2:
            return 1
        else:
            return -1

cacheNameArr.sort(key=functools.cmp_to_key(sortCache))
print(cacheNameArr)

colors = {
    'Load': '#5470C6',
    'Consume': '#91CC75',
    'Save': '#FAC858',
}

ordersDic = {
    'Task': cacheNameArr,
    'Resource': stateNameArr,
}

hoverData = ['Task', 'Start', 'Finish', 'Resource', 'Time', 'Target']

# fig = make_subplots(rows=2, cols=1,subplot_titles=("Gantt", "Mem"), shared_xaxes=True)

gantPlot = px.timeline(gantDataArr, x_start='Start', x_end='Finish', y='Task',
                  color_discrete_map=colors, color='Resource', category_orders=ordersDic,
                  hover_data=hoverData)

linePlot = px.line(memDataDict, x = 'time', y = ['anon', 'cache', 'swap', 'dram', 'total']) 

# for trace in range(len(gantPlot["data"])):
#     fig.append_trace(gantPlot["data"][trace], row=1, col=1)

# for trace in range(len(linePlot["data"])):
#     fig.append_trace(linePlot["data"][trace], row=2, col=1)

plotly.offline.plot(gantPlot, filename='gantt_%s.html' % (filename))
plotly.offline.plot(linePlot, filename='mem_%s.html' % (filename))
# gantPlot.show()
# linePlot.show()

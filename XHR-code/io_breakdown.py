import xlrd
import matplotlib.pyplot as plt
import numpy as np
from textwrap import fill

from xlrd import sheet

stageNameArr = ['I/O Time', 'Transmission Time', 'Computation Time']

colorDict = {
    'I/O Time': '#00B050', 
    'Transmission Time': '#C00000', 
    'Computation Time': '#F79646'
}

# colorDict = {
#     'I/O Time': 'tab:blue', 
#     'Transmission Time': 'tab:orange', 
#     'Computation Time': 'tab:green'
# }

hatchDict = {
    'I/O Time': '\\\\\\\\', 
    'Transmission Time': '////', 
    'Computation Time': 'xxxx'
}

readbook = xlrd.open_workbook('number of IOs.xlsx')

# 子表编号
sheetIdx = 0

sheets = readbook.sheets()
sheetNames = readbook.sheet_names()
curSheet = sheets[sheetIdx]

print('now draw %s' % (sheetNames[sheetIdx]))

dataArr = []

for curGroup in range(0, 4):
    curStartLine = curGroup*12+6
    
    dataArr.append({})
    for curLine in range(curStartLine, curStartLine+3):
        curArr = curSheet.row_values(curLine)

        curMethod = curArr[0]

        dataArr[-1][curMethod] = {
            'I/O Time':[],
            'Transmission Time':[],
            'Computation Time':[],
        }

        for curStage in range(3):
            for curSize in range(3):
                curCol = 2+curStage+4*curSize
                dataArr[-1][curMethod][stageNameArr[curStage]].append(curArr[curCol])

# print(dataArr)

width = 0.24
gap = 0.1*width

for figNum in range(len(dataArr)):
    fig = plt.figure(figsize=(9,6))

    legendArrBar = []
    legendEntryArrBar = []

    yMax = 0

    # 画第一方法
    baseArr = [0]*len(dataArr[figNum]['XHR']['I/O Time'])
    x=np.arange(len(baseArr))

    for curStageIdx in range(len(stageNameArr)):
        curEntry = stageNameArr[curStageIdx]
        curStageArr = dataArr[figNum]['XHR'][curEntry]
        curP = plt.bar(x-width-gap*1.5, curStageArr, width, bottom=baseArr, edgecolor=colorDict[curEntry], hatch=hatchDict[curEntry], color='white', linewidth=2)

        legendArrBar.insert(0,curP)
        legendEntryArrBar.insert(0,curEntry)

        for i in range(len(curStageArr)):
            baseArr[i] += curStageArr[i]
    for x_, y in zip(x, baseArr) :
        plt.text(x_-width-gap*1.5, y+0.1, "XHR", fontsize=26, ha = 'center',va = 'bottom', rotation=90)
    yMax = max(yMax, max(baseArr))

    # 画第二方法
    baseArr = [0]*len(dataArr[figNum]['ECWide']['I/O Time'])
    x=np.arange(len(baseArr))

    for curStageIdx in range(len(stageNameArr)):
        curEntry = stageNameArr[curStageIdx]
        curStageArr = dataArr[figNum]['ECWide'][curEntry]
        curP = plt.bar(x, curStageArr, width, bottom=baseArr, edgecolor=colorDict[curEntry], hatch=hatchDict[curEntry], color='white', linewidth=2)

        for i in range(len(curStageArr)):
            baseArr[i] += curStageArr[i]
    for x_, y in zip(x, baseArr) :
        plt.text(x_, y+0.1, "ECWide", fontsize=26, ha = 'center',va = 'bottom', rotation=90)
    yMax = max(yMax, max(baseArr))


    # 画第三方法
    baseArr = [0]*len(dataArr[figNum]['LRC']['I/O Time'])
    x=np.arange(len(baseArr))

    for curStageIdx in range(len(stageNameArr)):
        curEntry = stageNameArr[curStageIdx]
        curStageArr = dataArr[figNum]['LRC'][curEntry]
        curP = plt.bar(x+width+gap*1.5, curStageArr, width, bottom=baseArr, edgecolor=colorDict[curEntry], hatch=hatchDict[curEntry], color='white', linewidth=2)

        for i in range(len(curStageArr)):
            baseArr[i] += curStageArr[i]
    for x_, y in zip(x, baseArr) :
        plt.text(x_+width+gap*1.5, y+0.1, "LRC", fontsize=26, ha = 'center',va = 'bottom', rotation=90)
    yMax = max(yMax, max(baseArr))


    plt.ylabel('Total Repair Time', fontsize=28)
    plt.xticks(x, ['16M', '32M', '64M'], fontsize=26)
    plt.xlabel('Block Size', fontsize=28)
    plt.legend(legendArrBar, legendEntryArrBar, columnspacing=0.7, ncol=1, fontsize=22,loc='upper left')

    plt.subplots_adjust(left=0.1, right=0.99, top=0.99, bottom=0.135)
    # plt.subplots_adjust(left=0.13, right=0.99, top=0.99, bottom=0.135)
    plt.ylim(0, yMax*1.26)
    plt.yticks(fontsize=20)

    plt.savefig('%s_%d_3.pdf' % (sheetNames[sheetIdx], figNum))
    # plt.show()




import xlrd
import matplotlib.pyplot as plt
import numpy as np
from textwrap import fill

from xlrd import sheet

stageNameArr = ['Cross-rack Time', 'Intra-rack Time']

colorDict = {
    'Cross-rack Time': '#00B050', 
    'Intra-rack Time': '#C00000'
}

hatchDict = {
    'Cross-rack Time': '\\\\\\\\', 
    'Intra-rack Time': '////'
}

readbook = xlrd.open_workbook('number of IOs_new.xlsx')

# readbook = xlrd.open_workbook('10.9.xlsx')

# 子表编号
sheetIdx = 4

sheets = readbook.sheets()
sheetNames = readbook.sheet_names()
curSheet = sheets[sheetIdx]

print('now draw %s' % (sheetNames[sheetIdx]))

dataArr = []

for curGroup in range(0, 4):
    curStartLine = curGroup*5+2
    
    dataArr.append({})
    for curLine in range(curStartLine, curStartLine+2):
        curArr = curSheet.row_values(curLine)

        curMethod = curArr[0]

        dataArr[-1][curMethod] = {
            'Cross-rack Time':[],
            'Intra-rack Time':[]
        }

        for curStage in range(2):
            for curSize in range(3):
                curCol = 1+curStage+4*curSize
                dataArr[-1][curMethod][stageNameArr[curStage]].append(curArr[curCol])


width = 0.24
gap = 0.1*width
print(len(dataArr))
for figNum in range(len(dataArr)):
    fig = plt.figure(figsize=(9,6))

    legendArrBar = []
    legendEntryArrBar = []

    yMax = 0

    # 画第一方法
    baseArr = [0]*len(dataArr[figNum]['XHR']['Cross-rack Time'])
    x=np.arange(len(baseArr))
    for curStageIdx in range(len(stageNameArr)):
        curEntry = stageNameArr[curStageIdx]
        curStageArr = dataArr[figNum]['XHR'][curEntry]
        curP = plt.bar(x-0.5*width-0.5*gap, curStageArr, width, bottom=baseArr, edgecolor=colorDict[curEntry], hatch=hatchDict[curEntry], color='white', linewidth=2)

        legendArrBar.insert(0,curP)
        legendEntryArrBar.insert(0,curEntry)

        for i in range(len(curStageArr)):
            baseArr[i] += curStageArr[i]
    for x_, y in zip(x, baseArr) :
        plt.text(x_-0.5*width-0.5*gap, y+0.05, "XHR", fontsize=14, ha = 'center',va = 'bottom', rotation=90)
    yMax = max(yMax, max(baseArr))

    # 画第二方法
    baseArr = [0]*len(dataArr[figNum]['ECWide']['Cross-rack Time'])
    x=np.arange(len(baseArr))

    for curStageIdx in range(len(stageNameArr)):
        curEntry = stageNameArr[curStageIdx]
        curStageArr = dataArr[figNum]['ECWide'][curEntry]
        curP = plt.bar(x+0.5*width+0.5*gap, curStageArr, width, bottom=baseArr, edgecolor=colorDict[curEntry], hatch=hatchDict[curEntry], color='white', linewidth=2)

        for i in range(len(curStageArr)):
            baseArr[i] += curStageArr[i]
    for x_, y in zip(x, baseArr) :
        plt.text(x_+0.5*width+0.5*gap, y+0.05, "ECWide", fontsize=14, ha = 'center',va = 'bottom', rotation=90)
    yMax = max(yMax, max(baseArr))


    # # 画第三方法
    # baseArr = [0]*len(dataArr[figNum]['LRC']['I/O Time'])
    # x=np.arange(len(baseArr))

    # for curStageIdx in range(len(stageNameArr)):
    #     curEntry = stageNameArr[curStageIdx]
    #     curStageArr = dataArr[figNum]['LRC'][curEntry]
    #     curP = plt.bar(x+width+gap*1.5, curStageArr, width, bottom=baseArr, edgecolor=colorDict[curEntry], hatch=hatchDict[curEntry], color='white', linewidth=2)

    #     for i in range(len(curStageArr)):
    #         baseArr[i] += curStageArr[i]
    # for x_, y in zip(x, baseArr) :
    #     plt.text(x_+width+gap*1.5, y+0.1, "LRC", fontsize=16, ha = 'center',va = 'bottom', rotation=90)
    # yMax = max(yMax, max(baseArr))


    plt.ylabel('Total Transmission Time', fontsize=26)
    plt.xticks(x, ['16M', '32M', '64M'], fontsize=20)
    plt.xlabel('Block Size', fontsize=26)
    plt.legend(legendArrBar, legendEntryArrBar, columnspacing=0.7, ncol=1, fontsize=22,loc='upper left')

    plt.subplots_adjust(left=0.12, right=0.99, top=0.99, bottom=0.13)
    plt.ylim(0, yMax*1.25)
    plt.yticks(fontsize=20)

    plt.savefig('%s_%d.pdf' % (sheetNames[sheetIdx], figNum))
    # plt.show()




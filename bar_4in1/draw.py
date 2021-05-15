# 说明：
# 2021年5月13日 加入每个图的X/Y轴文字功能；加入1.5倍y坐标缩放防止legend重叠

import xlrd
import matplotlib.pyplot as plt
import numpy as np

# {
#     'RR-swans-RAID-0': '#1f497d', 
#     'FS-Lazwl': '#8064A2'
# }
colorDict = {}
hatchDict = {}
markerDict = {}

# {
#     'Average response time':{
#         'Write-30/RAID-0':{
#             'x-value':[...],
#             'RR-swans-RAID-0':[...],
#             ...
#         },
#         ...
#     }
# }
dataDict = {}

subfigTitle = ['Write-30/RAID-0', 'Write-30/RAID-5', 'Write-70/RAID-0', 'Write-70/RAID-5']
figYLabel = {} # Y轴说明
figXLabel = {} # X轴说明
plotType = {} # 画图类型

readbook = xlrd.open_workbook('2.xlsx')

# 读取config簿
configSheet = readbook.sheet_by_index(2)

nrows = configSheet.nrows

for i in range(1, nrows):
    # print(configSheet.row_values(i))
    curRow = configSheet.row_values(i)
    colorDict[curRow[0]] = curRow[1]
    hatchDict[curRow[0]] = curRow[2]
    markerDict[curRow[0]] = curRow[3]

# print(colorDict)

# 读取30的数据
dataSheet_1 = readbook.sheet_by_index(0)

nrows = dataSheet_1.nrows

i = 0
while i < nrows:
    curRow = dataSheet_1.row_values(i)
    # print(curRow)
    curTypeName = curRow[0]
    curYName = curRow[1]
    curXName = curRow[2]
    curPlotType = curRow[3]
    figYLabel[curTypeName] = curYName
    figXLabel[curTypeName] = curXName
    plotType[curTypeName] = curPlotType
    # print(i)
    # print(curTypeName)

    dataDict[curTypeName] = {
        subfigTitle[0]:{},
        subfigTitle[1]:{},
        subfigTitle[2]:{},
        subfigTitle[3]:{},
    }

    temRow = dataSheet_1.row_values(i+1)[1:]
    curX = [x for x in temRow if x != '']

    dataDict[curTypeName][subfigTitle[0]]['x-value'] = curX
    for j in range(6):
        temRow = dataSheet_1.row_values(i+2+j)
        curRow = [x for x in temRow if x != '']
        # print(i+2+j)
        # print(curRow)
        curType = curRow[0]
        curData = curRow[1:]
        dataDict[curTypeName][subfigTitle[0]][curType] = curData

    dataDict[curTypeName][subfigTitle[1]]['x-value'] = curX
    for j in range(6):
        temRow = dataSheet_1.row_values(i+8+j)
        curRow = [x for x in temRow if x != '']
        # print(i+8+j)
        # print(curRow)
        curType = curRow[0]
        curData = curRow[1:]
        dataDict[curTypeName][subfigTitle[1]][curType] = curData
    
    i += 15

# print(dataDict)


# 读取80的数据
dataSheet_2 = readbook.sheet_by_index(1)

nrows = dataSheet_2.nrows

i = 0
while i < nrows:
    curRow = dataSheet_2.row_values(i)
    curTypeName = curRow[0]

    # 名字这部分在30的部分就已经读过了，这里再弄反而混乱且没必要
    # if len(curRow) > 1 and curRow[1] != '':
    #     curYName = curRow[1]
    #     figYLabel[curTypeName] = curMatrix

    # print(i)
    # print(curTypeName)

    # dataDict[curTypeName] = {
    #     subfigTitle[0]:{},
    #     subfigTitle[1]:{},
    #     subfigTitle[2]:{},
    #     subfigTitle[3]:{},
    # }

    temRow = dataSheet_2.row_values(i+1)[1:]
    curX = [x for x in temRow if x != '']

    dataDict[curTypeName][subfigTitle[2]]['x-value'] = curX
    for j in range(6):
        temRow = dataSheet_2.row_values(i+2+j)
        curRow = [x for x in temRow if x != '']
        # print(i+2+j)
        # print(curRow)
        curType = curRow[0]
        curData = curRow[1:]
        dataDict[curTypeName][subfigTitle[2]][curType] = curData

    dataDict[curTypeName][subfigTitle[3]]['x-value'] = curX
    for j in range(6):
        temRow = dataSheet_2.row_values(i+8+j)
        curRow = [x for x in temRow if x != '']
        # print(i+8+j)
        # print(curRow)
        curType = curRow[0]
        curData = curRow[1:]
        dataDict[curTypeName][subfigTitle[3]][curType] = curData
    
    i += 15

# print(dataDict)
# print(figYLabel)
# print(figXLabel)

width = 0.12
gap = 0.1*width
bar_lw = 1
line_lw = 2

# print()

for figType in dataDict.keys():
    subFigK = list(dataDict[figType].keys())
    plt.figure(figsize=(36,6))
    for subFigIdx in range(len(subFigK)):
        plt.subplot(1, len(subFigK), subFigIdx+1)
        curSubFigK = subFigK[subFigIdx]

        ind = np.arange(len(dataDict[figType][curSubFigK]['x-value']))

        legendNameArr = list(dataDict[figType][curSubFigK].keys())

        barCnt = 0
        subFigMaxValue = 0

        for legendNameIdx in range(len(legendNameArr)):
            legendName = legendNameArr[legendNameIdx]
            if legendName == 'x-value':
                continue
            
            offset = 0.0-width*3.0-gap*2.5+(barCnt+0.5)*width+barCnt*gap
            # print(offset)
            if plotType[figType] == 'bar':
                curP = plt.bar(ind+offset, dataDict[figType][curSubFigK][legendName], width, edgecolor=colorDict[legendName], hatch=hatchDict[legendName], color='white', linewidth=bar_lw, label=legendName)
                barCnt += 1
            elif plotType[figType] == 'line':
                plt.plot(ind, dataDict[figType][curSubFigK][legendName], label=legendName, linewidth=line_lw, marker=markerDict[legendName], color=colorDict[legendName], markevery=int(1), markersize=12)

            # 求这幅图里的所有数据的最大值，用于控制y轴的缩放给legend留空间
            curMaxValue = max(dataDict[figType][curSubFigK][legendName])
            if curMaxValue > subFigMaxValue:
                subFigMaxValue = curMaxValue

        plt.xticks(ind, dataDict[figType][curSubFigK]['x-value'], fontsize=20)
        plt.xlabel(figXLabel[figType], fontsize=26) # x轴文字

        plt.ylabel(figYLabel[figType], fontsize=26) # y轴文字
        plt.yticks(fontsize=20) # y轴标签字体
        plt.ylim(0, subFigMaxValue*1.5) # y轴上下界

        plt.subplots_adjust(left=0.105, right=0.99, top=0.95, bottom=0.13) # 图的上下左右边界
        plt.legend(fontsize=22, loc='upper left', ncol=2, columnspacing=1)   # 图例

        plt.title(curSubFigK, fontsize=16)  # 图标题

    fileName = '_'.join('_'.join(figType.split(' ')).split('/'))
    print(fileName)
    plt.savefig("%s.pdf" % (fileName))
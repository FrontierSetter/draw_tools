# 说明：
# 2021年5月13日 加入每个图的X/Y轴文字功能；加入1.5倍y坐标缩放防止legend重叠
# 2021年5月15日 加入折线图、科学计数法功能；4合1共用同一个图例
# 2021年5月22日 柱状图offset按照柱子数量自适应；按照sheet名称索引

import xlrd
import matplotlib.pyplot as plt
import numpy as np
import copy

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
cntType = {} # 科学计数法 or 常规记法

readbook = xlrd.open_workbook('5.xlsx')

# 读取config簿
configSheet = readbook.sheet_by_name('draw_config')

nrows = configSheet.nrows

for i in range(1, nrows):
    # print(configSheet.row_values(i))
    curRow = configSheet.row_values(i)
    colorDict[curRow[0]] = curRow[1]
    hatchDict[curRow[0]] = curRow[2]
    markerDict[curRow[0]] = curRow[3]
    

# print(colorDict)

# 读取30的数据
dataSheet_1 = readbook.sheet_by_name('totalios-30')

nrows = dataSheet_1.nrows

i = 0
while i < nrows:
    curRow = dataSheet_1.row_values(i)
    # print(curRow)
    curTypeName = curRow[0]
    curYName = curRow[1]
    curXName = curRow[2]
    curPlotType = curRow[3]
    curCntType = curRow[4]
    figYLabel[curTypeName] = curYName
    figXLabel[curTypeName] = curXName
    plotType[curTypeName] = curPlotType
    cntType[curTypeName] = curCntType
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
dataSheet_2 = readbook.sheet_by_name('totalios-70')

nrows = dataSheet_2.nrows

i = 0
while i < nrows:
    curRow = dataSheet_2.row_values(i)
    curTypeName = curRow[0]

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

oriDataDict = copy.deepcopy(dataDict)
dataDict = {}

for curFigType in subfigTitle:
    dataDict[curFigType] = {}
    for curStage in oriDataDict.keys():
        dataDict[curFigType][curStage] = oriDataDict[curStage][curFigType]

width = 0.12
gap = 0.1*width
bar_lw = 1
line_lw = 2

# print()
drawCnt = 1
plt.figure(figsize=(36,18))
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.4)

for curFigType in subfigTitle:
    stageName = list(dataDict[curFigType].keys())
    methodName = list(dataDict[curFigType][stageName[0]].keys())
    for curGroup in range(3):
        plt.subplot(3, 4, drawCnt)

        barCnt = 0
        ind = np.arange(len(dataDict[curFigType][stageName[0]]['x-value']))
        
        scalFactor = 1.0

        for curMethod in range(2):
            totalBarNum = 2
            offset = 0.0-width*(totalBarNum/2.0)-gap*((totalBarNum-1.0)/2)+(barCnt+0.5)*width+barCnt*gap

            tmpMethodName = methodName[1+curGroup+curMethod*3]
            tmpData = dataDict[curFigType][curStage][tmpMethodName]
            curBase = [0]*len(tmpData)

            for curStage in stageName:
                curMethodName = methodName[1+curGroup+curMethod*3]
                curP = plt.bar(ind+offset, dataDict[curFigType][curStage][curMethodName], width, edgecolor=colorDict[curStage], hatch=hatchDict[curMethodName], color='white', linewidth=bar_lw, label=curMethodName+curStage, bottom=curBase)

                for i in range(len(dataDict[curFigType][curStage][curMethodName])):
                    curBase[i] += dataDict[curFigType][curStage][curMethodName][i]
            
            barCnt += 1

        plt.xticks(ind, dataDict[curFigType][stageName[0]]['x-value'], fontsize=20)
        plt.xlabel('x', fontsize=26) # x轴文字

        plt.ylabel('y', fontsize=26) # y轴文字
        plt.yticks(fontsize=20) # y轴标签字体

        plt.subplots_adjust(left=0.03, right=0.99, top=0.85, bottom=0.15) # 图的上下左右边界

        plt.legend()

        # 用统一的图例了，所以不单画
        # plt.legend(fontsize=22, loc='upper left', ncol=2, columnspacing=1)   # 图例

        plt.title(curFigType, fontsize=16)  # 图标题

        drawCnt += 1

plt.savefig("%s.pdf" % ('all_stage'))



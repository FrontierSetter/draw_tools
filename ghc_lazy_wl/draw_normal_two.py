# 说明：
# 2021年5月13日 加入每个图的X/Y轴文字功能；加入1.5倍y坐标缩放防止legend重叠
# 2021年5月15日 加入折线图、科学计数法功能；4合1共用同一个图例
# 2021年5月22日 柱状图offset按照柱子数量自适应；按照sheet名称索引

import xlrd
import matplotlib.pyplot as plt
import numpy as np
from textwrap import fill

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

subTitleDict = {}

subfigTitle = ['Write-30/RAID-0', 'Write-30/RAID-5', 'Write-70/RAID-0', 'Write-70/RAID-5']
figYLabel = {} # Y轴说明
figXLabel = {} # X轴说明
plotType = {} # 画图类型
cntType = {} # 科学计数法 or 常规记法

letterArr = [chr(x) for x in range(97, 123)]

readbook = xlrd.open_workbook('5.xlsx')

# 读取config簿
configSheet = readbook.sheet_by_name('draw_config')

nrows = configSheet.nrows

for i in range(1, nrows):
    curRow = configSheet.row_values(i)
    colorDict[curRow[0]] = curRow[1]
    hatchDict[curRow[0]] = curRow[2]
    markerDict[curRow[0]] = curRow[3]

# 读取subfig_title簿
subtitleSheet = readbook.sheet_by_name('subfig_title')

nrows = subtitleSheet.nrows

for i in range(1, nrows):
    curRow = subtitleSheet.row_values(i)
    curFigType = curRow[0]
    curSubFig = curRow[1]
    curTitle = curRow[2]

    if curFigType not in subTitleDict:
        subTitleDict[curFigType] = {}
    subTitleDict[curFigType][curSubFig] = curTitle

    
# print(subTitleDict)

# 读取30的数据
dataSheet_1 = readbook.sheet_by_name('Write-30')

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
dataSheet_2 = readbook.sheet_by_name('Write-70')

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

for baseFigType in dataDict.keys():

    if baseFigType[-1] == '2':
        continue

    plt.figure(figsize=(36,15))

    legendArr = []
    legendEntryArr = []
    subFigCnt = 0

    for figType in dataDict.keys():
        if baseFigType not in figType:
            continue

        # print("%s, %s" % (baseFigType, figType))

        subFigK = list(dataDict[figType].keys())


        for subFigIdx in range(len(subFigK)):
            subFigCnt += 1
            plt.subplot(2, len(subFigK), subFigCnt)
            curSubFigK = subFigK[subFigIdx]

            ind = np.arange(len(dataDict[figType][curSubFigK]['x-value']))

            legendNameArr = list(dataDict[figType][curSubFigK].keys())

            barCnt = 0
            subFigMaxValue = 0

            for legendNameIdx in range(len(legendNameArr)):
                legendName = legendNameArr[legendNameIdx]
                if legendName == 'x-value':
                    continue

                # 求这幅图里的所有数据的最大值，用于控制y轴的缩放给legend留空间
                # print(figType, curSubFigK, legendName)
                # print(figType)
                curMaxValue = max(dataDict[figType][curSubFigK][legendName])
                if curMaxValue > subFigMaxValue:
                    subFigMaxValue = curMaxValue
            
            # print(subFigMaxValue)

            for legendNameIdx in range(len(legendNameArr)):
                legendName = legendNameArr[legendNameIdx]
                if legendName == 'x-value':
                    continue

                scalFactor = 1.0
                scalNum = 0
                if cntType[figType] == 'scientific':
                    tmpMax = subFigMaxValue
                    while tmpMax >= 10:
                        scalFactor *= 10
                        scalNum += 1
                        tmpMax = int(tmpMax / 10)
                        # print(tmpMax)
                

                totalBarNum = len(legendNameArr)-1
                offset = 0.0-width*(totalBarNum/2.0)-gap*((totalBarNum-1.0)/2)+(barCnt+0.5)*width+barCnt*gap
                # print(offset)
                if plotType[figType] == 'bar':
                    curP = plt.bar(ind+offset, [float(i)/scalFactor for i in dataDict[figType][curSubFigK][legendName]], width, edgecolor=colorDict[legendName], hatch=hatchDict[legendName], color='white', linewidth=bar_lw, label=legendName)
                    barCnt += 1
                elif plotType[figType] == 'line':
                    # line的返回值比较特殊，是一个数组，见：https://matplotlib.org/2.0.2/users/legend_guide.html
                    curP, = plt.plot(ind, [float(i)/scalFactor for i in dataDict[figType][curSubFigK][legendName]], label=legendName, linewidth=line_lw, marker=markerDict[legendName], color=colorDict[legendName], markevery=int(1), markersize=12)

                if legendName not in legendEntryArr:
                    legendArr.append(curP)
                    legendEntryArr.append(legendName)          

            plt.xticks(ind, dataDict[figType][curSubFigK]['x-value'], fontsize=20)
            plt.xlabel(figXLabel[figType], fontsize=26) # x轴文字

            plt.ylabel(figYLabel[figType], fontsize=26) # y轴文字
            plt.yticks(fontsize=20) # y轴标签字体

            # 用统一的图例，所以上面不用留空了
            # plt.ylim(0, subFigMaxValue*1.5/scalFactor) # y轴上下界

            xmin, xmax, ymin, ymax = plt.axis()

            if cntType[figType] == 'scientific':
                # 因为柱状图和折线图y轴的x坐标不同，需要分别调整
                if plotType[figType] == 'line':
                    # 用统一的图例，所以上面不用留空了
                    # plt.text(-0.2, subFigMaxValue*1.5/scalFactor*1.005, r'$\times10^{%d}$'%(scalNum),fontsize=22,ha='left')             
                    plt.text(xmin, ymax*1.005, r'$\times10^{%d}$'%(scalNum),fontsize=20,ha='left')             
                elif plotType[figType] == 'bar':
                    # 用统一的图例，所以上面不用留空了
                    # plt.text(-0.63, subFigMaxValue*1.5/scalFactor*1.005, r'$\times10^{%d}$'%(scalNum),fontsize=22,ha='left')             
                    plt.text(xmin, ymax*1.005, r'$\times10^{%d}$'%(scalNum),fontsize=20,ha='left')    

            # 用来设置纵坐标自动放缩，这里用不到
            # plt.autoscale(enable=True, axis='y', tight=False)   


            # 用统一的图例了，所以不单画
            # plt.legend(fontsize=22, loc='upper left', ncol=2, columnspacing=1)   # 图例

            plt.title(fill(('(%s) %s' % (letterArr[subFigCnt-1], subTitleDict[figType][curSubFigK])), 60), fontsize=16, y=-0.25)  # 图标题

    # 统一的图例，参数见：https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.figlegend.html#matplotlib.pyplot.figlegend
    plt.figlegend(legendArr, legendEntryArr, ncol=len(legendEntryArr), loc="upper center", fontsize=22, columnspacing=1, handletextpad=0.3, bbox_to_anchor=(0.5, 1.01))
    plt.subplots_adjust(left=0.03, right=0.99, top=0.93, bottom=0.11, hspace=0.3) # 图的上下左右边界

    fileName = '_'.join('_'.join(baseFigType.split(' ')).split('/'))
    # plt.show()
    print(fileName)
    plt.savefig("2_4_%s.pdf" % (fileName))
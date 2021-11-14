# 说明：
# 2021年5月13日 加入每个图的X/Y轴文字功能；加入1.5倍y坐标缩放防止legend重叠
# 2021年5月15日 加入折线图、科学计数法功能；4合1共用同一个图例
# 2021年5月22日 柱状图offset按照柱子数量自适应；按照sheet名称索引


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

subfigTitle = ['place_holder']
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
dataSheet_1 = readbook.sheet_by_name('algorithmic-space-overhead')

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
    }

    temRow = dataSheet_1.row_values(i+3)[1:]
    curX = [x for x in temRow if x != '']

    validLen = len(curX)

    dataDict[curTypeName][subfigTitle[0]]['x-value'] = curX
    for j in range(3):
        temRow = dataSheet_1.row_values(i+4+j)
        curRow = [x for x in temRow if x != '']
        # print(i+2+j)
        # print(curRow)
        curType = curRow[0]
        curData = curRow[1:1+validLen]
        dataDict[curTypeName][subfigTitle[0]][curType] = curData

    i += 8


width = 0.12
gap = 0.1*width
bar_lw = 1
line_lw = 2

# print()

for figType in dataDict.keys():
    subFigK = list(dataDict[figType].keys())
    plt.figure(figsize=(9*len(subFigK),6))

    legendArr = []
    legendEntryArr = []
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

            # 求这幅图里的所有数据的最大值，用于控制y轴的缩放给legend留空间
            # print(figType, curSubFigK, legendName)
            # print(figType)
            # print(dataDict[figType][curSubFigK][legendName])
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

        plt.subplots_adjust(left=0.15, right=0.99, top=0.85, bottom=0.13) # 图的上下左右边界

        # 用统一的图例了，所以不单画
        # plt.legend(fontsize=22, loc='upper left', ncol=2, columnspacing=1)   # 图例

        # plt.title(curSubFigK, fontsize=16)  # 图标题

    # 统一的图例，参数见：https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.figlegend.html#matplotlib.pyplot.figlegend
    plt.figlegend(legendArr, legendEntryArr,ncol=len(legendEntryArr), loc="upper center", fontsize=22, columnspacing=1, handletextpad=0.3)

    fileName = '_'.join('_'.join(figType.split(' ')).split('/'))
    # plt.show()
    print(fileName)
    # plt.show()
    plt.savefig("space_%s.pdf" % (fileName))
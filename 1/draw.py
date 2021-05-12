import xlrd
import matplotlib.pyplot as plt
import numpy as np

# {
#     'RR-swans-RAID-0': '#1f497d', 
#     'FS-Lazwl': '#8064A2'
# }
colorDict = {}
hatchDict = {}

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

readbook = xlrd.open_workbook('1.xlsx')

# 读取config簿
configSheet = readbook.sheet_by_index(2)

nrows = configSheet.nrows

for i in range(1, nrows):
    # print(configSheet.row_values(i))
    curRow = configSheet.row_values(i)
    colorDict[curRow[0]] = curRow[1]
    hatchDict[curRow[0]] = curRow[2]

# print(colorDict)

# 读取30的数据
dataSheet_1 = readbook.sheet_by_index(0)

nrows = dataSheet_1.nrows

i = 0
while i < nrows:
    curRow = dataSheet_1.row_values(i)
    curTypeName = curRow[0]
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

width = 0.12
gap = 0.1*width
lw = 1

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
        for legendNameIdx in range(len(legendNameArr)):
            legendName = legendNameArr[legendNameIdx]
            if legendName == 'x-value':
                continue
            
            offset = 0.0-width*3.0-gap*2.5+(barCnt+0.5)*width+barCnt*gap
            # print(offset)
            curP = plt.bar(ind+offset, dataDict[figType][curSubFigK][legendName], width, edgecolor=colorDict[legendName], hatch=hatchDict[legendName], color='white', linewidth=lw, label=legendName)
            barCnt += 1

        plt.xticks(ind, dataDict[figType][curSubFigK]['x-value'], fontsize=20)

        plt.ylabel('Y_label', fontsize=26) # y轴文字
        plt.yticks(fontsize=20) # y轴标签字体
        # plt.ylim(0, 1.25) # y轴上下界

        plt.subplots_adjust(left=0.105, right=0.99, top=0.95, bottom=0.13) # 图的上下左右边界
        plt.legend(fontsize=22, loc='upper left', ncol=2, columnspacing=1)   # 图例

        plt.title(curSubFigK, fontsize=16)  # 图标题

    fileName = '_'.join('_'.join(figType.split(' ')).split('/'))
    print(fileName)
    plt.savefig("%s.pdf" % (fileName))
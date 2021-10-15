import xlrd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator

# colorDict = {'Full Recovery-PPR': 'darkviolet', 'Full Recovery-RP': 'dodgerblue', 'PRM': 'gold',
#              'Baseline': 'skyblue','GAN': '#fa8080'}  # 设置配色 2021-09-21

# colorDict = {'PRM-Typical': '#80499C', 'PRM-PPR': '#87CFEC', 'PRM-RP': '#3CB474', 'GAN': '#F26750'}  # 设置配色 2021-09-21
# hatchDict = {'PRM-Typical': '////', 'PRM-PPR': '\\\\\\\\', 'PRM-RP': 'xxxx', 'GAN': '----'}

# colorDict = {'PRM-Typical': '#80499C', 'Typical': '#5088C7', 'PRM-RP': '#87CFEC', 'RP': '#FCD718', 'PRM-PPR': '#3CB474', 'PPR': '#F26750', 'GAN': '#C00000'}  # 设置配色 2021-09-21
colorDict = {'PRM-Typical': '#80499C', 'Typical': '#5088C7', 'PRM-RP': '#219ebc', 'RP': '#B8860B', 'PRM-PPR': '#3CB474', 'PPR': '#F26750', 'GAN': '#C00000'}  # 设置配色 2021-09-21
# colorDict = {'PRM-Typical': '#80499C', 'Typical': '#3478BF', 'PRM-RP': '#219ebc', 'RP': '#B8860B', 'PRM-PPR': '#0a9396', 'PPR': '#F26750', 'GAN': '#C00000'}  # 设置配色 2021-09-21
markerDict = {'PRM-Typical': '^', 'Typical': 'o', 'PRM-RP': 'v', 'RP': 'D', 'PRM-PPR': '>', 'PPR': 's', 'GAN': 'x'}  # 设置配色 2021-09-21


dataDict = {}
paraDict = {}

readbook = xlrd.open_workbook('RS(6,3)数据-PRM-GAN_all.xlsx')

sheets = readbook.sheets()
sheetNames = readbook.sheet_names()

for i in range(2, len(sheets)):
    
    curSheet = sheets[i]

    curModelName = curSheet.row_values(1)[0]

    print(curModelName)

    dataDict[curModelName] = {'x-arr': [str(int(x)) for x in curSheet.row_values(0)[2:] if len(str(x)) > 1]}
    paraDict[curModelName] = {
        'yMin': curSheet.row_values(2)[0],
        'yMax': curSheet.row_values(3)[0],
    }

    curMin = 100

    for curLineNum in range(1, curSheet.nrows):
        curRow = curSheet.row_values(curLineNum)
        # if "Full Recovery" in curRow[1] or 'Baseline' in curRow[1]:
        #     continue
        if len(curRow[1]) == 0:
            continue

        dataDict[curModelName][curRow[1]] = [x for x in curRow[2:] if type(x) != type('')]

        curMin = min([curMin, min(dataDict[curModelName][curRow[1]])])
    
    # paraDict[curModelName]['full_line'] = (sum(dataDict[curModelName]['Full Recovery-PPR'])+sum(dataDict[curModelName]['Full Recovery-RP'])) / (len(dataDict[curModelName]['Full Recovery-PPR'])+len(dataDict[curModelName]['Full Recovery-RP']))
    paraDict[curModelName]['full_line'] = max([max(dataDict[curModelName]['Full Recovery-PPR']),max(dataDict[curModelName]['Full Recovery-RP'])])
    paraDict[curModelName]['base_line'] = sum(dataDict[curModelName]['Baseline']) / len(dataDict[curModelName]['Baseline'])
    
    if curModelName == 'resnet18':
        paraDict[curModelName]['base_line'] = min(dataDict[curModelName]['Baseline'])
        paraDict[curModelName]['full_line'] = max(dataDict[curModelName]['PRM-RP'])+0.2
    elif curModelName == 'resnet34':
        paraDict[curModelName]['full_line'] = max(dataDict[curModelName]['PRM-PPR'])+0.2

    del(dataDict[curModelName]['Full Recovery-PPR'])
    del(dataDict[curModelName]['Full Recovery-RP'])
    del(dataDict[curModelName]['Baseline'])

print(dataDict)
print(len(dataDict))

# plt.figure(figsize=(36, 6))
# plt.figure(figsize=(38, 8))

# bar_width = 0.18  # 设置柱状图的宽度
bar_width = 0.18  # 设置柱状图的宽度
# gap_width = 0.02
gap_width = 0.03


for subFigId in range(len(dataDict)):
    plt.figure(figsize=(9, 6))
    # plt.subplot(1, len(dataDict), subFigId + 1)
    curModelName = list(dataDict.keys())[subFigId]

    ind = np.arange(len(dataDict[curModelName]['x-arr']))
    totalBarNum = len(dataDict[curModelName].keys()) - 1

    legendArr = []
    legendEntryArr = []

    barCnt = 0
    for barId in dataDict[curModelName].keys():
        if barId == 'x-arr':
            continue

        # print(barId, curModelName)
        # print(dataDict[curModelName]['x-arr'])
        # print(dataDict[curModelName][barId])

        offset = 0.0 - bar_width * (totalBarNum / 2.0) - gap_width * ((totalBarNum - 1.0) / 2) + (
                    barCnt+0.5) * bar_width + barCnt * gap_width
        # curP = plt.bar(ind + offset, dataDict[curModelName][barId], bar_width, label=barId, color='white', edgecolor=colorDict[barId], hatch=hatchDict[barId], linewidth=3)
        curP = plt.plot(ind, dataDict[curModelName][barId], label=barId, linewidth=4, color=colorDict[barId], marker=markerDict[barId], markersize=12)
        barCnt += 1

        if barId not in legendEntryArr:
            legendArr.append(curP)
            legendEntryArr.append(barId)

    plt.axhline(y=paraDict[curModelName]['full_line'],ls=":",c="black",linewidth=4)#添加水平直线
    curP = plt.plot([],[],ls=":",c="black",linewidth=4, label='Supremum')
    legendArr.append(curP)
    legendEntryArr.append('Supremum')
    plt.axhline(y=paraDict[curModelName]['base_line'],ls="--",c="black",linewidth=4)#添加水平直线
    curP = plt.plot([],[],ls="--",color="black",linewidth=4, label='Infimum')
    legendArr.append(curP)
    legendEntryArr.append('Infimum')

    print("%f, %f" % (paraDict[curModelName]['full_line'], paraDict[curModelName]['base_line']))

    # plt.xticks(ind, dataArr[subfigId]['x-arr'], fontsize=20)
    plt.xticks(ind, dataDict[curModelName]['x-arr'], fontsize=24)
    plt.xlabel('Recovery Ratio(%)', fontsize=28)  # x轴文字

    # plt.gca().yaxis.set_major_locator(MultipleLocator(5))

    plt.yticks(fontsize=24)  # y轴标签字体
    plt.ylabel('acc(%)', fontsize=28)  # y轴文字

    # plt.legend(fontsize=22, ncol=2, columnspacing=0.8, handletextpad=0.5)  # 显示图例，即label
    plt.legend(fontsize=22, ncol=3, columnspacing=0.6, handletextpad=0.8, handlelength=1.5, mode='expand', loc='upper center')  # 显示图例，即label

    plt.ylim(paraDict[curModelName]['yMin'], paraDict[curModelName]['yMax'])
    # plt.ylim(paraDict[curModelName]['base_line']-1, paraDict[curModelName]['full_line']+10)

    plt.grid(True, linestyle='-.')
    # plt.title(curModelName, fontsize=28)  # 图标题

    # plt.figlegend(legendArr, legendEntryArr, ncol=len(legendEntryArr), loc="upper center", fontsize=22, columnspacing=1, handletextpad=0.3, bbox_to_anchor=(0.5, 1.01))
    plt.subplots_adjust(left=0.145, right=0.99, top=0.97, bottom=0.15)  # 图的上下左右边界

    plt.savefig('RS(6,3)_4_model_GAN_%s_line.pdf' % (curModelName))
    plt.show()
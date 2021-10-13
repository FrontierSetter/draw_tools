import xlrd
import matplotlib.pyplot as plt
import numpy as np
from textwrap import fill

from xlrd import sheet

colorDict = {
    'CIFAR10_PRM VS NOT': 'darkviolet',
    'CIFAR100_PRM VS NOT': 'dodgerblue',
    'MNIST_PRM VS NOT': 'skyblue',
    'ImageNet_PRM VS NOT': 'gold',
    'CIFAR10_PRM VS GAN': 'darkviolet',
    'CIFAR100_PRM VS GAN': 'dodgerblue',
    'MNIST_PRM VS GAN': 'skyblue',
    'ImageNet_PRM VS GAN': 'gold'
}  # 设置配色

markerDict = {
    'CIFAR10_PRM VS NOT': 'o', 
    'CIFAR100_PRM VS NOT': 'd',
    'MNIST_PRM VS NOT': '^', 
    'ImageNet_PRM VS NOT': 'x',
    'CIFAR10_PRM VS GAN': 'o', 
    'CIFAR100_PRM VS GAN': 'd',
    'MNIST_PRM VS GAN': '^', 
    'ImageNet_PRM VS GAN': 'x',
}  # 设置配色

dataArr = []

readbook = xlrd.open_workbook('new_PRM_VS_FULL_AVG_Reduce_ACC_improve _4_dataset.xlsx')

sheets = readbook.sheets()
sheetNames = readbook.sheet_names()

for i in range(0, len(sheets)):

    curSheet = sheets[i]

    nrows = curSheet.nrows
    # 第一行的第一列是空着的
    # metaRow = [i for i in curSheet.row_values(0) if i != '']
    metaRow = curSheet.row_values(0)
    
    dataArr.append({})

    dataArr[-1]['x-arr'] = []
    dataArr[-1][metaRow[1]] = []
    dataArr[-1][metaRow[2]] = []
    dataArr[-1][metaRow[3]] = []
    dataArr[-1][metaRow[4]] = []

    for rowId in range(1, nrows):
        curRow = [i for i in curSheet.row_values(rowId) if i != '']

        if len(curRow) == 0:
            continue

        print(curRow)

        dataArr[-1]['x-arr'].append(int(curRow[0]*100))
        dataArr[-1][metaRow[1]].append(curRow[1]*100)
        dataArr[-1][metaRow[2]].append(curRow[2]*100)
        dataArr[-1][metaRow[3]].append(curRow[3]*100)
        dataArr[-1][metaRow[4]].append(curRow[4]*100)

print(dataArr)

plt.figure(figsize=(18,6.5))
bar_width = 0.25#设置柱状图的宽度
gap_width = 0.02
line_lw = 3

legendArr = []
legendEntryArr = []

for subfigId in range(0, len(dataArr)):
    plt.subplot(1, len(dataArr), subfigId+1)

    ind=np.arange(len(dataArr[subfigId]['x-arr']))
    totalBarNum = len(dataArr[subfigId].keys())-1

    barCnt = 0
    for barId in dataArr[subfigId].keys():
        if barId == 'x-arr':
            continue
        
        offset = 0.0-bar_width*(totalBarNum/2.0)-gap_width*((totalBarNum-1.0)/2)+(barCnt+0.5)*bar_width+barCnt*gap_width
        # curP = plt.bar(ind+offset, dataArr[subfigId][barId], bar_width, label=barId, color=colorDict[barId], hatch=hatchDict[barId])
        curP = plt.plot(dataArr[subfigId]['x-arr'], dataArr[subfigId][barId], linewidth=line_lw, label=barId, color=colorDict[barId], marker=markerDict[barId], markersize=12)
        barCnt += 1
    
        if barId not in legendEntryArr:
            legendArr.append(curP)
            legendEntryArr.append(barId)
    
    # plt.xticks(ind, dataArr[subfigId]['x-arr'], fontsize=20)
    plt.xticks(fontsize=20)
    plt.xlabel('Percentage of Recovery(%)', fontsize=26) # x轴文字

    plt.yticks(fontsize=20) # y轴标签字体
    plt.ylabel('Y label(%)', fontsize=26) # y轴文字

    plt.legend(fontsize=14,ncol=1,columnspacing=0.8,handletextpad=0.5)#显示图例，即label

    plt.ylim(0, 100)
    plt.xlim(0, 75)

    plt.title(sheetNames[subfigId], fontsize=16)  # 图标题

# plt.figlegend(legendArr, legendEntryArr, ncol=len(legendEntryArr), loc="upper center", fontsize=22, columnspacing=1, handletextpad=0.3, bbox_to_anchor=(0.5, 1.01))
plt.subplots_adjust(left=0.07, right=0.99, top=0.90, bottom=0.12) # 图的上下左右边界

plt.savefig('acc_improve.pdf')
# plt.show()

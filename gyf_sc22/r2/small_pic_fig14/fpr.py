import numpy as np
import matplotlib.pyplot as plt
import random
import xlrd
import argparse

parser = argparse.ArgumentParser(description='画性能图')
parser.add_argument('-f','--file')
args = parser.parse_args()

baseRow = 74

# 每个stage对应的颜色和hatch，记得修改
colorDict = {
    'APSNet': '#324665', 
    'APSNet_LL': '#3478BF',
    'APSNet_GG': '#40A776',
    'APSNet_GL': '#F15326',
    'APSNet_NRF': '#F15326',
    # 'KNN': '#3478BF', 
    # 'LR': '#40A776', 
    # 'DT': '#F15326', 
    # 'SVM': '#8064A2', 
    # 'NN': '#C00000', 
    # 'LSTM': '#91CC75', 
}

markerDict = {
    'APSNet': 's', 
    'APSNet_LL': 'd',
    'APSNet_GG': '^',
    'APSNet_NRF': 'v',
    # 'KNN': 'd', 
    # 'LR': '^', 
    # 'DT': 'v', 
    # 'SVM': '<', 
    # 'NN': '>', 
    # 'LSTM': 'X', 
}

newNameDict = {
    'APSNet': 'APSNet',
    'PNET': 'APSNet_NRF',
    # 'DT': 'DT'
}

xTick = []
valueArr = []
lineName = []

# 读取新excel
readbook = xlrd.open_workbook(args.file)
defaultSheet = readbook.sheet_by_name('Sheet1')

lineName = [x for x in defaultSheet.row_values(baseRow) if x != '']
print(lineName)
for i in range(len(lineName)):
    valueArr.append([])

for i in range(8):
    curArr = defaultSheet.row_values(baseRow+1+i)
    print(curArr)

    xTick.append(int(curArr[0]))
    if xTick[-1] == 150:
        xTick[-1] = 120
    for i in range(len(lineName)):
        # print(curArr[i])
        valueArr[i].append(float(curArr[i]))

print(lineName)
print(valueArr)
print(xTick)

# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(9,6))

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='both')

# 各项参数
for item in newNameDict.keys():
    for i in range(len(lineName)):
        if lineName[i] != item:
            continue
        curLineName = newNameDict[lineName[i]]
        curP = plt.plot(xTick, valueArr[i], label=curLineName, \
            color=colorDict[curLineName], lw=4, zorder=5+len(lineName)-i, \
                marker=markerDict[curLineName], markersize=16)
        print(curLineName)
        print(valueArr[i])
        break

    
# 设置坐标轴文字
plt.ylabel('FPR', fontsize=28)
plt.xlabel('Days Lookahead', fontsize=28)

# 设置坐标轴刻度
plt.yticks(fontsize=26)
plt.xticks(fontsize=26)

# 设置图例
plt.legend(fontsize=24, loc='lower center', bbox_to_anchor=(0.5, 0.97),\
    labelspacing=0.1, handletextpad=1, handlelength=2, ncol=2, columnspacing=1.2)

# 设置坐标轴范围
# plt.ylim(0, 108)

# 设置图片边距
plt.subplots_adjust(left=0.15, right=0.99, top=0.825, bottom=0.15)

# 保存图片
plt.savefig('.\\image\\fpr_3.pdf')
# plt.savefig('line.png', dpi=600)

# 显示图片
plt.show()
import xlrd
import argparse
import numpy as np
import matplotlib.pyplot as plt

idCol = 1

colorDict = {
    'APSNet': '#324665', 
    'RF': '#EED777', 
    'KNN': '#3478BF', 
    'LR': '#40A776', 
    'DT': '#F15326', 
    'SVM': '#8064A2', 
    'NN': '#C00000', 
    'LSTM': '#91CC75', 
}

markerDict = {
    'APSNet': 's', 
    'RF': 'o', 
    'KNN': 'd', 
    'LR': '^', 
    'DT': 'v', 
    'SVM': '<', 
    'NN': '>', 
    'LSTM': 'X', 
}

inFile = open('f1_score.csv', 'r')

headLine = inFile.readline()
lineName = [x for x in headLine.strip('\n').split(',')[1:] if x != '']
xTickName = headLine.strip('\n').split(',')[0]

headLine = inFile.readline()
barName = headLine.strip('\n').split(',')[idCol]

xTick = []
valueArr = []
for i in range(len(lineName)):
    valueArr.append([])

while True:
    curLine = inFile.readline()
    if curLine == '':
        break
    curArr = curLine.strip('\n').split(',')

    xTick.append(int(curArr[0]))
    for i in range(len(lineName)):
        valueArr[i].append(float(curArr[3*i+idCol]))

print(lineName)
print(valueArr)
print(xTick)

# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(9,6))

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='both')

# 各项参数
for i in range(len(lineName)):
    curP = plt.plot(xTick, valueArr[i], label=lineName[i], \
        color=colorDict[lineName[i]], lw=4, zorder=5+len(lineName)-i, \
            marker=markerDict[lineName[i]], markersize=16)

# 设置坐标轴文字
plt.ylabel('F1-Score', fontsize=28)
plt.xlabel(xTickName, fontsize=28)

# 设置坐标轴刻度
plt.yticks(fontsize=26)
plt.xticks(fontsize=26)

# 设置图例
plt.legend(fontsize=24, loc='lower left', bbox_to_anchor=(-0.02, 0.98),\
    labelspacing=0.1, handletextpad=0.6, handlelength=1.5, ncol=4, columnspacing=0.8)

# 设置坐标轴范围
# plt.ylim(0, 108)

# 设置图片边距
plt.subplots_adjust(left=0.15, right=0.99, top=0.825, bottom=0.15)

# 保存图片
plt.savefig('f1_score.pdf')

# 显示图片
plt.show()
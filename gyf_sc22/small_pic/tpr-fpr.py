import numpy as np
import matplotlib.pyplot as plt
import random

# 每个stage对应的颜色和hatch，记得修改
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

inFile = open('fpr.csv', 'r')
headLine = inFile.readline()
fprValueArr = []

while True:
    curLine = inFile.readline()
    if curLine == '':
        break
    curArr = curLine.strip('\n').split(',')

    fprValueArr.append(float(curArr[1]))

inFile = open('tpr.csv', 'r')
headLine = inFile.readline()
tprValueArr = []

while True:
    curLine = inFile.readline()
    if curLine == '':
        break
    curArr = curLine.strip('\n').split(',')

    tprValueArr.append(float(curArr[1]))


# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(9,6))

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='both')

# 各项参数
curP = plt.plot(fprValueArr, tprValueArr, label='APSNet', \
    color=colorDict['APSNet'], lw=4, marker=markerDict['APSNet'], markersize=16)
    
# 设置坐标轴文字
plt.ylabel('TPR', fontsize=28)
plt.xlabel('FPR', fontsize=28)

# 设置坐标轴刻度
plt.yticks(fontsize=26)
plt.xticks(fontsize=26)

# 设置图例
plt.legend(fontsize=24, loc='upper right',\
    labelspacing=0.1, handletextpad=0.6, handlelength=1.5, ncol=4, columnspacing=0.8)

# 设置坐标轴范围
plt.xlim(0.086)

# 设置图片边距
plt.subplots_adjust(left=0.18, right=0.99, top=0.970, bottom=0.15)

# 保存图片
plt.savefig('.\\image\\fpr_tpr.pdf')
# plt.savefig('line.png', dpi=600)

# 显示图片
plt.show()
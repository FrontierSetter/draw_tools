import xlrd
import argparse
import numpy as np
import matplotlib.pyplot as plt
import random

parser = argparse.ArgumentParser(description='画性能图')
parser.add_argument('-f','--file')
args = parser.parse_args()

idCol = 1

colorDict = {
    'APSNet': '#324665', 
    'APSNet_LL': '#3478BF',
    'APSNet_GG': '#40A776',
    'APSNet_GL': '#F15326'
    # 'RF': '#EED777', 
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
    'APSNet_GL': 'v'
    # 'RF': 'o', 
    # 'KNN': 'd', 
    # 'LR': '^', 
    # 'DT': 'v', 
    # 'SVM': '<', 
    # 'NN': '>', 
    # 'LSTM': 'X', 
}

newNameDict = {
    'APSNet': 'APSNet',
    '2LSTM': 'APSNet_LL',
    '2GRU': 'APSNet_GG',
    'GRU_LSTM': 'APSNet_GL'
}

# 读取旧csv
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

# 读取新excel
targetKeyWord = ['2GRU','2LSTM','GRU_LSTM']
readbook = xlrd.open_workbook(args.file)
defaultSheet = readbook.sheet_by_name('Sheet1')

newNameArr = defaultSheet.row_values(106)
newValueArr = defaultSheet.row_values(107)
print(newNameArr)
print(newValueArr)
for item in targetKeyWord:
    lineName.append(item)
    valueArr.append([])
    for i in range(1, len(newNameArr)+1):
        if item in str(newNameArr[-i]):
            valueArr[-1].append(newValueArr[-i])

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
plt.ylabel('F1-Score', fontsize=28)
plt.xlabel(xTickName, fontsize=28)

# 设置坐标轴刻度
plt.yticks(np.arange(0.73, 0.92, 0.03), fontsize=26)
plt.xticks(fontsize=26)

# 设置图例
plt.legend(fontsize=24, loc='lower center', bbox_to_anchor=(0.5, 0.97),\
    labelspacing=0.1, handletextpad=1, handlelength=2, ncol=2, columnspacing=1.2)

# 设置坐标轴范围
# plt.ylim(0, 108)

# 设置图片边距
plt.subplots_adjust(left=0.15, right=0.99, top=0.825, bottom=0.15)

# 保存图片
plt.savefig('.\\image\\f1_score_2.pdf')

# 显示图片
plt.show()
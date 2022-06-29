import numpy as np
import matplotlib.pyplot as plt
import random

fileArr = [
    'data_miss_bad_timeout.csv',
    'data_miss_bad_wl.csv',
    'data_miss_good_timeout.csv',
    'data_miss_good_wl.csv',
]

colorArr = [
    '#324665',
    '#3478BF',
    '#40A776',
    '#F15326',
]

markerArr = [
    's',
    'o',
    'd',
    '^'
]

xArr = []
dataArr = []

for curFileName in fileArr:
    inFile = open(curFileName, 'r', encoding='utf-8')

    xArr.append([])
    dataArr.append([])
    headLine = inFile.readline()

    while True:
        curLine = inFile.readline()
        if curLine == '':
            break

        curArr = curLine.strip('\n').split(',')
        xArr[-1].append(int(curArr[0]))
        dataArr[-1].append(int(curArr[1]))


# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(9,6))

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='both')

# 各项参数

for i in range(len(fileArr)):
    curP = plt.plot(xArr[i], dataArr[i], label=fileArr[i].split('.')[0], lw=3)
    
# 设置坐标轴文字
plt.ylabel('yName (unit)', fontsize=28)
plt.xlabel('xName (unit)', fontsize=28)

# 设置坐标轴刻度
plt.yticks(fontsize=26)
plt.xticks(fontsize=26)

# 设置图例
plt.legend(fontsize=16)

# 设置坐标轴范围

# 设置图片边距
plt.subplots_adjust(left=0.195, right=0.99, top=0.975, bottom=0.15)

# 保存图片
# plt.savefig('line.pdf')
# plt.savefig('line.png', dpi=600)

# 显示图片
plt.show()
import numpy as np
import matplotlib.pyplot as plt

inFile = open('storage.csv', 'r')
# inFile.readline()

xTick = []
valueArr = []

while True:
    curLine = inFile.readline()
    if curLine == '':
        break
    curArr = curLine.strip('\n').split(',')

    xTick.append(curArr[0])
    valueArr.append(float(curArr[1])/1024)

# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(9,6))

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='y')

# 柱子的宽度
bar_width = 0.5

curP = plt.bar(range(len(xTick)), valueArr, bar_width, color='#40A776')

# 设置坐标轴文字
plt.ylabel('Storage Overhead (MB)  ', fontsize=34)
# plt.xlabel('Methods', fontsize=28)

# 设置坐标轴刻度
plt.yticks(fontsize=28)
plt.xticks(range(len(xTick)), xTick, fontsize=28, rotation=-20)

# 设置坐标轴范围
# plt.ylim(0, 108)

# 设置图片边距
plt.subplots_adjust(left=0.140, right=0.99, top=0.975, bottom=0.15)

# 保存图片
plt.savefig('storage.pdf')

# 显示图片
plt.show()
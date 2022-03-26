import numpy as np
import matplotlib.pyplot as plt
import random

filePath = 'T15/'

fileNameArr = [
    'percentage2_loop0.csv', 
    'percentage2_loop50.csv', 
    'percentage2_loop100.csv', 
    'percentage2_loop150.csv', 
    'percentage2_loop200.csv', 
]

labelArr = [
    'loop-0',
    'loop-800',
    'loop-1600',
    'loop-2400',
    'loop-3200',
]

xTicks = []
valueArrs = []

for i in range(len(fileNameArr)):
    print(filePath+fileNameArr[i])
    inFile = open(filePath+fileNameArr[i], 'r')
    xTick = inFile.readline().strip('\n').strip(',').split(',')
    valueArr = inFile.readline().strip('\n').strip(',').split(',')
    valueArr = [100 * float(x) for x in valueArr]
    xTicks.append(xTick)
    valueArrs.append(valueArr)

# print(valueArrs)

# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(9,6))

# 生成背后的网格

# 各项参数

for i in range(len(fileNameArr)):
    subfigNum = len(fileNameArr)*100+10+(i+1)
    plt.subplot(subfigNum)
    # curP = plt.scatter(xTicks[i], valueArrs[i], label=labelArr[i], linewidth=3)
    curP = plt.plot(xTicks[i], valueArrs[i], label=labelArr[i], lw=1.5)
    
    plt.grid(True, linestyle='-.', axis='both')
    
    # 设置坐标轴刻度
    plt.yticks(range(0,9,2), range(0,9,2), fontsize=14)
    plt.xticks(range(0,256,15), ['' for i in range(0,256,15)])

    # 设置图例
    plt.legend(fontsize=18, loc='upper right', handlelength=0, handletextpad=0.1)

    # 设置坐标轴范围
    plt.ylim(0, 8)
    plt.xlim(0, 255)

    if i == len(fileNameArr)-1:
        plt.xlabel('the Number of Error Bit per Data Frame', fontsize=24)
        plt.xticks(range(0,256,15), range(0,256,15), fontsize=18, rotation=-35)
    
    if i == 2:
        # 设置坐标轴文字
        plt.ylabel('Percentage (%)', fontsize=24)


# 设置图片边距
plt.subplots_adjust(left=0.07, right=0.97, top=0.985, bottom=0.160, hspace=0.325)

# 保存图片
plt.savefig('err_bit_hlist_split.pdf')

# 显示图片
plt.show()

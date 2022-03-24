import numpy as np
import matplotlib.pyplot as plt
import random

fileNameArr = [
    'percentage_loop0.csv', 
    'percentage_loop50.csv', 
    'percentage_loop100.csv', 
    'percentage_loop150.csv', 
    'percentage_loop200.csv', 
]

labelArr = [
    'loop-0',
    'loop-50',
    'loop-100',
    'loop-150',
    'loop-200',
]

xTicks = []
valueArrs = []

for i in range(len(fileNameArr)):
    inFile = open(fileNameArr[i], 'r')
    xTick = inFile.readline().strip('\n').strip(',').split(',')
    valueArr = inFile.readline().strip('\n').strip(',').split(',')
    valueArr = [100 * float(x) for x in valueArr]
    xTicks.append(xTick)
    valueArrs.append(valueArr)

print(valueArrs)

# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(9,6))

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='both')

# 各项参数

for i in range(len(fileNameArr)):
    curP = plt.plot(xTicks[i], valueArrs[i], label=labelArr[i], linewidth=3)
    
# 设置坐标轴文字
plt.ylabel('Percentage (%)', fontsize=28)
# plt.xlabel('xName (unit)', fontsize=28)

# 设置坐标轴刻度
plt.yticks(fontsize=26)
plt.xticks(range(0,256,5), range(0,256,5), fontsize=26)

# 设置图例
plt.legend(fontsize=26)

# 设置坐标轴范围
plt.ylim(0)
plt.xlim(0, 45)

# 设置图片边距
plt.subplots_adjust(left=0.195, right=0.99, top=0.975, bottom=0.15)

# 保存图片
plt.savefig('err_bit_count.pdf')

# 显示图片
plt.show()

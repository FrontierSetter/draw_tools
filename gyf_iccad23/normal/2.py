import numpy as np
import matplotlib.pyplot as plt
import xlrd
import argparse

xTick = ['4', '5', '6', '7', '8', '9', '10']
valueArr = [0.167, 0.267, 0.379, 0.496, 0.689, 0.872, 1]

print(xTick)
print(valueArr)

# 生成图片实例, figsize的元组是宽高比
fig = plt.figure(figsize=(9,6))

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='y')

# 柱子的宽度
bar_width = 0.6

curP = plt.bar(range(len(xTick)), [x/valueArr[-1] for x in valueArr], bar_width, color='#40A776')

# 设置坐标轴文字
plt.ylabel('Normalized Time Overhead   ', fontsize=30)
plt.xlabel('Cycles', fontsize=30)

# 设置坐标轴刻度
plt.yticks(fontsize=26)
# plt.yticks(np.arange(0,1.01,0.2), fontsize=26)
plt.xticks(range(len(xTick)), xTick, fontsize=26)

# 设置坐标轴范围
# plt.ylim(0, 1.05)

# 设置图片边距
plt.subplots_adjust(left=0.155, right=0.99, top=0.975, bottom=0.15)

# 保存图片
plt.savefig('time.pdf')

# 显示图片
plt.show()
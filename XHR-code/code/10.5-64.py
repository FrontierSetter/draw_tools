import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

# TL
x1 = [68]
y1 = [64/4-1]
# LRC
x2 = [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
y2 = [64/3, 64/4, 64/5, 64/6, 64/7, 64/8, 64/9, 64/10, 64/11, 64/12, 64/13]
# ECWide
x3 = [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
y3 = [64/8, 64/12, 64/16, 64/20, 64/24, 64/28, 64/32, 64/36, 64/40, 64/44, 64/48]
y33 = []
for i in y3:
    y33.append(i-1)
# XHR_min
x4 = [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
y4 = [64/9, 64/12, 64/16, 64/20, 64/25, 64/30, 64/36, 64/42, 64/49, 64/56, 64/64]
y44 = []
for i in y4:
    y44.append(i-1)
fig,ax=plt.subplots(figsize=(6.4,4.8), dpi=100)
# 画图
ax.plot(x1, y1, label='TL', linestyle='', marker='s',  markersize='10')
ax.plot(x2, y2, label='Azure LRC', linestyle='--', marker='p', markersize='10')
ax.plot(x3, y33, label='ECWide CL', linestyle='-', marker='o', markersize='10')
ax.plot(x4, y44, label='XHR_min', linestyle='dotted', marker='x', markersize='10')
# 设置坐标轴
# ax.set_xlim(1, 1.2)
# ax.set_ylim(0, 1.4)
ax.set_xlabel('Redundancy', fontsize=13)
ax.set_ylabel('single chunk cross-rack repair bandwidth', fontsize=13)
ax.set_xscale('linear')
# ax.set_yscale('symlog')
# ax.set_yticks([0, 1, 10, 100])
# 设置刻度
ax.tick_params(axis='both', labelsize=11)
# 显示网格
ax.grid(True, linestyle='-.')
ax.yaxis.grid(True, linestyle='-.')
# 添加图例
legend = ax.legend(loc='best')
# 添加标题
plt.title('k=64')
plt.show()
fig.savefig('./64-1.pdf')
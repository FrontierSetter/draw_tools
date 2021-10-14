import math
from scipy.special import comb
import matplotlib.pyplot as plt
import numpy as np

x5_1 = np.arange(1, 9, 0.01) / 10
y5_1 = np.arange(1, 256, 1)
x5,y5 = np.meshgrid(x5_1,y5_1)
z5 = y5/((1-x5)*x5*100)

def oneFaultCost(XORChunkNum,HHChunkNum):
    return 1/XORChunkNum/HHChunkNum

parityNum=10

XORNums=[i for i in np.arange(1.05, parityNum-1,0.01)]
HHNums=[parityNum-i for i in XORNums]

one=[oneFaultCost(XORNums[i],HHNums[i]) for i in range(len(XORNums))]

two = []

for i in one:
    print(i)
    two.append(i*128)

XORNums=np.divide(XORNums,10)

plt.figure(figsize=(6.4,4.8), dpi=100)
    # 画图
# ax.plot(XORNums, two, color='red', label='k=128', linestyle='-', cmap=plt.get_cmap('rainbow'))
plt.scatter(XORNums, two, label='k=128',c=z5.resize(1),  cmap=plt.get_cmap('rainbow'), edgecolors='none')
# 设置坐标轴
# ax.set_xlim(1, 1.2)
# ax.set_ylim(0, 1.4)
plt.xlabel('$m_{l} / (m_{l} + m_{g} + 1)$', fontsize=22)
plt.ylabel('$\lambda$', fontsize=22)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
# ax.set_yscale('symlog')
# ax.set_yticks([0, 1, 10, 100])
# 显示网格
plt.grid(True, linestyle='-.')
# 添加图例
# legend = ax.legend(loc='best', fontsize=13)
# 添加标题
plt.title(f'$m_l+m_g+1=10$, k=128', fontsize=22)
plt.subplots_adjust(top=0.915,bottom=0.155,left=0.125,right=0.985)

plt.savefig('GeneralCrossRack.pdf')
# plt.show()


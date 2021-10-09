import math
from scipy.special import comb
import matplotlib.pyplot as plt
import numpy as np

def oneFaultCost(XORChunkNum,HHChunkNum):
    return 1/XORChunkNum/HHChunkNum

parityNum=20

XORNums=[i for i in np.arange(1.05, parityNum-1,0.1)]
HHNums=[parityNum-i for i in XORNums]

one=[oneFaultCost(XORNums[i],HHNums[i]) for i in range(len(XORNums))]

XORNums=np.divide(XORNums,20)

fig,ax=plt.subplots(figsize=(6.4,4.8), dpi=100)
    # 画图
ax.plot(XORNums, one, label='one error', linestyle='-')
# 设置坐标轴
# ax.set_xlim(1, 1.2)
# ax.set_ylim(0, 1.4)
ax.set_xlabel('$m_{l}$', fontsize=13)
ax.set_ylabel('Cross Rack Bandwidth', fontsize=13)
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
plt.title(f'$m_l+m_g=p$')
plt.show()
fig.savefig(f'./generalGeneralCrossRack.pdf')


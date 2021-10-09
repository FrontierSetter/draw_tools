import math
from scipy.special import comb
import matplotlib.pyplot as plt
import numpy as np

k=128
n=143
parityNum=n-k

XORNums=[i for i in range(3, parityNum -1)]
HHNums=[parityNum-i for i in XORNums]
p=[i for i in range(6,28)]
redundancy1=[(1+i+128)/128 for i in p]
redundancy2=[(2+i+128)/128 for i in p]
redundancy3=[(3+i+128)/128 for i in p]
fig,ax=plt.subplots(figsize=(9,6), dpi=100)
    # 画图
ax.plot(p, redundancy1, label='$m_g=1$', linestyle='-', marker='s',  markersize='5')
ax.plot(p, redundancy2, label='$m_g=2$', linestyle='-', marker='p', markersize='5')
ax.plot(p, redundancy3, label='$m_g=3$', linestyle='-', marker='o', markersize='5')
# 设置坐标轴
# ax.set_xlim(1, 1.2)
# ax.set_ylim(0, 1.4)
ax.set_xlabel('$m_h$+$m_l$', fontsize=16)
ax.set_ylabel('Storage Redundancy', fontsize=16)
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
plt.legend(fontsize=18)
# 添加标题
plt.title(f'k={k}')
plt.show()
fig.savefig(f'./sameRSStorageRedundancy.pdf')


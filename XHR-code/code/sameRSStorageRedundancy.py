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

plt.figure(figsize=(9,6))
    # 画图
plt.plot(p, redundancy1, label='$m_g=1$', linestyle='-', marker='^',  markersize=12, linewidth=4)
plt.plot(p, redundancy2, label='$m_g=2$', linestyle='-', marker='D',  markersize=12, linewidth=4)
plt.plot(p, redundancy3, label='$m_g=3$', linestyle='-', marker='o',  markersize=12, linewidth=4)
plt.xlabel('$m_h$+$m_l$', fontsize=26)
plt.ylabel('Storage Redundancy', fontsize=26)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# 显示网格
plt.grid(True, linestyle='-.')
# 添加图例
plt.legend(fontsize=22)
# 添加标题
plt.title(f'k={k}', fontsize=26)
plt.subplots_adjust(top=0.925,bottom=0.13,left=0.145,right=0.99,)
plt.savefig(f'./sameRSStorageRedundancy.pdf')
plt.show()


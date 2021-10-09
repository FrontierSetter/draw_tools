import math
from scipy.special import comb
import matplotlib.pyplot as plt
import numpy as np

k=128
n=143
parityNum=n-k

mRS=[i for i in range(1,7)]
ft3=[3+i for i in mRS]
ft4=[4+i for i in mRS]
fig,ax=plt.subplots(figsize=(9,6), dpi=100)
    # 画图
ax.plot(mRS, ft3, label='$r_h=3$', linestyle='-', marker='s',  markersize='5')
ax.plot(mRS, ft4, label='$r_h=4$', linestyle='-', marker='p', markersize='5')
# 设置坐标轴
# ax.set_xlim(1, 1.2)
# ax.set_ylim(0, 1.4)
ax.set_xlabel('$m_g$', fontsize=16)
ax.set_ylabel('Fault Tolerance', fontsize=16)
ax.set_xscale('linear')
# ax.set_yscale('symlog')
# ax.set_yticks([0, 1, 10, 100])
# 设置刻度
ax.tick_params(axis='both', labelsize=11)
# 显示网格
ax.grid(True, linestyle='-.')
ax.yaxis.grid(True, linestyle='-.')
# 添加图例
legend = ax.legend(loc='best',fontsize=16)
# 添加标题
plt.title(f'k={k}, n={n}')
plt.legend(fontsize=18)
plt.show()
fig.savefig(f'./sameNFaultTor.pdf')


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
plt.figure(figsize=(9,6))
plt.plot(mRS, ft3, label='$r_h=3$', linestyle='-', marker='^',  markersize=12, linewidth=4)
plt.plot(mRS, ft4, label='$r_h=4$', linestyle='-', marker='D',  markersize=12, linewidth=4)
# ax.set_ylim(0, 1.4)
plt.xlabel('$m_g$', fontsize=26)
plt.ylabel('Fault Tolerance', fontsize=26)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.grid(True, linestyle='-.')
# 添加标题
plt.title(f'k={k}, n={n}', fontsize=26)
plt.legend(fontsize=22)
plt.subplots_adjust(top=0.925,bottom=0.13,left=0.125,right=0.99,)
plt.savefig(f'./sameNFaultTor.pdf')
plt.show()


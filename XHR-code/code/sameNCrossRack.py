import math
from scipy.special import comb
import matplotlib.pyplot as plt
import numpy as np

def oneFaultCost(XORChunkNum,HHChunkNum,dataChunkNum):
    return dataChunkNum/XORChunkNum/HHChunkNum

def twoFaultCost(XORChunkNum,HHChunkNum,dataChunkNum,RHH):
    rackNum=dataChunkNum/HHChunkNum
    ChunkNumInOneXOR=dataChunkNum/XORChunkNum
    rackNumInOneXOR=max(1,rackNum/XORChunkNum)
    # rackNum=math.ceil(dataChunkNum/HHChunkNum)
    # ChunkNumInOneXOR=math.ceil(dataChunkNum/XORChunkNum)
    # rackNumInOneXOR=math.ceil(rackNum/XORChunkNum)

    inOneXOR=XORChunkNum*comb(ChunkNumInOneXOR,2)/comb(dataChunkNum,2)
    return inOneXOR*rackNum+(1-inOneXOR)*(rackNumInOneXOR-1)*2

def threeFaultCost(XORChunkNum,HHChunkNum,dataChunkNum,RHH):
    rackNum=dataChunkNum/HHChunkNum
    ChunkNumInOneXOR=dataChunkNum/XORChunkNum
    rackNumInOneXOR=max(1,rackNum/XORChunkNum)
    # rackNum=math.ceil(dataChunkNum/HHChunkNum)
    # ChunkNumInOneXOR=math.ceil(dataChunkNum/XORChunkNum)
    # rackNumInOneXOR=math.ceil(rackNum/XORChunkNum)

    inThreeXOR=comb(XORChunkNum,3)*(ChunkNumInOneXOR**3)/comb(dataChunkNum,3)
    
    return (1-inThreeXOR)*rackNum+inThreeXOR*(rackNumInOneXOR-1)*3

k=128
n=143
parityNum=n-k

XORNums=[i for i in range(2, parityNum-1)]
HHNums=[parityNum-i for i in XORNums]

one=[oneFaultCost(XORNums[i],HHNums[i],k) for i in range(len(XORNums))]
two4=[twoFaultCost(XORNums[i],HHNums[i],k,4) for i in range(len(XORNums))]
three4=[threeFaultCost(XORNums[i],HHNums[i],k,4) for i in range(len(XORNums))]
one=[oneFaultCost(XORNums[i],HHNums[i],k) for i in range(len(XORNums))]
two3=[twoFaultCost(XORNums[i],HHNums[i],k,3) for i in range(len(XORNums))]
three3=[threeFaultCost(XORNums[i],HHNums[i],k,3) for i in range(len(XORNums))]
fig,ax=plt.subplots(figsize=(9,6), dpi=100)
    # 画图
ax.plot(XORNums, one, label='single failure, $r_h$=3 or 4', linestyle='-', marker='s',  markersize='5')
ax.plot(XORNums, two4, label='double failure, $r_h$=3 or 4', linestyle='-', marker='p', markersize='5')
ax.plot(XORNums, three4, label='triple failure, $r_h$=3 or 4', linestyle='-', marker='o', markersize='5')
# 设置坐标轴
# ax.set_xlim(1, 1.2)
# ax.set_ylim(0, 1.4)
ax.set_xlabel('$m_l$', fontsize=16)
ax.set_ylabel('Cross Rack Bandwidth', fontsize=16)
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
plt.legend(fontsize=16)
plt.show()
fig.savefig(f'./sameNCrossRack.pdf')


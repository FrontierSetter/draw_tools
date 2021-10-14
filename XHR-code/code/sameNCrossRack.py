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

plt.figure(figsize=(9,6))
    # 画图
plt.plot(XORNums, one, label='single failure, $r_h$=3 or 4', linestyle='-', marker='^',  markersize=12, linewidth=4)
plt.plot(XORNums, two4, label='double failure, $r_h$=3 or 4', linestyle='-', marker='D', markersize=12, linewidth=4)
plt.plot(XORNums, three4, label='triple failure, $r_h$=3 or 4', linestyle='-', marker='o', markersize=12, linewidth=4)
# 设置坐标轴
# ax.set_xlim(1, 1.2)
# ax.set_ylim(0, 1.4)
plt.xlabel('$m_l$', fontsize=26)
plt.ylabel('Cross Rack Bandwidth', fontsize=26)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.grid(True, linestyle='-.')
# 添加标题
plt.title(f'k={k}, n={n}', fontsize=26)
plt.legend(fontsize=22)
plt.subplots_adjust(top=0.925,bottom=0.13,left=0.125,right=0.99,)

plt.savefig(f'./sameNCrossRack.pdf')
plt.show()


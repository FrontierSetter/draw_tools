import math
from scipy.special import comb
import matplotlib.pyplot as plt
import numpy as np

def oneFaultCost(XORChunkNum,HHChunkNum,dataChunkNum):
    if XORChunkNum==1:
        return dataChunkNum
    return dataChunkNum/XORChunkNum

def twoFaultCost(XORChunkNum,HHChunkNum,dataChunkNum,RHH):
    if XORChunkNum==1:
        return dataChunkNum
    
    rackNum=dataChunkNum/HHChunkNum
    ChunkNumInOneXOR=dataChunkNum/XORChunkNum
    rackNumInOneXOR=rackNum/XORChunkNum
    ChunkNumInOneHH=math.ceil(dataChunkNum/HHChunkNum)
    # rackNum=math.ceil(dataChunkNum/HHChunkNum)
    # ChunkNumInOneXOR=math.ceil(dataChunkNum/XORChunkNum)
    # rackNumInOneXOR=math.ceil(rackNum/XORChunkNum)

    inOneXOR=XORChunkNum*comb(ChunkNumInOneXOR,2)/comb(dataChunkNum,2)

    inTwoXOR=1-inOneXOR

    inOneHH=HHChunkNum*comb(ChunkNumInOneHH,2)/comb(dataChunkNum,2)

    inTwoHH=1-inOneHH
    
    return inOneXOR*rackNum*RHH+inTwoXOR*inTwoHH*ChunkNumInOneXOR*2+inTwoXOR*inOneHH*min(ChunkNumInOneXOR*2,rackNum*RHH)

def threeFaultCost(XORChunkNum,HHChunkNum,dataChunkNum,RHH):
    if XORChunkNum==1:
        return dataChunkNum
    
    # RHH=min(RHH,HHChunkNum)
    rackNum=dataChunkNum/HHChunkNum
    ChunkNumInOneXOR=dataChunkNum/XORChunkNum
    rackNumInOneXOR=rackNum/XORChunkNum
    # rackNum=math.ceil(dataChunkNum/HHChunkNum)
    # ChunkNumInOneXOR=math.ceil(dataChunkNum/XORChunkNum)
    # rackNumInOneXOR=math.ceil(rackNum/XORChunkNum)
    totalInterRack=0

    inThreeXOR=comb(XORChunkNum,3)*(ChunkNumInOneXOR**3)/comb(dataChunkNum,3)
    # print(f"3:{inThreeXOR}")
    inOneXOR=XORChunkNum*comb(math.floor(ChunkNumInOneXOR),3)/comb(dataChunkNum,3)
    # print(f"1:{inOneXOR}")
    
    return (1-inThreeXOR-inOneXOR)*(RHH*rackNum+ChunkNumInOneXOR)+inThreeXOR*min(ChunkNumInOneXOR*3,dataChunkNum)+inOneXOR*(RHH*rackNum)

k=128
n=143
parityNum=n-k

XORNums=[i for i in range(3, parityNum -1)]
HHNums=[parityNum-i for i in XORNums]

one=[oneFaultCost(XORNums[i],HHNums[i],k) for i in range(len(XORNums))]
two4=[twoFaultCost(XORNums[i],HHNums[i],k,4) for i in range(len(XORNums))]
three4=[threeFaultCost(XORNums[i],HHNums[i],k,4) for i in range(len(XORNums))]
one=[oneFaultCost(XORNums[i],HHNums[i],k) for i in range(len(XORNums))]
two3=[twoFaultCost(XORNums[i],HHNums[i],k,3) for i in range(len(XORNums))]
three3=[threeFaultCost(XORNums[i],HHNums[i],k,3) for i in range(len(XORNums))]
fig,ax=plt.subplots(figsize=(9,6), dpi=100)
    # 画图
ax.plot(XORNums, one, label='single failure, $r_h=$3 or 4', linestyle='-', marker='s',  markersize='5')
ax.plot(XORNums, two4, label='double failure, $r_h=4$', linestyle='-', marker='p', markersize='5')
ax.plot(XORNums, three4, label='triple failure, $r_h=4$', linestyle='-', marker='o', markersize='5')
ax.plot(XORNums, two3, label='double failure, $r_h=3$', linestyle='-', marker='p', markersize='5')
ax.plot(XORNums, three3, label='triple failure, $r_h=3$', linestyle='-', marker='o', markersize='5')
# 设置坐标轴
# ax.set_xlim(1, 1.2)
# ax.set_ylim(0, 1.4)
ax.set_xlabel('$x_l$', fontsize=16)
ax.set_ylabel('I/O Request Counts', fontsize=16)
ax.set_ylim([5,120])
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
plt.legend(fontsize=14)
# 添加标题
plt.title(f'k={k}, n={n}')
plt.show()
fig.savefig(f'./sameNNodeVisit.pdf')


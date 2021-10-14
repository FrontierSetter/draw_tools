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
plt.figure(figsize=(9,6))
    # 画图
plt.plot(XORNums, one, label='single failure, $r_h=$3 or 4', linestyle='-', marker='s',  markersize=12, linewidth=4)
plt.plot(XORNums, two4, label='double failure, $r_h=4$', linestyle='-', marker='p',  markersize=12, linewidth=4)
plt.plot(XORNums, three4, label='triple failure, $r_h=4$', linestyle='-', marker='o',  markersize=12, linewidth=4)
plt.plot(XORNums, two3, label='double failure, $r_h=3$', linestyle='-', marker='^',  markersize=12, linewidth=4)
plt.plot(XORNums, three3, label='triple failure, $r_h=3$', linestyle='-', marker='D',  markersize=12, linewidth=4)

plt.xlabel('$x_l$', fontsize=26)
plt.ylabel('I/O Request Counts', fontsize=26)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.ylim([5,160])
plt.grid(True, linestyle='-.')
plt.legend(columnspacing=0.7, ncol=1, fontsize=20)
# 添加标题
plt.title(f'k={k}, n={n}', fontsize=26)
plt.subplots_adjust(top=0.925,bottom=0.13,left=0.125,right=0.99,)
plt.savefig(f'./sameNNodeVisit.pdf')
plt.show()


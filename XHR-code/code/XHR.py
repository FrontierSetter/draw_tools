import sys
import math
from scipy.special import comb

def inOneXOR(x,y,dataChunkNum,XORChunkNum,HHChunkNum):
    dataChunkNum,XORChunkNum,HHChunkNum

def getXHRInterRackBandwidth(dataChunkNum,XORChunkNum,HHChunkNum):
    rackNum=math.ceil(dataChunkNum/HHChunkNum)
    ChunkNumInOneXOR=math.ceil(dataChunkNum/XORChunkNum)
    rackNumInOneXOR=math.ceil(rackNum/XORChunkNum)
    totalInterRack=0

    inOneXOR=XORChunkNum*(comb(ChunkNumInOneXOR,2))/comb(dataChunkNum,2)
    
    return inOneXOR*rackNum+(1-inOneXOR)*rackNumInOneXOR

def getECWideInterRackBandwidth(dataChunkNum,parityChunkNum):
    rackNum=math.ceil(dataChunkNum/4)
    XORChunkNum=parityChunkNum-4
    ChunkNumInOneXOR=math.ceil(dataChunkNum/XORChunkNum)
    rackNumInOneXOR=math.ceil(rackNum/XORChunkNum)
    totalInterRack=0

    inOneXOR=parityChunkNum*(comb(ChunkNumInOneXOR,2))/comb(dataChunkNum,2)
    
    return inOneXOR*rackNum+(1-inOneXOR)*rackNumInOneXOR

if __name__=='__main__':
    parameters=[
        (3,3),
        (3,4),
        (4,4),
        (4,5),
        (5,5),
        (5,6),
        (6,5),
        (6,6),
        (6,7),
        (7,7)
    ]
    for i,j in parameters:
        print(getXHRInterRackBandwidth(64,i,j),end='\t\t')
        print(getECWideInterRackBandwidth(64,i+j))
import math
from scipy.special import comb

def getXHRInterRackBandwidth(dataChunkNum,XORChunkNum,HHChunkNum):
    rackNum=dataChunkNum/HHChunkNum
    ChunkNumInOneXOR=dataChunkNum/XORChunkNum
    rackNumInOneXOR=max(1,rackNum/XORChunkNum)
    # rackNum=math.ceil(dataChunkNum/HHChunkNum)
    # ChunkNumInOneXOR=math.ceil(dataChunkNum/XORChunkNum)
    # rackNumInOneXOR=math.ceil(rackNum/XORChunkNum)

    inOneXOR=XORChunkNum*comb(ChunkNumInOneXOR,2)/comb(dataChunkNum,2)
    
    return inOneXOR*rackNum+(1-inOneXOR)*(rackNumInOneXOR-1)*2
    
def getXHRNodeVisit(dataChunkNum,XORChunkNum,HHChunkNum,RHH):
    rackNum=(dataChunkNum+XORChunkNum+HHChunkNum)/HHChunkNum
    ChunkNumInOneXOR=dataChunkNum/XORChunkNum
    rackNumInOneXOR=dataChunkNum/HHChunkNum/XORChunkNum
    ChunkNumInOneHH=dataChunkNum/HHChunkNum
    # rackNum=math.ceil(dataChunkNum/HHChunkNum)
    # ChunkNumInOneXOR=math.ceil(dataChunkNum/XORChunkNum)
    # rackNumInOneXOR=math.ceil(rackNum/XORChunkNum)

    inOneXOR=XORChunkNum*comb(ChunkNumInOneXOR,2)/comb(dataChunkNum,2)

    inTwoXOR=1-inOneXOR

    inOneHH=HHChunkNum*comb(ChunkNumInOneHH,2)/comb(dataChunkNum,2)

    inTwoHH=1-inOneHH
    
    return inOneXOR*rackNum*RHH+inTwoXOR*inTwoHH*ChunkNumInOneXOR*2+inTwoXOR*inOneHH*min(ChunkNumInOneXOR*2,rackNum*RHH)

def getECWideInterRackBandwidth(dataChunkNum,parityChunkNum):
    rackNum=(dataChunkNum+parityChunkNum)/4
    # rackNum=math.ceil(dataChunkNum/4)
    XORChunkNum=parityChunkNum-4
    ChunkNumInOneXOR=dataChunkNum/XORChunkNum
    rackNumInOneXOR=max(1,ChunkNumInOneXOR/4)
    # ChunkNumInOneXOR=math.ceil(dataChunkNum/XORChunkNum)
    # rackNumInOneXOR=math.ceil(rackNum/XORChunkNum)
    totalInterRack=0

    inOneXOR=XORChunkNum*comb(ChunkNumInOneXOR,2)/comb(dataChunkNum,2)
    
    return inOneXOR*rackNum+(1-inOneXOR)*(rackNumInOneXOR-1)*2

def getECWideNodeVisit(dataChunkNum,parityChunkNum):
    rackNum=(dataChunkNum+parityChunkNum)/4
    # rackNum=math.ceil(dataChunkNum/4)
    XORChunkNum=parityChunkNum-4
    ChunkNumInOneXOR=dataChunkNum/XORChunkNum
    # ChunkNumInOneXOR=math.ceil(dataChunkNum/XORChunkNum)
    # rackNumInOneXOR=math.ceil(rackNum/XORChunkNum)
    totalInterRack=0

    inOneXOR=XORChunkNum*comb(ChunkNumInOneXOR,2)/comb(dataChunkNum,2)
    
    return inOneXOR*(dataChunkNum+parityChunkNum)+(1-inOneXOR)*min(ChunkNumInOneXOR*2,dataChunkNum)

def getLRCInterRackBandwidth(dataChunkNum,parityChunkNum):
    rackNum=dataChunkNum
    # rackNum=math.ceil(dataChunkNum/4)
    XORChunkNum=parityChunkNum-4
    ChunkNumInOneXOR=dataChunkNum/XORChunkNum
    rackNumInOneXOR=rackNum/XORChunkNum
    # ChunkNumInOneXOR=math.ceil(dataChunkNum/XORChunkNum)
    # rackNumInOneXOR=math.ceil(rackNum/XORChunkNum)
    totalInterRack=0

    inOneXOR=parityChunkNum*comb(ChunkNumInOneXOR,2)/comb(dataChunkNum,2)
    return inOneXOR*rackNum+(1-inOneXOR)*rackNumInOneXOR

def getLRCNodeVisit(dataChunkNum,parityChunkNum):
    return getECWideNodeVisit(dataChunkNum,parityChunkNum)

def getTLInterRackBandwidth(dataChunkNum):
    rackNum=dataChunkNum/4
    
    return rackNum

def getTLNodeVisit(dataChunkNum,parityChunkNum):
    
    return dataChunkNum+parityChunkNum


def getBandwidth(method):
    if method==1:
        dataChunks=[(64,2,8),(128,3,16),(192,5,24),(256,7,32)]
        for (data,pmin,pmax) in dataChunks:
            print(f"k={data}, n start from {data+pmin*2}, end in {data+pmax*2}")
            for i in range(pmin,pmax+1):
                for j in range(2):
                    print(f"{getXHRInterRackBandwidth(data,i,i+j):.3f}")
                    # print(f"{getECWideInterRackBandwidth(data,i+i+j):.3f}")
                    # print(f"{getLRCInterRackBandwidth(data,i+i+j):.3f}")
                    # print(f"{getTLInterRackBandwidth(data):.3f}")
    if method==2:
        dataChunks=[(64,3,8),(128,3,16),(192,5,24),(256,7,32)]
        for (data,pmin,pmax) in dataChunks:
            print(f"k={data}, n start from {data+pmin*2}, end in {data+pmax*2}")
            for i in range(pmin,pmax+1):
                for j in range(2):
                    # print(f"{getXHRInterRackBandwidth(data,i,i+j):.3f}")
                    print(f"{getECWideInterRackBandwidth(data,i+i+j):.3f}")
                    # print(f"{getLRCInterRackBandwidth(data,i+i+j):.3f}")
                    # print(f"{getTLInterRackBandwidth(data):.3f}")
    if method==3:
        dataChunks=[(64,3,8),(128,3,16),(192,5,24),(256,7,32)]
        for (data,pmin,pmax) in dataChunks:
            print(f"k={data}, n start from {data+pmin*2}, end in {data+pmax*2}")
            for i in range(pmin,pmax+1):
                for j in range(2):
                    # print(f"{getXHRInterRackBandwidth(data,i,i+j):.3f}")
                    # print(f"{getECWideInterRackBandwidth(data,i+i+j):.3f}")
                    print(f"{getLRCInterRackBandwidth(data,i+i+j):.3f}")
                    # print(f"{getTLInterRackBandwidth(data):.3f}")
    if method==4:
        dataChunks=[(64,2,8),(128,3,16),(192,5,24),(256,7,32)]
        for (data,pmin,pmax) in dataChunks:
            print(f"k={data}, n start from {data+pmin*2}, end in {data+pmax*2}")
            for i in range(pmin,pmax+1):
                for j in range(2):
                    # print(f"{getXHRInterRackBandwidth(data,i,i+j):.3f}")
                    # print(f"{getECWideInterRackBandwidth(data,i+i+j):.3f}")
                    # print(f"{getLRCInterRackBandwidth(data,i+i+j):.3f}")
                    print(f"{getTLInterRackBandwidth(data):.3f}")

def getNodeVisit(method):
    if method==1:
        dataChunks=[(64,3,8),(128,3,16),(192,6,24),(256,7,32)]
        for (data,pmin,pmax) in dataChunks:
            print(f"k={data}, n start from {data+pmin*2}, end in {data+pmax*2}")
            for i in range(pmin,pmax+1):
                for j in range(2):
                    print(f"{getXHRNodeVisit(data,i,i+j,4):.3f}")
                    # print(f"{getECWideNodeVisit(data,i+i+j):.3f}")
                    # print(f"{getLRCNodeVisit(data,i+i+j):.3f}")
                    # print(f"{getTLNodeVisit(data):.3f}")
    if method==2:
        dataChunks=[(64,3,8),(128,3,16),(192,6,24),(256,7,32)]
        for (data,pmin,pmax) in dataChunks:
            print(f"k={data}, n start from {data+pmin*2}, end in {data+pmax*2}")
            for i in range(pmin,pmax+1):
                for j in range(2):
                    # print(f"{getXHRNodeVisit(data,i,i+j):.3f}")
                    print(f"{getECWideNodeVisit(data,i+i+j):.3f}")
                    # print(f"{getLRCNodeVisit(data,i+i+j):.3f}")
                    # print(f"{getTLNodeVisit(data):.3f}")
    if method==3:
        dataChunks=[(64,3,8),(128,3,16),(192,6,24),(256,7,32)]
        for (data,pmin,pmax) in dataChunks:
            print(f"k={data}, n start from {data+pmin*2}, end in {data+pmax*2}")
            for i in range(pmin,pmax+1):
                for j in range(2):
                    # print(f"{getXHRNodeVisit(data,i,i+j):.3f}")
                    # print(f"{getECWideNodeVisit(data,i+i+j):.3f}")
                    print(f"{getLRCNodeVisit(data,i+i+j):.3f}")
                    # print(f"{getTLNodeVisit(data):.3f}")
    if method==4:
        dataChunks=[(64,3,8),(128,3,16),(192,6,24),(256,7,32)]
        for (data,pmin,pmax) in dataChunks:
            print(f"k={data}, n start from {data+pmin*2}, end in {data+pmax*2}")
            for i in range(pmin,pmax+1):
                for j in range(2):
                    # print(f"{getXHRNodeVisit(data,i,i+j):.3f}")
                    # print(f"{getECWideNodeVisit(data,i+i+j):.3f}")
                    # print(f"{getLRCNodeVisit(data,i+i+j):.3f}")
                    print(f"{getTLNodeVisit(data):.3f}")
    if method==5:
        dataChunks=[(64,3,8),(128,3,16),(192,6,24),(256,7,32)]
        for (data,pmin,pmax) in dataChunks:
            print(f"k={data}, n start from {data+pmin*2}, end in {data+pmax*2}")
            for i in range(pmin,pmax+1):
                for j in range(2):
                    print(f"{getXHRNodeVisit(data,i,i+j,i+j):.3f}")
                    # print(f"{getECWideNodeVisit(data,i+i+j):.3f}")
                    # print(f"{getLRCNodeVisit(data,i+i+j):.3f}")
                    # print(f"{getTLNodeVisit(data):.3f}")

if __name__=='__main__':
    getNodeVisit(5)
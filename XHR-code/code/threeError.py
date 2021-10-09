import math
from scipy.special import comb

def getXHRInterRackBandwidth(dataChunkNum,XORChunkNum,HHChunkNum):
    rackNum=dataChunkNum/HHChunkNum
    ChunkNumInOneXOR=dataChunkNum/XORChunkNum
    rackNumInOneXOR=max(1,rackNum/XORChunkNum)
    # rackNum=math.ceil(dataChunkNum/HHChunkNum)
    # ChunkNumInOneXOR=math.ceil(dataChunkNum/XORChunkNum)
    # rackNumInOneXOR=math.ceil(rackNum/XORChunkNum)

    inThreeXOR=comb(XORChunkNum,3)*(ChunkNumInOneXOR**3)/comb(dataChunkNum,3)
    
    return (1-inThreeXOR)*rackNum+inThreeXOR*(rackNumInOneXOR-1)*3

def getXHRNodeVisit(dataChunkNum,XORChunkNum,HHChunkNum,RHH):
    RHH=min(RHH,HHChunkNum)
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
    
    return (1-inThreeXOR-inOneXOR)*min((RHH*rackNum+ChunkNumInOneXOR),dataChunkNum+3)+inThreeXOR*min(ChunkNumInOneXOR*3,dataChunkNum)+inOneXOR*(RHH*rackNum)

def getECWideInterRackBandwidth(dataChunkNum,parityChunkNum):
    rackNum=(dataChunkNum+parityChunkNum)/4
    # rackNum=math.ceil(dataChunkNum/4)
    XORChunkNum=parityChunkNum-4
    ChunkNumInOneXOR=dataChunkNum/XORChunkNum
    rackNumInOneXOR=max(1,ChunkNumInOneXOR/4)
    # ChunkNumInOneXOR=math.ceil(dataChunkNum/XORChunkNum)
    # rackNumInOneXOR=math.ceil(rackNum/XORChunkNum)
    totalInterRack=0

    inThreeXOR=comb(XORChunkNum,3)*(ChunkNumInOneXOR**3)/comb(dataChunkNum,3)
    
    return (1-inThreeXOR)*rackNum+inThreeXOR*(rackNumInOneXOR-1)*3

def getECWideNodeVisit(dataChunkNum,parityChunkNum):
    rackNum=dataChunkNum/4
    # rackNum=math.ceil(dataChunkNum/4)
    XORChunkNum=parityChunkNum-4
    ChunkNumInOneXOR=dataChunkNum/XORChunkNum
    rackNumInOneXOR=rackNum/XORChunkNum
    # ChunkNumInOneXOR=math.ceil(dataChunkNum/XORChunkNum)
    # rackNumInOneXOR=math.ceil(rackNum/XORChunkNum)
    totalInterRack=0

    inThreeXOR=comb(XORChunkNum,3)*(ChunkNumInOneXOR**3)/comb(dataChunkNum,3)
    
    return (1-inThreeXOR)*(dataChunkNum+parityChunkNum)+inThreeXOR*ChunkNumInOneXOR*3

def getLRCInterRackBandwidth(dataChunkNum,parityChunkNum):
    rackNum=(dataChunkNum+parityChunkNum)
    XORChunkNum=parityChunkNum-4
    ChunkNumInOneXOR=dataChunkNum/XORChunkNum
    rackNumInOneXOR=ChunkNumInOneXOR
    totalInterRack=0

    inThreeXOR=comb(XORChunkNum,3)*(ChunkNumInOneXOR**3)/comb(dataChunkNum,3)
    
    return (1-inThreeXOR)*rackNum+inThreeXOR*rackNumInOneXOR*3
    
    return (1-inThreeXOR)*rackNum+inThreeXOR*rackNumInOneXOR*3

def getLRCNodeVisit(dataChunkNum,parityChunkNum):
    rackNum=dataChunkNum+parityChunkNum
    # rackNum=math.ceil(dataChunkNum/4)
    XORChunkNum=parityChunkNum-4
    ChunkNumInOneXOR=dataChunkNum/XORChunkNum
    rackNumInOneXOR=rackNum/XORChunkNum
    # ChunkNumInOneXOR=math.ceil(dataChunkNum/XORChunkNum)
    # rackNumInOneXOR=math.ceil(rackNum/XORChunkNum)
    totalInterRack=0

    inThreeXOR=comb(XORChunkNum,3)*(ChunkNumInOneXOR**3)/comb(dataChunkNum,3)
    
    return (1-inThreeXOR)*(dataChunkNum+parityChunkNum)+inThreeXOR*ChunkNumInOneXOR*3

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
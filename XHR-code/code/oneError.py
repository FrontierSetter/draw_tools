def getXHRInterRackBandwidth(dataChunkNum,XORChunkNum,HHChunkNum):
    return max(dataChunkNum/XORChunkNum/HHChunkNum-1,0)
    
def getECWideInterRackBandwidth(dataChunkNum,parityChunkNum):
    return dataChunkNum/(parityChunkNum-4)/4-1

def getLRCInterRackBandwidth(dataChunkNum,parityChunkNum):
    return dataChunkNum/(parityChunkNum-4)

def getTLInterRackBandwidth(dataChunkNum):
    return dataChunkNum/4

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

if __name__=='__main__':
    getBandwidth(2)
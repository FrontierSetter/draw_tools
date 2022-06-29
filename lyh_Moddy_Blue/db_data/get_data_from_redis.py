import sys
import redis
import argparse
import time
sys.path.append("..\\header")
from sortCache import *

parser = argparse.ArgumentParser(description='画性能图')
parser.add_argument('-f','--file')
parser.add_argument('-g','--gap')
parser.add_argument('-b','--begin')
parser.add_argument('-t','--target')
parser.add_argument('-d','--db')

args = parser.parse_args()
print(args)
totalProg = 50

timeGap = int(args.gap)
if args.target == 'ckvp':
    # ckvp
    r = redis.Redis(host='9.4.7.33', port=12002, db = int(args.db), password="360:tencent123", decode_responses=True)
elif args.target == 'dev_redis':
    # dev-redis
    r = redis.Redis(host='9.135.251.44', port=6380, db = int(args.db), password='XMRFv*5473rXxf', decode_responses=True)
else:
    exit

outHyFile = open(args.file+"_hy.csv", 'w', encoding='utf-8')
outAccessFile = open(args.file+"_access.csv", 'w', encoding='utf-8')

progressResult = r.hgetall('progress')

beginStamp = int(args.begin)
endStamp = max([int(x) for x in progressResult.values()])

cacheName = [cn for cn in progressResult.keys()]
cacheName.sort(key=functools.cmp_to_key(sortCache))
resultHy = [0]*len(cacheName)
resultAccess = [0]*len(cacheName)

outHyFile.write("%s,%s\n" % ("timestamp", ','.join(cacheName)))
outAccessFile.write("%s,%s\n" % ("timestamp", ','.join(cacheName)))

startTime = time.perf_counter()
for curTime in range(beginStamp, endStamp+1, timeGap):
    curResult = r.hgetall(str(curTime))

    hySuffix = "_total_hy_size"
    for i in range(len(cacheName)):
        if cacheName[i]+hySuffix not in curResult:
            resultHy[i] = ''
        else:
            resultHy[i] = str(curResult[cacheName[i]+hySuffix])
    outHyFile.write("%s,%s\n" % (str(curTime), ','.join(resultHy)))
    
    accessSuffix = "_total_access_size"
    for i in range(len(cacheName)):
        if cacheName[i]+accessSuffix not in curResult:
            resultAccess[i] = ''
        else:
            resultAccess[i] = str(curResult[cacheName[i]+accessSuffix])
    outAccessFile.write("%s,%s\n" % (str(curTime), ','.join(resultAccess)))

    donePart = int((curTime-beginStamp)/(endStamp+1-beginStamp)*totalProg)
    remainPart = (totalProg-donePart)
    percentPart = (curTime-beginStamp)/(endStamp+1-beginStamp)*100
    durTime = time.perf_counter() - startTime
    print("\r{:^3.0f}%[{}{}]{:.2f}s".format(percentPart,donePart * '*',remainPart * '.',durTime),end = "")

outAccessFile.close()
outHyFile.close()
    




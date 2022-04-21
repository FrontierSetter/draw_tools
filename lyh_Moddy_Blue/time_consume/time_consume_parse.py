import sys
import matplotlib.pyplot as plt
import numpy as np
import functools
sys.path.append("..\\header")
from sortCache import *
from getFileName import *

"""
{
    ARC_1T: {
        read: {
            time: xxxx,
            obj_cnt: xxx,   # 处理的对象数
            call_cnt: xxx,   # 读取的次数
            obj_error: {
                max_v: xxx,
            },
            call_error: {
                max_v: xxx,
            }
        },
        consume: {
            time: xxx,
            obj_cnt: xxx,
            call_cnt: xxx,
        },
        write: {
            time: xxx,
            obj_cnt: xxx,
            call_cnt: xxx,
        }
    },
    xxx
}
"""

def inc_num(cacheName, opeName, opeData):
    global dataDict
    dataDict[cacheName][opeName]['time'] += opeData[1]
    dataDict[cacheName][opeName]['obj_cnt'] += opeData[0]
    dataDict[cacheName][opeName]['call_cnt'] += 1
    if opeData[0] == 0:
        curObj = 0
    else:
        curObj = opeData[1] / opeData[0]
    curCall = opeData[1]

    dataDict[cacheName][opeName]['obj_error']['max_v'] = max(dataDict[cacheName][opeName]['obj_error']['max_v'], curObj)
    dataDict[cacheName][opeName]['call_error']['max_v'] = max(dataDict[cacheName][opeName]['call_error']['max_v'], curCall)



def outTable(oFile, cacheN, stageN, valueA):
    """
    -,read,consume,write,
    cache1,xx,xx,xx,
    cache2,xx,xx,xx,
    cache3,xx,xx,xx,
    """
    oFile.write('-,')
    oFile.write(','.join(stageN))
    oFile.write('\n')

    for i in range(len(cacheN)):
        oFile.write('%s,%s\n' % (cacheN[i], ','.join(valueA[i])))


# 总时间表
def outTotalTime(oFile, dataDict):
    cacheName = [x for x in dataDict.keys()]
    cacheName.sort(key=functools.cmp_to_key(sortCache))
    stageName = [x for x in dataDict[cacheName[0]].keys()]
    valueArr = []

    for i in range(len(cacheName)):
        valueArr.append([str(dataDict[cacheName[i]][sn]['time']) for sn in stageName])
    
    oFile.write('title:%s\n' % ('Total time'))
    outTable(oFile, cacheName, stageName, valueArr)

# 调用均值表
def outCallAverageTime(oFile, dataDict):
    cacheName = [x for x in dataDict.keys()]
    cacheName.sort(key=functools.cmp_to_key(sortCache))
    stageName = [x for x in dataDict[cacheName[0]].keys()]
    valueArr = []

    for i in range(len(cacheName)):
        valueArr.append([str(dataDict[cacheName[i]][sn]['time']/dataDict[cacheName[i]][sn]['call_cnt']) for sn in stageName])
    
    oFile.write('title:%s\n' % ('Avg call time'))
    outTable(oFile, cacheName, stageName, valueArr)

# 调用最大值表
def outCallMaxTime(oFile, dataDict):
    cacheName = [x for x in dataDict.keys()]
    cacheName.sort(key=functools.cmp_to_key(sortCache))
    stageName = [x for x in dataDict[cacheName[0]].keys()]
    valueArr = []

    for i in range(len(cacheName)):
        valueArr.append([str(dataDict[cacheName[i]][sn]['call_error']['max_v']) for sn in stageName])
    
    oFile.write('title:%s\n' % ('Max call time'))
    outTable(oFile, cacheName, stageName, valueArr)

# 对象均值表
def outObjAverageTime(oFile, dataDict):
    cacheName = [x for x in dataDict.keys()]
    cacheName.sort(key=functools.cmp_to_key(sortCache))
    stageName = [x for x in dataDict[cacheName[0]].keys()]
    valueArr = []

    for i in range(len(cacheName)):
        valueArr.append([str(dataDict[cacheName[i]][sn]['time']/dataDict[cacheName[i]][sn]['obj_cnt']) for sn in stageName])
    
    oFile.write('title:%s\n' % ('Avg obj time'))
    outTable(oFile, cacheName, stageName, valueArr)

# 对象最大值表
def outObjMaxTime(oFile, dataDict):
    cacheName = [x for x in dataDict.keys()]
    cacheName.sort(key=functools.cmp_to_key(sortCache))
    stageName = [x for x in dataDict[cacheName[0]].keys()]
    valueArr = []

    for i in range(len(cacheName)):
        valueArr.append([str(dataDict[cacheName[i]][sn]['obj_error']['max_v']) for sn in stageName])
    
    oFile.write('title:%s\n' % ('Max obj time'))
    outTable(oFile, cacheName, stageName, valueArr)

if __name__ == '__main__':
    dataDict = {}
    inFile = open(sys.argv[1], mode='r', encoding='UTF-8')

    while True:
        curLine = inFile.readline()
        if curLine == '':
            break

        if 'end' not in curLine or 'obtain' in curLine:
            continue

        curArr = curLine.strip('\n').split(' ')

        # print(curArr)

        curCache = curArr[1]
        curRead = [float(x) for x in curArr[4].split(',')]
        curConsume = [float(x) for x in curArr[5].split(',')]
        curWrite = [float(x) for x in curArr[6].split(',')]

        if curCache not in dataDict:
            dataDict[curCache] = {
                'read': {
                    'time': 0,
                    'obj_cnt': 0,
                    'call_cnt': 0,
                    'obj_error': {
                        'max_v': 0,
                    },
                    'call_error': {
                        'max_v': 0,
                    }
                },
                'consume': {
                    'time': 0,
                    'obj_cnt': 0,
                    'call_cnt': 0,
                    'obj_error': {
                        'max_v': 0,
                    },
                    'call_error': {
                        'max_v': 0,
                    }
                },
                'write': {
                    'time': 0,
                    'obj_cnt': 0,
                    'call_cnt': 0,
                    'obj_error': {
                        'max_v': 0,
                    },
                    'call_error': {
                        'max_v': 0,
                    }
                }
            }
        
        inc_num(curCache, 'read', curRead)
        inc_num(curCache, 'consume', curConsume)
        inc_num(curCache, 'write', curWrite)

    print(dataDict)

    outFile = open("%s.csv" % (getFileName(sys.argv[1])), mode='w', encoding='UTF-8')

    outTotalTime(outFile, dataDict)

    outCallAverageTime(outFile, dataDict)
    outCallMaxTime(outFile, dataDict)

    outObjAverageTime(outFile, dataDict)
    outObjMaxTime(outFile, dataDict)
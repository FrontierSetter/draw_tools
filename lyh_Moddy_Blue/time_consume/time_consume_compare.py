import sys, os
import matplotlib.pyplot as plt
import numpy as np
sys.path.append("..\\header")
from sortCache import *
from getFileName import *

def obtainFileData(inFilePath, dataDict):
    inFile = open(inFilePath, 'r', encoding='utf-8')
    curTitle = 'initTitle'
    colNameArr = []
    while True:
        curLine = inFile.readline()
        if curLine == '':
            break
        if 'title:' in curLine:
            # 处理表头
            curTitle = curLine.strip('\n').split(':')[1]
            if curTitle in dataDict:
                print("Wrong in %s, title %s duplicate" % (inFilePath, curTitle))

            dataDict[curTitle] = {}
            
            curLine = inFile.readline()
            colNameArr = curLine.strip('\n').split(',')[1:]
        else:
            # 处理表体
            curArr = curLine.strip('\n').split(',')
            curCache = curArr[0]
            # print(curArr)
            curDataArr = [float(x) for x in curArr[1:]]

            if len(curDataArr) != len(colNameArr):
                print("Wrong in %s-%s, cache %s lenth" % (inFilePath, curTitle, curCache))

            if curCache in dataDict[curTitle]:
                print("Wrong in %s-%s, cache %s duplicate" % (inFilePath, curTitle, curCache))
            
            dataDict[curTitle][curCache] = {}
            for i in range(len(curDataArr)):
                dataDict[curTitle][curCache][colNameArr[i]] = curDataArr[i]
    inFile.close()

def calculateDiffAbs(baseDict, newDict, resultDict):
    for curTitle in newDict.keys():
        resultDict[curTitle] = {}
        for curCache in newDict[curTitle].keys():
            resultDict[curTitle][curCache] = {}
            for curCol in newDict[curTitle][curCache].keys():
                curDiff = 'x'
                if (curTitle in baseDict) and (curCache in baseDict[curTitle]) and (curCol in baseDict[curTitle][curCache]):
                    curDiff = newDict[curTitle][curCache][curCol] - baseDict[curTitle][curCache][curCol]

                strDiff = ''
                if curDiff == 'x':
                    strDiff = curDiff
                elif curDiff > 0:
                    strDiff = ("+%.3f" % (curDiff))
                else:
                    strDiff = ("%.3f" % (curDiff))    
                
                resultDict[curTitle][curCache][curCol] = strDiff

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

def outputFileData(outFilePath, newDict, resultDict):
    outFile = open(outFilePath, 'w', encoding='utf-8')

    for curTitle in newDict.keys():
        cacheName = [x for x in newDict[curTitle].keys()]
        cacheName.sort(key=functools.cmp_to_key(sortCache))
        stageName = [x for x in newDict[curTitle][cacheName[0]].keys()]
        valueArr = []

        for cn in cacheName:
            valueArr.append([])
            for sn in stageName:
                strDiff = resultDict[curTitle][cn][sn]
                curNew = newDict[curTitle][cn][sn]
                valueArr[-1].append("%.3f(%s)" % (curNew, strDiff))
        
        outFile.write('title:%s\n' % (curTitle))
        outTable(outFile, cacheName, stageName, valueArr)

    outFile.close()

if __name__ == '__main__':
    baseFilePath = sys.argv[1]
    newFilePath = sys.argv[2]

    baseDataDict = {}
    newDataDict = {}

    obtainFileData(baseFilePath, baseDataDict)
    obtainFileData(newFilePath, newDataDict)
    # print(baseDataDict)
    # print(newDataDict)

    diffDict = {}
    calculateDiffAbs(baseDataDict, newDataDict, diffDict)
    # print(diffDict)

    outFilePath = "%s__to__%s.csv" % (os.path.splitext(os.path.split(baseFilePath)[1])[0], \
        os.path.splitext(os.path.split(newFilePath)[1])[0])
    outputFileData(outFilePath, newDataDict, diffDict)







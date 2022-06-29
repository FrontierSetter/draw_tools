import sys
from typing_extensions import runtime
import matplotlib.pyplot as plt
import numpy as np
import os
import functools
import argparse
sys.path.append("..\\header")
from sortCache import *
from timeStr import *

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
dataDict = {}

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

def drawBarStack(plt, cacheN, stageN, valueA, title):
    plt.grid(True, linestyle='-.', axis='y')

    bar_width = 0.6

    curBase = [0]*len(cacheN)
    for i in range(len(stageN)):
        plt.bar(range(len(cacheN)), valueA[i], bar_width, bottom=curBase, label=stageN[i])
        
        for j in range(len(valueA[i])):
            curBase[j] += valueA[i][j]

    plt.ylabel('Time (us)')

    plt.xticks(range(len(cacheN)), cacheN, rotation=-90)
    plt.title('%s_b%s_e%s_g%s_r%s' % (title, sToStr(begTime), sToStr(endTime), sToStr(gapTime), sToStr(runningTime-runningBaseTime)))

    plt.legend()

def drawBarGroup(plt, cacheN, stageN, valueA, errorA, title):
    plt.grid(True, linestyle='-.', axis='y')

    totalBarNum = len(stageN)
    bar_width = 0.8/1.1/totalBarNum
    gap = 0.1*bar_width
    ind = np.arange(len(cacheN))

    error_params=dict(elinewidth=1, capsize=1.5) #设置误差标记参数

    for i in range(len(stageN)):
        offset = 0.0-bar_width*(totalBarNum/2.0)-gap*((totalBarNum-1.0)/2)+(i+0.5)*bar_width+i*gap
        if errorA != None:
            # print(errorA[i])
            plt.bar(ind+offset, valueA[i], bar_width, label=stageN[i], yerr=errorA[i], error_kw=error_params)
        else:
            plt.bar(ind+offset, valueA[i], bar_width, label=stageN[i])

    plt.ylabel('Time (us)')

    plt.xticks(range(len(cacheN)), cacheN, rotation=-90)
    plt.title('%s_b%s_e%s_g%s_r%s' % (title, sToStr(begTime), sToStr(endTime), sToStr(gapTime), sToStr(runningTime-runningBaseTime)))

    plt.legend()


# 画总时间图
def drawTotalTimeStack(plt, dataDict):
    cacheName = [x for x in dataDict.keys()]
    cacheName.sort(key=functools.cmp_to_key(sortCache))
    stageName = [x for x in dataDict[cacheName[0]].keys()]
    valueArr = []

    for i in range(len(stageName)):
        valueArr.append([dataDict[cn][stageName[i]]['time'] for cn in cacheName])
    
    drawBarStack(plt, cacheName, stageName, valueArr, 'Total time')

def drawTotalTimeGroup(plt, dataDict):
    cacheName = [x for x in dataDict.keys()]
    cacheName.sort(key=functools.cmp_to_key(sortCache))
    stageName = [x for x in dataDict[cacheName[0]].keys()]
    valueArr = []

    for i in range(len(stageName)):
        valueArr.append([dataDict[cn][stageName[i]]['time'] for cn in cacheName])

    drawBarGroup(plt, cacheName, stageName, valueArr, None, 'Total time')

# 画调用均值图
def drawCallAverageTimeStack(plt, dataDict):
    cacheName = [x for x in dataDict.keys()]
    cacheName.sort(key=functools.cmp_to_key(sortCache))
    stageName = [x for x in dataDict[cacheName[0]].keys()]
    valueArr = []

    for i in range(len(stageName)):
        valueArr.append([dataDict[cn][stageName[i]]['time']/dataDict[cn][stageName[i]]['call_cnt'] for cn in cacheName])
    
    drawBarStack(plt, cacheName, stageName, valueArr, 'Avg call time')

def drawCallAverageTimeGroup(plt, dataDict):
    cacheName = [x for x in dataDict.keys()]
    cacheName.sort(key=functools.cmp_to_key(sortCache))
    stageName = [x for x in dataDict[cacheName[0]].keys()]

    valueArr = []
    errorArr = []
    for i in range(len(stageName)):
        valueArr.append([])
        errorArr.append([[],[]])
        for cn in cacheName:
            valueArr[-1].append(dataDict[cn][stageName[i]]['time']/dataDict[cn][stageName[i]]['call_cnt'])
            errorArr[-1][1].append(dataDict[cn][stageName[i]]['call_error']['max_v'] - valueArr[-1][-1])
            errorArr[-1][0].append(0)
    
    drawBarGroup(plt, cacheName, stageName, valueArr, errorArr, 'Avg call time')

# 画对象均值图
def drawObjAverageTimeStack(plt, dataDict):
    cacheName = [x for x in dataDict.keys()]
    cacheName.sort(key=functools.cmp_to_key(sortCache))
    stageName = [x for x in dataDict[cacheName[0]].keys()]
    valueArr = []

    for i in range(len(stageName)):
        valueArr.append([dataDict[cn][stageName[i]]['time']/dataDict[cn][stageName[i]]['obj_cnt'] for cn in cacheName])
    
    drawBarStack(plt, cacheName, stageName, valueArr, 'Avg obj time')
    # plt.ylim(0,7)

def drawObjAverageTimeGroup(plt, dataDict):
    cacheName = [x for x in dataDict.keys()]
    cacheName.sort(key=functools.cmp_to_key(sortCache))
    stageName = [x for x in dataDict[cacheName[0]].keys()]

    valueArr = []
    errorArr = []
    for i in range(len(stageName)):
        valueArr.append([])
        errorArr.append([[],[]])
        for cn in cacheName:
            valueArr[-1].append(dataDict[cn][stageName[i]]['time']/dataDict[cn][stageName[i]]['obj_cnt'])
            errorArr[-1][1].append(dataDict[cn][stageName[i]]['obj_error']['max_v'] - valueArr[-1][-1])
            errorArr[-1][0].append(0)

    drawBarGroup(plt, cacheName, stageName, valueArr, errorArr, 'Avg obj time')

    # plt.ylim(0,5)


# 主逻辑
parser = argparse.ArgumentParser(description='画性能图')
parser.add_argument('-f','--file', help='输入的log文件')
parser.add_argument('-b','--begin', default='0s', help='统计开始时间')
parser.add_argument('-e','--end', default='100000000s', help='统计结束时间')
parser.add_argument('-g','--gap', default='0s', help='统计持续时间')

args = parser.parse_args()
print(args)

targetFile = args.file
inFile = open(targetFile, mode='r', encoding='UTF-8')
(filepath, tempfilename) = os.path.split(targetFile)
(filename, extension) = os.path.splitext(tempfilename)

baseTime = 0
shouldStart = False
touchedRight = False
begTime = strToS(args.begin)
gapTime = strToS(args.gap)
endTime = strToS(args.end)
runningBaseTime = 0
runningTime = 0
if gapTime != 0:
    endTime = begTime + gapTime;
else:
    gapTime = endTime - begTime

while True:
    curLine = inFile.readline()
    if curLine == '':
        break

    if 'obtain_end' in curLine:
        curTime = int(curLine.split('_')[-2])
        if baseTime == 0:
            baseTime = curTime
        
        if curTime > endTime+baseTime:
            touchedRight = True
            break
        elif curTime > begTime+baseTime:
            shouldStart = True
        
    if (not shouldStart) or ('consume_end' not in curLine):
        continue

    curArr = curLine.strip('\n').split(' ')

    # print(curArr)
    runningTime = int(curArr[-1].split(',')[-1])
    if runningBaseTime == 0:
        runningBaseTime = runningTime

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

# print(dataDict)

fig = plt.figure(figsize=(18,12))

plt.subplot(321)
drawTotalTimeStack(plt, dataDict)
plt.subplot(322)
drawTotalTimeGroup(plt, dataDict)

plt.subplot(323)
drawCallAverageTimeStack(plt, dataDict)
plt.subplot(324)
drawCallAverageTimeGroup(plt, dataDict)

plt.subplot(325)
drawObjAverageTimeStack(plt, dataDict)
plt.subplot(326)
drawObjAverageTimeGroup(plt, dataDict)

plt.subplots_adjust(top=0.98,bottom=0.075,left=0.04,right=0.99,hspace=0.405,wspace=0.095)

if touchedRight:
    plt.savefig("%s_b%s_e%s_g%s_r%s.pdf" % (filename, sToStr(begTime), sToStr(endTime), sToStr(gapTime), sToStr(runningTime-runningBaseTime)))
else:
    plt.savefig("%s_not_b%s_e%s_g%s_r%s.pdf" % (filename, sToStr(begTime), sToStr(endTime), sToStr(gapTime), sToStr(runningTime-runningBaseTime)))
    
# plt.show()

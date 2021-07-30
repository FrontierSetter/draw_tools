import sys,os
import random

inFileName = sys.argv[1]
dataNumber = int(sys.argv[2])

cnt = 0
timeArr = []
fragArr = []

inFile = open(inFileName, 'r')
outFile = open('tmp.csv', 'w')

while True and cnt < dataNumber:
    curLine = inFile.readline()
    if curLine == '':
        break

    curArr = curLine.strip('\n').split(',')

    curTime = int(curArr[0])
    curFrag = float(curArr[1])

    timeArr.append(curTime)
    fragArr.append(curFrag)


    cnt += 1
    
for i in range(len(timeArr)):
    outFile.write('%d,%f\n' % (timeArr[-(i+1)], fragArr[-(i+1)]))

inFile.close()
outFile.close()
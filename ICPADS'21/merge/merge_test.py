import sys,os
import matplotlib.pyplot as plt
import numpy as np

infileNameArr = ['origin_24_threads_frag.csv', 'ibuddy_24_threads_frag.csv', 'spring_24_threads_frag.csv']
nameArr = ['std-Buddy', 'iBuddy', 'Spring-Buddy']

markerTable = {'iBuddy':'s', 'std-Buddy':'o', 'Spring-Buddy':'D'}
colorTable = {'iBuddy':'#C00000', 'std-Buddy':'#00B050', 'Spring-Buddy':'#1f497d'}

timeArr = []
fragArr = []

for infileName in infileNameArr:
    inFile = open(infileName, 'r')
    baseTime = -1
    timeArr.append([])
    fragArr.append([])

    while True:
        curLine = inFile.readline()
        if curLine == '':
            break

        curArr = curLine.strip('\n').split(',')

        curTime = int(curArr[0])
        curFrag = float(curArr[1])

        if baseTime < 0:
            baseTime = curTime
        
        timeArr[-1].append(len(timeArr[-1]))
        fragArr[-1].append(curFrag)
    
    inFile.close()

    # print(fragArr[-1][50:-50])
    print("%s, %f" % (infileName, sum(fragArr[-1][50:-100])/len(fragArr[-1][50:-100])))

plt.figure(figsize=(12,6))

for i in range(len(infileNameArr)):
    plt.plot(timeArr[i],fragArr[i], label=nameArr[i], linewidth=4, color=colorTable[nameArr[i]])

plt.legend(fontsize=20, loc="center left", bbox_to_anchor=(0.025, 0.65))
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.ylabel('Fragmentation Rate', fontsize=26)
plt.xlabel('Elapsed Time (s)', fontsize=26)
plt.subplots_adjust(left=0.1, right=0.99, top=0.99, bottom=0.125)

# plt.savefig('%s.pdf' % os.path.splitext(sys.argv[0])[0])

# plt.show()
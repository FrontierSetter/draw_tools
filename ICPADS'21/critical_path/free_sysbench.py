import sys,os
import matplotlib.pyplot as plt
import random

markerTable = {'iBuddy':'s', 'std-Buddy':'o', 'Spring-Buddy':'D'}
colorTable = {'iBuddy':'#C00000', 'std-Buddy':'#00B050', 'Spring-Buddy':'#1f497d'}


xArr = [1,2,4,8,12,16,20,24]
yDict = {
    "std-Buddy": [105, 148, 282, 414, 655, 1364, 2475, 3919],
    "iBuddy": [138, 182, 237, 314, 409, 526, 648, 792],
    "Spring-Buddy": [44, 43, 75, 85, 102, 110, 115, 125]
}

plt.figure(figsize=(9,6))

targetName = list(yDict.keys())

for i in range(len(targetName)):
    plt.plot(xArr,yDict[targetName[i]], label=targetName[i], linewidth=4, marker=markerTable[targetName[i]], color=colorTable[targetName[i]], markersize=12)

plt.legend(fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xticks(xArr,xArr,fontsize=20)
plt.ylabel('Request Latency (cycles)', fontsize=26)
plt.xlabel('Number of Threads', fontsize=26)
plt.subplots_adjust(left=0.13, right=0.99, top=0.99, bottom=0.12)

plt.savefig('%s.pdf' % os.path.splitext(sys.argv[0])[0])

plt.show()
import sys,os
import matplotlib.pyplot as plt
import random

markerTable = {'iBuddy':'s', 'std-Buddy':'o', 'Spring-Buddy':'D'}
colorTable = {'iBuddy':'#C00000', 'std-Buddy':'#00B050', 'Spring-Buddy':'#1f497d'}


xArr = [1,2,4,8,12,16,20,24]
yDict = {
    "std-Buddy": [225, 234, 315, 527, 985, 1103, 1564, 2177],
    "iBuddy": [213, 223, 357, 444, 699, 785, 1063, 1510],
    "Spring-Buddy": [208, 211, 283, 352, 502, 626, 722, 856]
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
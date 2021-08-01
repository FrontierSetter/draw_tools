import sys,os
import matplotlib.pyplot as plt
import random

markerTable = {'iBuddy':'s', 'std-Buddy':'o', 'Spring-Buddy':'D'}
colorTable = {'iBuddy':'#C00000', 'std-Buddy':'#00B050', 'Spring-Buddy':'#1f497d'}


xArr = [1,2,4,8,12,16,20,24]
yDict = {
    "std-Buddy": [195, 220, 387, 425, 671, 1359, 2578, 3716],
    "iBuddy": [144, 256, 352, 476, 562, 671, 842, 1342],
    "Spring-Buddy": [183, 195, 282, 300, 327, 368, 460, 505]
}

plt.figure(figsize=(9,6))

targetName = list(yDict.keys())

for i in range(len(targetName)):
    plt.plot(xArr, [num/1000.0 for num in yDict[targetName[i]]], label=targetName[i], linewidth=4, marker=markerTable[targetName[i]], color=colorTable[targetName[i]], markersize=12)

plt.legend(fontsize=22)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.xticks(xArr,xArr,fontsize=22)
plt.ylabel('Request Latency (cycles)', fontsize=28)
plt.xlabel('Number of Threads', fontsize=28)

xmin, xmax, ymin, ymax = plt.axis()
plt.text(xmin, ymax*1.005, r'$\times10^{%d}$'%(3),fontsize=20,ha='left')

plt.subplots_adjust(left=0.135, right=0.99, top=0.95, bottom=0.128)

plt.savefig('%s.pdf' % os.path.splitext(sys.argv[0])[0])

plt.show()
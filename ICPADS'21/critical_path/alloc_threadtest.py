import sys, os
import matplotlib.pyplot as plt
import random

markerTable = {'iBuddy':'s', 'std-Buddy':'o', 'Spring-Buddy':'D'}
colorTable = {'iBuddy':'#C00000', 'std-Buddy':'#00B050', 'Spring-Buddy':'#1f497d'}


xArr = [1,2,4,8,12,16,20,24]
yDict = {
    "std-Buddy": [170, 213, 259, 388, 631, 1345, 2798, 4886],
    "iBuddy": [161, 277, 330, 467, 656, 742, 840, 986],
    "Spring-Buddy": [168, 210, 257, 282, 309, 405, 486, 555]
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
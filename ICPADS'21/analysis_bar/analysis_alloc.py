import sys,os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

colorDict = {'iBuddy': '#C00000', 'std-Buddy': '#00B050', 'Spring-Buddy (with fixlazy)': '#F79646', 'Spring-Buddy': '#1f497d', 'Improvement by spring core layer':'#4BACC6', 'Improvement by spring lazy layer':'#4BACC6'}
hatchDict = {'iBuddy': 'xxx', 'std-Buddy': '\\\\\\', 'Spring-Buddy (with fixlazy)': '///', 'Spring-Buddy': '---', 'Improvement by spring core layer':'..', 'Improvement by spring lazy layer':''}

tickArr = ['Ramspeed', 'Stream', 'Linux\nScalability', 'Threadtest', 'Sysbench', 'Average']

yDict = {
    "std-Buddy": [1425, 4886, 1293, 2177, 3716],
    "iBuddy": [652, 840, 740, 1510, 842],
    "Spring-Buddy": [523, 555, 539, 856, 505],
    "fixlazy-Buddy": [571, 670, 695, 1247, 820],
}

stdArr = []
iBuddyArr = []
springArr = []
coreArr = []
lazyArr = []

for i in range(5):
    stdArr.append(float(yDict["std-Buddy"][i])/yDict["std-Buddy"][i])
    iBuddyArr.append(float(yDict["iBuddy"][i])/yDict["std-Buddy"][i])
    springArr.append(float(yDict["Spring-Buddy"][i])/yDict["std-Buddy"][i])

    coreArr.append(float(yDict["std-Buddy"][i]-yDict["fixlazy-Buddy"][i])/yDict["std-Buddy"][i])
    lazyArr.append(float(yDict["fixlazy-Buddy"][i]-yDict["Spring-Buddy"][i])/yDict["std-Buddy"][i])

labelArr = ['iBuddy', 'std-Buddy', 'Spring-Buddy']
allArr = [iBuddyArr, stdArr, springArr]

for l in allArr:
    l.append(sum(l)/len(l))

padLabelArr = ['Improvement by spring core layer', 'Improvement by spring lazy layer']
padArr = [coreArr, lazyArr]

for l in padArr:
    l.append(sum(l)/len(l))

ind=np.arange(len(tickArr))
bar_width = 0.18
gap_width = 0.04
totalBarNum = len(allArr)

plt.figure(figsize=(9,6))

barCnt = 0
for barId in range(totalBarNum):
    offset = 0.0-bar_width*(totalBarNum/2.0)-gap_width*((totalBarNum-1.0)/2)+(barCnt+0.5)*bar_width+barCnt*gap_width
    curP = plt.bar(ind+offset, allArr[barId], bar_width, label=labelArr[barId],color='white', \
        edgecolor=colorDict[labelArr[barId]], hatch=hatchDict[labelArr[barId]], lw=3)
    barCnt += 1

barCnt -= 1
curBase = springArr
for barId in range(len(padLabelArr)):
    offset = 0.0-bar_width*(totalBarNum/2.0)-gap_width*((totalBarNum-1.0)/2)+(barCnt+0.5)*bar_width+barCnt*gap_width
    plt.bar(ind+offset, padArr[barId], bar_width, label=padLabelArr[barId],color='white', \
            edgecolor=colorDict[padLabelArr[barId]], hatch=hatchDict[padLabelArr[barId]], lw=3, bottom=curBase, linestyle='--', alpha = 0.6)
    
    for i in range(len(curBase)):
        curBase[i] += padArr[barId][i]


plt.ylabel('Normalized Latency', fontsize=24)
plt.yticks(fontsize=20)
# plt.ylim(0,1.25)

# xfmt = ScalarFormatter(useMathText=True)
# xfmt.set_powerlimits((0, 0))
# plt.gca().yaxis.set_major_formatter(xfmt)

# plt.text(-0.5, 1.25, r'$\times10^{-2}$',fontsize=20)

plt.xticks(ind,tickArr, fontsize=18, rotation=360-5)
# plt.xlabel('Main Memory Capacity(GB)', fontsize=26)

plt.subplots_adjust(left=0.1, right=0.99, top=0.78, bottom=0.12)

# plt.legend(fontsize=18, ncol = 2, loc='upper center', columnspacing=0.6, handletextpad=0.3, bbox_to_anchor=(0.455, 1.15))
plt.legend(fontsize=18, ncol=2, columnspacing=1, loc='upper center', bbox_to_anchor=(0.5, 1.34))

plt.savefig('%s.pdf' % os.path.splitext(sys.argv[0])[0])
plt.show()
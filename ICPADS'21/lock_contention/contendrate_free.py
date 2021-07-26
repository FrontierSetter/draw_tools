import sys,os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

colorDict = {'iBuddy': '#C00000', 'std-Buddy': '#00B050', 'Spring-Buddy (with fixlazy)': '#F79646', 'Spring-Buddy': '#1f497d'}
hatchDict = {'iBuddy': 'xxx', 'std-Buddy': '\\\\\\', 'Spring-Buddy (with fixlazy)': '///', 'Spring-Buddy': '---'}

oriData = [
    {
        'name': 'Ramspeed',
        'Spring-Buddy': [6053, 17],
        'std-Buddy': [1096601, 1904154],
        'Spring-Buddy (with fixlazy)': [5494106, 308220],
        'iBuddy': [1591629, 471912],
    },
    {
        'name': 'Stream',
        'Spring-Buddy': [1250, 16],
        'std-Buddy': [360657, 313272],
        'Spring-Buddy (with fixlazy)': [1151230, 22086],
        'iBuddy': [161704, 20911],
    },
    {
        'name': 'Linux Scalability',
        'Spring-Buddy': [3327, 11],
        'std-Buddy': [1648350, 2921731],
        'Spring-Buddy (with fixlazy)': [8579547, 661129],
        'iBuddy': [8643228, 1474087],
    },
    {
        'name': 'Threadtest',
        'Spring-Buddy': [73774, 1336],
        'std-Buddy': [62975, 8706701],
        'Spring-Buddy (with fixlazy)': [12278537, 2231673],
        'iBuddy': [1441682, 1138373],
    },
    {
        'name': 'Sysbench',
        'Spring-Buddy': [1731, 23],
        'std-Buddy': [799205, 6059887],
        'Spring-Buddy (with fixlazy)': [9428394, 1418871],
        'iBuddy': [1001349, 1898615],
    }
]

sBArr = []
iBArr = []
stdBArr = []
sBfixArr = []
tickArr = []

for dataDict in oriData:
    tickArr.append(dataDict['name'])
    curSBHit = dataDict['Spring-Buddy'][0]
    curSBMiss = dataDict['Spring-Buddy'][1]
    curStdBHit = dataDict['std-Buddy'][0]
    curStdBMiss = dataDict['std-Buddy'][1]
    cursBfixHit = dataDict['Spring-Buddy (with fixlazy)'][0]
    cursBfixMiss = dataDict['Spring-Buddy (with fixlazy)'][1]
    curiBHit = dataDict['iBuddy'][0]
    curiBMiss = dataDict['iBuddy'][1]
    sBArr.append((1-float(curSBHit)/(curSBHit+curSBMiss))*100)
    iBArr.append((1-float(curiBHit)/(curiBHit+curiBMiss))*100)
    stdBArr.append((1-float(curStdBHit)/(curStdBHit+curStdBMiss))*100)
    sBfixArr.append((1-float(cursBfixHit)/(cursBfixHit+cursBfixMiss))*100)

labelArr = ['std-Buddy', 'iBuddy', 'Spring-Buddy (with fixlazy)', 'Spring-Buddy']
allArr = [stdBArr, iBArr, sBfixArr, sBArr]

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

plt.ylabel('Core Layer Contention Rate (%)', fontsize=24)
plt.yticks(fontsize=20)
# plt.ylim(0,1.25)

# xfmt = ScalarFormatter(useMathText=True)
# xfmt.set_powerlimits((0, 0))
# plt.gca().yaxis.set_major_formatter(xfmt)

# plt.text(-0.5, 1.25, r'$\times10^{-2}$',fontsize=20)

plt.xticks(ind,tickArr, fontsize=18, rotation=360-10)
# plt.xlabel('Main Memory Capacity(GB)', fontsize=26)

plt.subplots_adjust(left=0.115, right=0.99, top=0.99, bottom=0.11)

# plt.legend(fontsize=18, ncol = 2, loc='upper center', columnspacing=0.6, handletextpad=0.3, bbox_to_anchor=(0.455, 1.15))
plt.legend(fontsize=18)

plt.savefig('%s.pdf' % os.path.splitext(sys.argv[0])[0])
plt.show()
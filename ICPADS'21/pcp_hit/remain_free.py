import sys,os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

colorDict = {'fixlazy-186': '#C00000', 'fixlazy-372': '#00B050', 'fixlazy-744': '#F79646', 'spring-lazy': '#1f497d'}
hatchDict = {'fixlazy-186': 'xxx', 'fixlazy-372': '\\\\\\', 'fixlazy-744': '///', 'spring-lazy': '---'}

oriData = [
    {
        'name': 'Ramspeed',
        'fixlazy-186': 110.77,
        'fixlazy-372': 206.85,
        'fixlazy-744': 377.96,
        'spring-lazy': 65.93,
    },
    {
        'name': 'Stream',
        'fixlazy-186': 79.02,
        'fixlazy-372': 136.86,
        'fixlazy-744': 211.91,
        'spring-lazy': 202.9,
    },
    {
        'name': 'Linux Scalability',
        'fixlazy-186': 89.93,
        'fixlazy-372': 136.86,
        'fixlazy-744': 355.22,
        'spring-lazy': 67.54,
    },
    {
        'name': 'Threadtest',
        'fixlazy-186': 135.48,
        'fixlazy-372': 175.69,
        'fixlazy-744': 536.25,
        'spring-lazy': 142.21,
    },
    {
        'name': 'Sysbench',
        'fixlazy-186': 86.91,
        'fixlazy-372': 159.71,
        'fixlazy-744': 348.12,
        'spring-lazy': 241.09,
    }
]

fix186Arr = []
fix372Arr = []
fix744Arr = []
springArr = []
tickArr = []

for dataDict in oriData:
    tickArr.append(dataDict['name'])
    curFix186Remain = dataDict['fixlazy-186']
    curFix372Remain = dataDict['fixlazy-372']
    curFix744Remain = dataDict['fixlazy-744']
    curSpringRemain = dataDict['spring-lazy']
    fix186Arr.append(curFix186Remain)
    fix372Arr.append(curFix372Remain)
    fix744Arr.append(curFix744Remain)
    springArr.append(curSpringRemain)

labelArr = ['fixlazy-186', 'fixlazy-372', 'fixlazy-744', 'spring-lazy']
allArr = [fix186Arr, fix372Arr, fix744Arr, springArr]

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

plt.ylabel('Lazy Buffer Residual Pages', fontsize=26)
plt.yticks(fontsize=20)
# plt.ylim(0,1.25)

# xfmt = ScalarFormatter(useMathText=True)
# xfmt.set_powerlimits((0, 0))
# plt.gca().yaxis.set_major_formatter(xfmt)

# plt.text(-0.5, 1.25, r'$\times10^{-2}$',fontsize=20)

plt.xticks(ind,tickArr, fontsize=20, rotation=360-13)
# plt.xlabel('Main Memory Capacity(GB)', fontsize=26)

plt.subplots_adjust(left=0.115, right=0.99, top=0.90, bottom=0.14)

plt.legend(fontsize=21, ncol = 4, loc='upper center', columnspacing=0.5, handletextpad=0.15, bbox_to_anchor=(0.453, 1.15), handlelength=1.3)

plt.savefig('%s.pdf' % os.path.splitext(sys.argv[0])[0])
plt.show()
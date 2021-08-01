import sys,os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

colorDict = {'fixlazy-186': '#C00000', 'fixlazy-372': '#00B050', 'fixlazy-744': '#F79646', 'spring-lazy': '#1f497d'}
hatchDict = {'fixlazy-186': 'xxx', 'fixlazy-372': '\\\\\\', 'fixlazy-744': '///', 'spring-lazy': '---'}

oriData = [
    {
        'name': 'Ramspeed',
        "fixlazy-186": [95571476, 98645963],
        "fixlazy-372": [95339244, 96359888],
        "fixlazy-744": [95155060, 96137220],
        "spring-lazy": [94869775, 94965814],
    },
    {
        'name': 'Stream',
        "fixlazy-186": [28639611, 29561600],
        "fixlazy-372": [29144115, 29456761],
        "fixlazy-744": [28142114, 28434292],
        "spring-lazy": [27879852, 27906624],
    },
    {
        'name': 'Linux Scalability',
        "fixlazy-186": [135008874, 139356612],
        "fixlazy-372": [29144115, 29456761],
        "fixlazy-744": [135190055, 136592220],
        "spring-lazy": [135710575, 136245656],
    },
    {
        'name': 'Threadtest',
        "fixlazy-186": [296154859, 305620595],
        "fixlazy-372": [313328015, 316643382],
        "fixlazy-744": [307543236, 310638796],
        "spring-lazy": [372837465, 376269435],
    },
    {
        'name': 'Sysbench',
        "fixlazy-186": [222853631, 230038141],
        "fixlazy-372": [231304073, 233789331],
        "fixlazy-744": [229152924, 231536829],
        "spring-lazy": [264822558, 265092580],
    }
]

fix186Arr = []
fix372Arr = []
fix744Arr = []
springArr = []
tickArr = []

for dataDict in oriData:
    tickArr.append(dataDict['name'])
    curFix186Hit = dataDict['fixlazy-186'][0]
    curFix186All = dataDict['fixlazy-186'][1]
    curFix372Hit = dataDict['fixlazy-372'][0]
    curFix372All = dataDict['fixlazy-372'][1]
    curFix744Hit = dataDict['fixlazy-744'][0]
    curFix744All = dataDict['fixlazy-744'][1]
    curSpringHit = dataDict['spring-lazy'][0]
    curSpringAll = dataDict['spring-lazy'][1]
    fix186Arr.append((1-float(curFix186Hit)/curFix186All)*100)
    fix372Arr.append((1-float(curFix372Hit)/curFix372All)*100)
    fix744Arr.append((1-float(curFix744Hit)/curFix744All)*100)
    springArr.append((1-float(curSpringHit)/curSpringAll)*100)

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

plt.ylabel('Lazy Layer Miss Rate (%)', fontsize=26)
plt.yticks(fontsize=20)
# plt.ylim(0,1.25)

# xfmt = ScalarFormatter(useMathText=True)
# xfmt.set_powerlimits((0, 0))
# plt.gca().yaxis.set_major_formatter(xfmt)

# plt.text(-0.5, 1.25, r'$\times10^{-2}$',fontsize=20)

plt.xticks(ind,tickArr, fontsize=20, rotation=360-13)
# plt.xlabel('Main Memory Capacity(GB)', fontsize=26)

plt.subplots_adjust(left=0.105, right=0.99, top=0.90, bottom=0.14)

plt.legend(fontsize=21, ncol=4, loc='upper center', columnspacing=0.5, handletextpad=0.15, bbox_to_anchor=(0.455, 1.15), handlelength=1.3)

plt.savefig('%s.pdf' % os.path.splitext(sys.argv[0])[0])
plt.show()
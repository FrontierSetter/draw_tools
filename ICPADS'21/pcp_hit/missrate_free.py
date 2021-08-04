import sys,os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

colorDict = {'fixlazy-186': '#C00000', 'fixlazy-372': '#00B050', 'fixlazy-744': '#F79646', 'spring-lazy': '#1f497d'}
hatchDict = {'fixlazy-186': 'xxx', 'fixlazy-372': '\\\\\\', 'fixlazy-744': '///', 'spring-lazy': '---'}

oriData = [
    {
        'name': 'Ramspeed',
        "fixlazy-186": [93956863, 96979336],
        "fixlazy-372": [93515422, 94516471],
        "fixlazy-744": [93517424, 94482654],
        "spring-lazy": [93387294, 93390365],
    },
    {
        'name': 'Stream',
        "fixlazy-186": [19865846, 20504812],
        "fixlazy-372": [20745725, 20968066],
        "fixlazy-744": [20306286, 20516849],
        "spring-lazy": [19426407, 19427010],
    },
    {
        'name': 'Linux Scalability',
        "fixlazy-186": [133843710, 138153966],
        "fixlazy-372": [20745725, 20968066],
        "fixlazy-744": [133891758, 135280516],
        "spring-lazy": [134472338, 134474103],
    },
    {
        'name': 'Threadtest',
        "fixlazy-186": [295930635, 305389199],
        "fixlazy-372": [134052919, 135490902],
        "fixlazy-744": [307311004, 310404242],
        "spring-lazy": [372570198, 372607588],
    },
    {
        'name': 'Sysbench',
        "fixlazy-186": [216364148, 223339488],
        "fixlazy-372": [237988751, 240545840],
        "fixlazy-744": [222188967, 224500475],
        "spring-lazy": [257591334, 257592161],
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

plt.ylabel('Lazy Buffer Miss Rate (%)', fontsize=26)
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
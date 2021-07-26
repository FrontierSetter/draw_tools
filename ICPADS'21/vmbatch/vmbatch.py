import sys,os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

colorDict = {'Allocation': '#C00000', 'Deallocation': '#1f497d'}
hatchDict = {'Allocation': 'xxx', 'Deallocation': '---'}

allocArr = [2265.03, 1220.11, 2500.36, 6242.04, 4835.61]
freeArr = [16929.51, 9759.3, 10010.51, 74248.67, 68491.47]
tickArr = ['Ramspeed', 'Stream', 'Linux Scalability', 'Threadtest', 'Sysbench']

labelArr = ['Allocation', 'Deallocation']
allArr = [allocArr, freeArr]

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

plt.ylabel('Average Number of Consecutive Requests', fontsize=26)
plt.yticks(fontsize=20)
# plt.ylim(0,1.25)

# xfmt = ScalarFormatter(useMathText=True)
# xfmt.set_powerlimits((0, 0))
# plt.gca().yaxis.set_major_formatter(xfmt)

# plt.text(-0.5, 1.25, r'$\times10^{-2}$',fontsize=20)

plt.xticks(ind,tickArr, fontsize=18, rotation=360-10)
# plt.xlabel('Main Memory Capacity(GB)', fontsize=26)

plt.subplots_adjust(left=0.105, right=0.99, top=0.90, bottom=0.11)

# plt.legend(fontsize=18, ncol = 4, loc='upper center', columnspacing=1, handletextpad=0.3, bbox_to_anchor=(0.455, 1.15))
plt.legend(fontsize=18)

plt.savefig('%s.pdf' % os.path.splitext(sys.argv[0])[0])
plt.show()
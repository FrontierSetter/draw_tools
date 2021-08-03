import os, sys
import matplotlib.pyplot as plt
import numpy as np
import xlrd
from matplotlib.ticker import ScalarFormatter

# # processNum = [4, 8, 12, 16, 20, 24]
# processNum = [1, 4, 8, 12, 16, 20]

# # allocTime = [1869.3, 3641.9, 6296.6, 6944.1, 7436.8, 8056.8]
# # allocTime = [4520897024, 8833510400, 15213447168, 17626060800, 18694342656, 20484042752]
# allocTime = [3805849344, 4529754624, 10437569536, 12913256448, 15990241280, 18714742784]

# # freeTime = [223.4, 612.5, 838.4, 1224.2, 2208.1, 2966.9]
# # freeTime = [527221824, 1391155456, 1857217792, 3016021248, 4790685936, 6246812672]
# freeTime = [347048480, 527221824, 1829782144, 4300934144, 5267849216, 7209771008]

# # allocLockPercent = [0.37, 1.40, 7.96, 13.31, 20.79, 30.73]
# allocLockPercent = [0.03, 0.48, 4.57, 16.27, 24.15, 38.62]

# # freeLockPercent = [0.48, 1.66, 19.03, 25.97, 26.91, 29.74]
# freeLockPercent = [0.02, 0.47, 3.72, 9.22, 20.04, 22.87]

# # clearPercent = [39.94, 36.48, 32.01, 25.56, 20.17, 14.07]
# clearPercent = [27.47, 27.15, 30.24, 27.2, 17.62, 11.48]

processNum = []

archInteruptPercent = []
allocClearPercent = []
allocBuddyPercent = []
allocManagePercent = []
allocLockPercent = []
freeBuddyPercent = []
freeManagerPercent = []
freeLockPercent = []

allocTime = []
freeTime = []

colorDict = {
    'architecture overhead': '#00B050',
    'allocation': '#1f497d',
    'waiting (allocation)': '#C00000',
    'waiting (deallocation)': '#F79646',
    'deallocation': '#4BACC6',
}

colors = ['#00B050', '#1f497d', '#C00000']

hatchDict = {
    'architecture overhead': '....',
    'allocation': '----',
    'waiting (allocation)': '////',
    'waiting (deallocation)': '\\\\\\\\',
    'deallocation': '||||',
}

hatchs = ['....', '++++', 'xxxx']

readbook = xlrd.open_workbook('mem_contention_final.xlsx')
curSheet = readbook.sheet_by_name('m4-稠密')
nrows = curSheet.nrows

for i in range(2, nrows):
    # print(i)
    curRow = curSheet.row_values(i)
    # print(curRow)

    processNum.append("%d" % (curRow[0]))

    archInteruptPercent.append(curRow[6])

    allocClearPercent.append(curRow[12])
    allocBuddyPercent.append(curRow[15])
    allocManagePercent.append(curRow[17])
    allocLockPercent.append(curRow[19])

    freeBuddyPercent.append(curRow[23])
    freeManagerPercent.append(curRow[25])
    freeLockPercent.append(curRow[27])

    allocTime.append(curRow[34])
    freeTime.append(curRow[35])




totalMemTime = []

archInteruptTime = []

allocClearTime = []
allocBuddyTime = []
allocManageTime = []
allocLockTime = []
allocUseful = []

freeBuddyTime = []
freeManagerTime = []
freeLockTime = []
freeUseful = []

archOverheadTime = []
usefulWorkTime = []
lockTime = []

scalNum = 1000

for i in range(len(allocTime)):
    totalMemTime.append((allocTime[i]+freeTime[i])/(1024*1024*5*scalNum))

    archInteruptTime.append(totalMemTime[i]*archInteruptPercent[i]/100.0)

    allocClearTime.append(totalMemTime[i]*allocClearPercent[i]/100.0)
    allocBuddyTime.append(totalMemTime[i]*allocBuddyPercent[i]/100.0)
    allocManageTime.append(totalMemTime[i]*allocManagePercent[i]/100.0)

    allocUseful.append(0.0)
    allocUseful[-1] += allocClearTime[-1]
    allocUseful[-1] += allocBuddyTime[-1]
    allocUseful[-1] += allocManageTime[-1]

    allocLockTime.append(totalMemTime[i]*allocLockPercent[i]/100.0)

    freeBuddyTime.append(totalMemTime[i]*freeBuddyPercent[i]/100.0)
    freeManagerTime.append(totalMemTime[i]*freeManagerPercent[i]/100.0)

    freeUseful.append(0.0)
    freeUseful[-1] += freeBuddyTime[-1]
    freeUseful[-1] += freeManagerTime[-1]

    freeLockTime.append(totalMemTime[i]*freeLockPercent[i]/100.0)

    # 背景图
    archOverheadTime.append(archInteruptTime[-1])
    usefulWorkTime.append(allocUseful[-1]+freeUseful[-1])
    lockTime.append(allocLockTime[-1]+freeLockTime[-1])

ind = np.arange(len(allocLockTime))
ind_more = np.arange(len(allocLockTime)+1)
curBase = [0]*len(allocLockTime)

plt.figure(figsize=(11,6))

bar_width = 0.5


def draw_bar(barArr, labelName):
    global curBase
    plt.bar(ind, barArr, bar_width, label=labelName, edgecolor=colorDict[labelName], bottom=curBase, hatch=hatchDict[labelName], color='white', lw=3)
    for i in range(len(curBase)):
        curBase[i] += barArr[i]


stacks = plt.stackplot(ind,archOverheadTime,usefulWorkTime,lockTime,colors=colors,alpha=0.2)
# for stack, hatch in zip(stacks, hatchs):
#     stack.set_hatch(hatch)

# for stack, color in zip(stacks, colors):
#     stack.set_edgecolor(color)


draw_bar(archInteruptTime, 'architecture overhead')
draw_bar(allocUseful, 'allocation')
draw_bar(freeUseful, 'deallocation')
draw_bar(allocLockTime, 'waiting (allocation)')
draw_bar(freeLockTime, 'waiting (deallocation)')

# plt.plot(ind,archOverheadTime,color='black')
# plt.plot(ind,[archOverheadTime[i]+usefulWorkTime[i] for i in range(len(archOverheadTime))], color='black')
# plt.plot(ind,[archOverheadTime[i]+usefulWorkTime[i]+lockTime[i] for i in range(len(archOverheadTime))], color='black')


# plt.bar(range(len(curBase)+2), [0]*(len(curBase)+2), bar_width, color='white', lw=1)

xfmt = ScalarFormatter(useMathText=True)
xfmt.set_powerlimits((0, 0))
plt.gca().yaxis.set_major_formatter(xfmt)

plt.ylabel('Request Latency (cycles)', fontsize=26)
plt.xlabel('Number of Threads', fontsize=26)
plt.subplots_adjust(left=0.08, right=0.8, top=0.95, bottom=0.12)

plt.legend(fontsize=20, handletextpad=0.3, handlelength=1)
plt.yticks(fontsize=20)
plt.xticks(ind, processNum, fontsize=20)

xmin, xmax, ymin, ymax = plt.axis()
plt.text(xmin, ymax*1.005, r'$\times10^{%d}$'%(3),fontsize=20,ha='left')

plt.savefig('%s.pdf' % os.path.splitext(sys.argv[0])[0])

plt.show()
from os import curdir
import xlrd
import matplotlib.pyplot as plt
import numpy as np

colorDict = {
    'angle x': '#C00000', 
    'angle y': '#00B050', 
    'angle z': '#1f497d', 
}

markerDict = {
    'angle x': 'D', 
    'angle y': 'o', 
    'angle z': '^', 
}

lsDict = {
    'angle x': 'solid', 
    'angle y': 'dashed', 
    'angle z': 'dashdot', 
}

nameArr = [
    'angle x', 
    'angle y', 
    'angle z', 
]


inFile = open('angle.txt', 'r')
dataArr = [[],[],[]]

while True:
    curLine = inFile.readline()
    if curLine == '':
        break
    curArr = curLine.strip('\n').split(' ')

    for i in range(3):
        curData = int(curArr[i]) / 32768 * 180
        if curData > 180:
            curData = curData-360
        dataArr[i].append(curData)


plt.figure(figsize=(9,6))
line_lw = 3

for i in range(3):
    # print(dataArr[i])
    # print(nameArr[i])
    plt.plot(range(len(dataArr[i])), dataArr[i], linewidth=line_lw, label=nameArr[i], \
        color=colorDict[nameArr[i]], markersize=10, zorder=5, markevery=int(len(dataArr[i])/40))

    # 修改线型之后不好看
    # plt.plot(range(len(dataArr[i])), dataArr[i], linewidth=line_lw, label=nameArr[i], \
    #     color=colorDict[nameArr[i]], linestyle=lsDict[nameArr[i]], markersize=10, zorder=5, markevery=int(len(dataArr[i])/40))
    
    # marker加上之后不好看
    # plt.plot(range(len(dataArr[i])), dataArr[i], linewidth=line_lw, label=nameArr[i], \
    #     color=colorDict[nameArr[i]], marker=markerDict[nameArr[i]], markersize=10, zorder=5, markevery=int(len(dataArr[i])/40))

# plt.ylabel(yLabel, fontsize=28)
# plt.xlabel(xLabel, fontsize=28)

plt.ylabel("degree", fontsize=28)
plt.xlabel("time sequence", fontsize=28)

plt.legend(fontsize=22, ncol=3, columnspacing=0.6, labelspacing=0.2, loc='upper center')
plt.yticks(fontsize=22)
plt.xticks(fontsize=22)

# plt.ylim(0)
plt.xlim(0, len(dataArr[0]))
plt.grid(True, linestyle='-.', axis='both')

plt.subplots_adjust(left=0.15, right=0.97, top=0.99, bottom=0.14)

plt.savefig('angle.pdf')
plt.show()

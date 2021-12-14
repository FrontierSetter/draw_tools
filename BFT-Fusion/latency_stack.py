import xlrd
import matplotlib.pyplot as plt
import numpy as np

colorDict = {
    'network': '#00B050', 
    'computation': '#1f497d', 
    'I/O': '#C00000', 
}

hatchDict = {
    'network': '\\\\\\\\',
    'computation': '----',
    'I/O': '////',
}

readbook = xlrd.open_workbook('latency(2)(2).xlsx')
dataSheet = readbook.sheet_by_name('Sheet2')

nrows = dataSheet.nrows

dataDict = {}

stageArr = [i for i in dataSheet.row_values(0) if i != '']
methodArr = []

for curStage in stageArr:
    dataDict[curStage] = []

for i in range(1, nrows):
    curRow = dataSheet.row_values(i)
    methodArr.append(curRow[0])
    for j in range(len(stageArr)):
        dataDict[stageArr[j]].append(curRow[j+1])

print(dataDict)

ind = np.arange(len(methodArr))
bar_lw = 3
bar_width = 0.5
legendArr = []
legendEntryArr = []

plt.figure(figsize=(9,6))

curBase = [0]*len(methodArr)
plt.grid(True, linestyle='-.', axis='y')

for i in range(len(stageArr)):
    curP = plt.bar(ind, dataDict[stageArr[i]], bar_width, label=stageArr[i], bottom=curBase, \
        hatch=hatchDict[stageArr[i]], edgecolor=colorDict[stageArr[i]], color='white', lw=bar_lw, zorder=5)
    legendArr.insert(0,curP)
    legendEntryArr.insert(0,stageArr[i])
    for j in range(len(curBase)):
        curBase[j] += dataDict[stageArr[i]][j]

plt.ylabel('Overhead(ms)', fontsize=26)
# plt.xlabel('Number of Threads', fontsize=26)

plt.legend(legendArr, legendEntryArr, fontsize=24)
plt.yticks(fontsize=22)
plt.xticks(ind, methodArr, fontsize=22, rotation=-10)


plt.subplots_adjust(left=0.1, right=0.995, top=0.99, bottom=0.13)

plt.savefig('latency_stack.pdf')
# plt.show()

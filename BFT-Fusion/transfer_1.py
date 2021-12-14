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
dataSheet = readbook.sheet_by_name('transfer')

startRow = 0
finalRow = 5

dataDict = {}

stageArr = [i for i in dataSheet.row_values(startRow) if i != ''][1:-1]
xArr = []
xLabel = dataSheet.row_values(startRow)[0].split(',')[0].split(':')[1]
yLabel = dataSheet.row_values(startRow)[0].split(',')[1].split(':')[1]

for curStage in stageArr:
    dataDict[curStage] = []

for i in range(startRow+1, finalRow+1):
    curRow = dataSheet.row_values(i)
    xArr.append(curRow[1])
    for j in range(len(stageArr)):
        dataDict[stageArr[j]].append(curRow[j+2])

print(dataDict)

ind = np.arange(len(xArr))
bar_lw = 3
bar_width = 0.5
legendArr = []
legendEntryArr = []

plt.figure(figsize=(9,6))

curBase = [0]*len(xArr)
plt.grid(True, linestyle='-.', axis='y')

for i in range(len(stageArr)):
    curP = plt.bar(ind, dataDict[stageArr[i]], bar_width, label=stageArr[i], bottom=curBase, \
        hatch=hatchDict[stageArr[i]], edgecolor=colorDict[stageArr[i]], color='white', lw=bar_lw, zorder=5)
    legendArr.insert(0,curP)
    legendEntryArr.insert(0,stageArr[i])
    for j in range(len(curBase)):
        curBase[j] += dataDict[stageArr[i]][j]

plt.ylabel(yLabel, fontsize=26)
plt.xlabel(xLabel, fontsize=26)

plt.legend(legendArr, legendEntryArr, fontsize=24, ncol=3, \
    columnspacing=1, labelspacing=0.2, loc='upper center', bbox_to_anchor=(0.5, 1.176))
plt.yticks(fontsize=22)
plt.xticks(ind, [str(int(i)) for i in xArr], fontsize=22)


plt.subplots_adjust(left=0.12, right=0.995, top=0.89, bottom=0.13)

plt.savefig('transfer_1.pdf')
plt.show()

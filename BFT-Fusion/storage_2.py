import xlrd
import matplotlib.pyplot as plt
import numpy as np

colorDict = {
    'Full-replication': '#C00000', 
    'BFT-Store': '#00B050', 
    'BFT-Fusion(k=5%)': '#F79646', 
    'BFT-Fusion(k=10%)': '#1f497d', 
    'BFT-Fusion(k=15%)':'#4BACC6', 
    'BFT-Fusion(k=20%)':'#8064A2'
}

markerDict = {
    'Full-replication': 'D', 
    'BFT-Store': 'o', 
    'BFT-Fusion(k=5%)': 'v', 
    'BFT-Fusion(k=10%)': '^', 
    'BFT-Fusion(k=15%)':'>', 
    'BFT-Fusion(k=20%)':'<'
}

hatchDict = {
    'network': '\\\\\\\\',
    'computation': '----',
    'I/O': '////',
}

readbook = xlrd.open_workbook('latency.xlsx')
dataSheet = readbook.sheet_by_name('storage')

startRow = 8
finalRow = 13

dataDict = {}

baseMethodArr = [i for i in dataSheet.row_values(0) if i != ''][1:-1]
xArr = []

xLabel = dataSheet.row_values(startRow)[0].split(',')[0].split(':')[1]
yLabel = dataSheet.row_values(startRow)[0].split(',')[1].split(':')[1]

for curMethod in baseMethodArr:
    dataDict[curMethod] = []

for i in range(startRow+1, finalRow+1):
    curRow = dataSheet.row_values(i)
    print(curRow)
    xArr.append(curRow[1])
    for j in range(len(baseMethodArr)):
        dataDict[baseMethodArr[j]].append(curRow[j+2])

print(dataDict)

methodArr = []
for i in range(len(baseMethodArr)):
    methodArr.append(baseMethodArr[i//3+i%3*2])

ind = np.arange(len(xArr))
line_lw = 3
legendArr = []
legendEntryArr = []

plt.figure(figsize=(9,6))


for i in range(len(methodArr)):
    curMethod = methodArr[i]
    plt.plot(xArr, dataDict[curMethod], linewidth=line_lw, label=curMethod, \
        color=colorDict[curMethod], marker=markerDict[curMethod], markersize=12, zorder=5)

plt.ylabel(yLabel, fontsize=28)
plt.xlabel(xLabel, fontsize=28)

plt.legend(fontsize=22, ncol=2, columnspacing=0.6, labelspacing=0.2, loc='upper center', bbox_to_anchor=(0.4755, 1.375))
plt.yticks(fontsize=22)
plt.xticks(xArr, [str(int(i)) for i in xArr], fontsize=22)

plt.ylim(0)
plt.grid(True, linestyle='-.', axis='both')

plt.subplots_adjust(left=0.145, right=0.995, top=0.78, bottom=0.13)

plt.savefig('storage_2.pdf')
plt.show()

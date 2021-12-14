import xlrd
import matplotlib.pyplot as plt
import numpy as np

colorDict = {
    'Full-replication': '#C00000', 
    'BFT-Store': '#00B050', 
    'k=5%': '#F79646', 
    'k=10%': '#1f497d', 
    'k=15%':'#4BACC6', 
    'k=20%':'#8064A2'
}

markerDict = {
    'Full-replication': 'D', 
    'BFT-Store': 'o', 
    'k=5%': 'v', 
    'k=10%': '^', 
    'k=15%':'>', 
    'k=20%':'<'
}

hatchDict = {
    'network': '\\\\\\\\',
    'computation': '----',
    'I/O': '////',
}

readbook = xlrd.open_workbook('latency(2)(2).xlsx')
dataSheet = readbook.sheet_by_name('transfer')

startRow = 16
finalRow = 21

dataArr = []
xArr = []

xLabel = dataSheet.row_values(startRow)[0].split(',')[0].split(':')[1]
yLabel = dataSheet.row_values(startRow)[0].split(',')[1].split(':')[1]

for i in range(startRow+1, finalRow+1):
    curRow = dataSheet.row_values(i)
    xArr.append(curRow[1])
    dataArr.append(curRow[2])

ind = np.arange(len(xArr))
line_lw = 3
legendArr = []
legendEntryArr = []

plt.figure(figsize=(9,6))


plt.plot(xArr, dataArr, linewidth=line_lw, label='Latency', \
    color='#00B050', marker='o', markersize=12, zorder=5)

plt.ylabel(yLabel, fontsize=26)
plt.xlabel(xLabel, fontsize=26)

plt.legend(fontsize=24)
plt.yticks(fontsize=22)
plt.xticks(xArr, [str(int(i)) for i in xArr], fontsize=22)

# plt.ylim(0)
plt.grid(True, linestyle='-.', axis='both')

plt.subplots_adjust(left=0.145, right=0.995, top=0.99, bottom=0.13)

plt.savefig('transfer_3.pdf')
plt.show()

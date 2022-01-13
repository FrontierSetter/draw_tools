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

inFile = open('bend.txt', 'r')
dataArr = []

while True:
    curLine = inFile.readline()
    if curLine == '':
        break
    curNum = int(curLine.strip('\n'))
    bend=(4095-curNum)/4095*210
    if bend>95:
        bend=95
    dataArr.append(int(bend))


plt.figure(figsize=(9,6))
line_lw = 3

plt.plot(range(len(dataArr)), dataArr, linewidth=line_lw, label='bend', \
    color="#1f497d", markersize=10, zorder=5, markevery=int(len(dataArr)/40))

plt.ylabel("degree", fontsize=28)
plt.xlabel("time sequence", fontsize=28)

plt.legend(fontsize=22)
plt.yticks(fontsize=22)
plt.xticks(fontsize=22)

plt.ylim(0)
plt.xlim(0, len(dataArr))
plt.grid(True, linestyle='-.', axis='both')

plt.subplots_adjust(left=0.1, right=0.965, top=0.99, bottom=0.14)

plt.savefig('bend.pdf')
plt.show()

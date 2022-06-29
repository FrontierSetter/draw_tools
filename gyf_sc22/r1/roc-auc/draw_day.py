from dataclasses import dataclass
import xlrd
import matplotlib.pyplot as plt
import numpy as np
import sys

algoDict = {
    'apsnet': 'APSNet',
    'rf': 'RF',
    'lstm': 'LSTM',
    'nn': 'NN'
}

colorDict = {
    'APSNet': '#324665', 
    'RF': '#EED777', 
    'KNN': '#3478BF', 
    'LR': '#40A776', 
    'DT': '#F15326', 
    'SVM': '#8064A2', 
    'NN': '#C00000', 
    'LSTM': '#91CC75', 
}

markerDict = {
    'APSNet': 's', 
    'RF': 'o', 
    'KNN': 'd', 
    'LR': '^', 
    'DT': 'v', 
    'SVM': '<', 
    'NN': '>', 
    'LSTM': 'X', 
}


targetDay = int(sys.argv[1])

# dateArr = [5,7,15,30,45,60,90,150]
methodArr = ['apsnet','rf','lstm','nn']

fprArrs = []
tprArrs = []

for i in range(len(methodArr)):
    fprArrs.append([])
    fprFilePath = "auc_%d\\auc_fpr_%s_%d.xlsx" % (targetDay, methodArr[i], targetDay)
    fprBook = xlrd.open_workbook(fprFilePath)
    fprSheet = fprBook.sheet_by_index(0)
    nrows = fprSheet.nrows
    for idx in range(1, nrows):
        fprArrs[-1].append(fprSheet.row_values(idx)[1])

    tprArrs.append([])
    tprFilePath = "auc_%d\\auc_tpr_%s_%d.xlsx" % (targetDay, methodArr[i], targetDay)
    tprBook = xlrd.open_workbook(tprFilePath)
    tprSheet = tprBook.sheet_by_index(0)
    nrows = tprSheet.nrows
    for idx in range(1, nrows):
        tprArrs[-1].append(tprSheet.row_values(idx)[1])
    
    print(fprArrs[-1][:20])
    print(tprArrs[-1][:20])

# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(9,6))

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='both')

# 各项参数
import sys
sys.path.append("..\\..\\general\\header")
from marker import *
for i in range(len(methodArr)):
    curName = algoDict[methodArr[i]]
    curP = plt.plot(fprArrs[i], tprArrs[i], label=curName,\
        color=colorDict[curName], lw=2.5, marker=markerDict[curName], markersize=8, markevery=getMarkerArr(len(fprArrs[i]),15))
    
# 设置坐标轴文字
plt.ylabel('TPR', fontsize=28)
plt.xlabel('FPR', fontsize=28)

# 设置坐标轴刻度
plt.yticks(fontsize=26)
plt.xticks(fontsize=26)

# 设置图例
plt.legend(fontsize=24, loc='lower right',\
    labelspacing=0.1, handletextpad=0.6, handlelength=1.5, ncol=1, columnspacing=0.8)

# 设置坐标轴范围
# plt.xlim(0.086)

# 设置图片边距
plt.subplots_adjust(left=0.125, right=0.995, top=0.970, bottom=0.135)

# 保存图片
plt.savefig('.\\image\\roc-auc_%d.pdf' % (targetDay))
# plt.savefig('line.png', dpi=600)

# 显示图片
plt.show()



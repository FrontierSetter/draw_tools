from dataclasses import dataclass
import xlrd
import matplotlib.pyplot as plt
import numpy as np
import sys

colorArr = [
    '#324665', 
    '#EED777', 
    '#3478BF', 
    '#40A776', 
    '#F15326', 
    '#8064A2', 
    '#C00000', 
    '#91CC75', 
]

markerArr = [
    's',
    '^',
    'o',
    'd',
    'v', 
    '<', 
    '>', 
    'X', 
]

targetAlg = sys.argv[1]

dateArr = [5,7,15,30,45,60,90,150]
# dateArr = [7,30,60]

fprArrs = []
tprArrs = []

for i in range(len(dateArr)):
    fprArrs.append([])
    fprFilePath = "auc_%d\\auc_fpr_%s_%d.xlsx" % (dateArr[i], targetAlg, dateArr[i])
    fprBook = xlrd.open_workbook(fprFilePath)
    fprSheet = fprBook.sheet_by_index(0)
    nrows = fprSheet.nrows
    for idx in range(1, nrows):
        fprArrs[-1].append(fprSheet.row_values(idx)[1])

    tprArrs.append([])
    tprFilePath = "auc_%d\\auc_tpr_%s_%d.xlsx" % (dateArr[i], targetAlg, dateArr[i])
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
for i in range(len(dateArr)):
    curP = plt.plot(fprArrs[i], tprArrs[i], label='%d days lookahead' % (dateArr[i] if dateArr[i] != 150 else 120),\
        color=colorArr[i], lw=2.5, marker=markerArr[i], markersize=8, markevery=getMarkerArr(len(fprArrs[i]),15))

    # curP = plt.plot(fprArrs[i], tprArrs[i], label='%d days lookahead' % (dateArr[i]),\
    #     color=colorArr[i], lw=2.5, marker=markerArr[i], markersize=8, markevery=getMarkerArr(len(fprArrs[i]),15))
    
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
plt.savefig('.\\image\\roc-auc_%s.pdf' % (targetAlg))
# plt.savefig('line.png', dpi=600)

# 显示图片
plt.show()



import numpy as np
import matplotlib.pyplot as plt
import random
import xlrd
import argparse

colorDict = {
    'Regular': '#40A776',
    'Infant Weak': '#EC6568'
}
hatchDict = {
    'Regular': '////',
    'Infant Weak': '\\\\\\\\'
}
barName = ['Regular', 'Infant Weak']
xTick = []
valueArr = []

parser = argparse.ArgumentParser(description='画性能图')
parser.add_argument('-f','--file')
args = parser.parse_args()

readbook = xlrd.open_workbook(args.file)
defaultSheet = readbook.sheet_by_name('Sheet1')

xTick = defaultSheet.row_values(17)[11:17]
valueArr.append(defaultSheet.row_values(26)[11:17])
valueArr.append(defaultSheet.row_values(30)[11:17])

print(xTick)
print(valueArr)

# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(9,6))

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='y')

# 各项参数
totalBarNum = len(barName)
bar_width = 0.8/1.1/totalBarNum
gap = 0.12*bar_width
ind = np.arange(len(xTick))

for i in range(len(barName)):
    offset = 0.0-bar_width*(totalBarNum/2.0)-gap*((totalBarNum-1.0)/2)+(i+0.5)*bar_width+i*gap
    # curP = plt.bar(ind+offset, valueArr[i], bar_width, label=barName[i], color=colorDict[barName[i]])
    curP = plt.bar(ind+offset, valueArr[i], bar_width, label=barName[i], \
         hatch=hatchDict[barName[i]], edgeColor=colorDict[barName[i]], lw=3, color='white')
    
# 设置坐标轴文字
plt.ylabel('Precision', fontsize=30)
# plt.xlabel('xName (unit)', fontsize=28)

# 设置坐标轴刻度
plt.yticks(np.arange(0, 1.1, 0.2), fontsize=26)
plt.xticks(range(len(xTick)), xTick, fontsize=30)

# 设置图例
plt.legend(fontsize=26, ncol=2, loc='upper center')

# 设置坐标轴范围
plt.ylim(0, 1.2)

# 设置图片边距
plt.subplots_adjust(left=0.15, right=0.99, top=0.975, bottom=0.075)

# 保存图片
plt.savefig('Precision.pdf')

# 显示图片
plt.show()
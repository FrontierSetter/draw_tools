import xlrd
import argparse
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='画性能图')
parser.add_argument('-f','--file')
args = parser.parse_args()

readbook = xlrd.open_workbook(args.file)
defaultSheet = readbook.sheet_by_name('Sheet1')

xTick = defaultSheet.row_values(9)[11:17]
valueArr = defaultSheet.row_values(10)[11:17]

print(xTick)
print(valueArr)

# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(9,6))

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='y')

# 柱子的宽度
bar_width = 0.6

curP = plt.bar(range(len(xTick)), valueArr, bar_width, color='#40A776')

# 设置坐标轴文字
plt.ylabel('AUC', fontsize=30)
# plt.xlabel('xName (unit)', fontsize=28)

# 设置坐标轴刻度
plt.yticks(fontsize=26)
plt.xticks(range(len(xTick)), xTick, fontsize=30)

# 设置坐标轴范围
plt.ylim(0, 1)

# 设置图片边距
plt.subplots_adjust(left=0.15, right=0.99, top=0.975, bottom=0.075)

# 保存图片
plt.savefig('AUC.pdf')

# 显示图片
plt.show()
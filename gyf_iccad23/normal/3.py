import numpy as np
import matplotlib.pyplot as plt
import xlrd
import argparse

colorDict = {
    'Default Burn-in': '#40A776',
    'Dynamically Adjust Burn-in based on GAN-LSTM': '#EC6568'
}
hatchDict = {
    'Default Burn-in': '////',
    'Dynamically Adjust Burn-in based on GAN-LSTM': '\\\\\\\\'
}
barName = ['Default Burn-in', 'Dynamically Adjust Burn-in based on GAN-LSTM']

xTick = ['']
valueArr = [[1],[0.148]]

print(xTick)
print(valueArr)

# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(9,6))

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='y')

# 各项参数
totalBarNum = len(barName)
bar_width = 0.8/1.1/totalBarNum/2.5
gap = 0.12*bar_width*10
ind = np.arange(len(xTick))

for i in range(len(barName)):
    offset = 0.0-bar_width*(totalBarNum/2.0)-gap*((totalBarNum-1.0)/2)+(i+0.5)*bar_width+i*gap
    # curP = plt.bar(ind+offset, valueArr[i], bar_width, label=barName[i], color=colorDict[barName[i]])
    curP = plt.bar(ind+offset, valueArr[i], bar_width, label=barName[i], \
         hatch=hatchDict[barName[i]], edgeColor=colorDict[barName[i]], lw=3, color='white')
    
# 设置坐标轴文字
# plt.ylabel('         Normalized Time Overhead', fontsize=30)
plt.ylabel('    Normalized Time Overhead', fontsize=30)
# plt.xlabel('Cycles', fontsize=28)

# 设置坐标轴刻度
plt.yticks(fontsize=26)
# plt.yticks(np.arange(0, 1.1, 0.2), fontsize=26)
plt.xticks(range(len(xTick)), xTick, fontsize=30)

# 设置图例
plt.legend(handlelength=1, fontsize=22, ncol=1, loc='lower center', bbox_to_anchor=(0.46, 0.98))
# plt.legend(fontsize=24, ncol=1, loc='center right')

# 设置坐标轴范围
plt.ylim(0, 1.02)
plt.xlim(-0.5, 0.5)

# 设置图片边距
# plt.subplots_adjust(left=0.15, right=0.99, top=0.69, bottom=0.075)
plt.subplots_adjust(left=0.15, right=0.99, top=0.8, bottom=0.075)

# 保存图片
plt.savefig('time2.pdf')

# 显示图片
plt.show()
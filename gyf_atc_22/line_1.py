import numpy as np
import matplotlib.pyplot as plt
import random

def random_color():
     colors1 = '0123456789ABCDEF'
     num = "#"
     for i in range(6):
         num += random.choice(colors1)
     return num

# 每个stage对应的颜色和hatch，记得修改
colorDict = {
    'precision': '#1f497d', 
    'recall': '#00B050', 
    'f1-score': '#C00000', 
    'support': '#F79646', 
}

markerDict = {
    'precision': 'o', 
    'recall': 'd', 
    'f1-score': '^', 
    'support': 'x', 
}

inFile = open('line_1.csv', 'r')

headLine = inFile.readline()

lineName = headLine.strip('\n').split(',')[1:]

xTick = []
valueArr = []
for i in range(len(lineName)):
    valueArr.append([])

while True:
    curLine = inFile.readline()
    if curLine == '':
        break
    curArr = curLine.strip('\n').split(',')

    xTick.append(curArr[0])
    for i in range(len(lineName)):
        valueArr[i].append(float(curArr[i+1]))

print(lineName)
print(valueArr)
print(xTick)

# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(9,6))

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='both')

# 各项参数
line_lw = 2
for i in range(len(lineName)):
    curP = plt.plot(range(len(xTick)), valueArr[i], label=lineName[i], lw=line_lw, \
        color=colorDict[lineName[i]], marker=markerDict[lineName[i]], markersize=12, markevery=max(int(len(valueArr)/20),1))
    
# 设置坐标轴文字
plt.ylabel('yName (unit)', fontsize=28)
plt.xlabel('xName (unit)', fontsize=28)

# 设置坐标轴刻度
plt.yticks(fontsize=26)
plt.xticks(fontsize=26, rotation=15)

# 设置图例
plt.legend(fontsize=26)

# 设置坐标轴范围
plt.xlim(0, len(xTick)-1)

# 设置图片边距
plt.subplots_adjust(left=0.15, right=0.99, top=0.975, bottom=0.15)

# 保存图片
plt.savefig('line_1.pdf')
# plt.savefig('line.png', dpi=600)

# 显示图片
plt.show()
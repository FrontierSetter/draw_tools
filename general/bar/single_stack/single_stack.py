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
    'value1': '#1f497d', 
    'value2': '#00B050', 
    'value3': '#C00000', 
}

hatchDict = {
    'value1': '\\\\\\\\',
    'value2': '----',
    'value3': '////',
}

inFile = open('single_stack.csv', 'r')

headLine = inFile.readline()

stageName = headLine.strip('\n').split(',')[1:]

xTick = []
valueArr = []
for i in range(len(stageName)):
    valueArr.append([])

while True:
    curLine = inFile.readline()
    if curLine == '':
        break
    curArr = curLine.strip('\n').split(',')

    xTick.append(curArr[0])
    for i in range(len(stageName)):
        valueArr[i].append(float(curArr[i+1]))

print(stageName)
print(valueArr)
print(xTick)

# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(9,6))

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='y')

# 柱子的宽度
bar_width = 0.3

legendArr = []
legendName = []

curBase = [0]*len(xTick)
for i in range(len(stageName)):
    # 画图，linewidth调整外边框粗细，hatch粗细怎么调整问贾冉昊，我没用过不知道
    curP = plt.bar(range(len(xTick)), valueArr[i], bar_width, bottom=curBase, label=stageName[i], \
        edgecolor=colorDict[stageName[i]] if stageName[i] in colorDict else random_color(), \
            hatch=hatchDict[stageName[i]] if stageName[i] in hatchDict else 'x', color='white', linewidth=2)
    
    # 默认的legend和stack的顺序是反着的，所以需要手动维护顺序
    legendArr.insert(0, curP)
    legendName.insert(0, stageName[i])
    
    for j in range(len(valueArr[i])):
        curBase[j] += valueArr[i][j]

# 设置坐标轴文字
plt.ylabel('yName (unit)', fontsize=28)
plt.xlabel('xName (unit)', fontsize=28)

# 设置坐标轴刻度
plt.yticks(fontsize=26)
plt.xticks(range(len(xTick)), xTick, fontsize=26)

# 设置图例
plt.legend(legendArr, legendName, fontsize=26)

# 设置坐标轴范围
# plt.ylim(0, 108)

# 设置图片边距
plt.subplots_adjust(left=0.195, right=0.99, top=0.975, bottom=0.15)

# 保存图片
plt.savefig('single_stack.pdf')
plt.savefig('single_stack.png', dpi=600)

# 显示图片
plt.show()
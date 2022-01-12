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

inFile = open('group_bar.csv', 'r')

headLine = inFile.readline()

barName = headLine.strip('\n').split(',')[1:]

xTick = []
valueArr = []
for i in range(len(barName)):
    valueArr.append([])

while True:
    curLine = inFile.readline()
    if curLine == '':
        break
    curArr = curLine.strip('\n').split(',')

    xTick.append(curArr[0])
    for i in range(len(barName)):
        valueArr[i].append(float(curArr[i+1]))

print(barName)
print(valueArr)
print(xTick)

# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(9,6))

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='y')

# 各项参数
totalBarNum = len(barName)
bar_width = 0.8/1.1/totalBarNum
gap = 0.1*bar_width
ind = np.arange(len(xTick))

for i in range(len(barName)):
    offset = 0.0-bar_width*(totalBarNum/2.0)-gap*((totalBarNum-1.0)/2)+(i+0.5)*bar_width+i*gap
    curP = plt.bar(ind+offset, valueArr[i], bar_width, label=barName[i], \
        color=colorDict[barName[i]] if barName[i] in colorDict else random_color())
    
# 设置坐标轴文字
plt.ylabel('yName (unit)', fontsize=28)
plt.xlabel('xName (unit)', fontsize=28)

# 设置坐标轴刻度
plt.yticks(fontsize=26)
plt.xticks(range(len(xTick)), xTick, fontsize=26)

# 设置图例
plt.legend(fontsize=26)

# 设置坐标轴范围
# plt.ylim(0, 108)

# 设置图片边距
plt.subplots_adjust(left=0.195, right=0.99, top=0.975, bottom=0.15)

# 保存图片
plt.savefig('group_bar.pdf')
plt.savefig('group_bar.png', dpi=600)

# 显示图片
plt.show()
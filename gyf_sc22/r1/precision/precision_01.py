import numpy as np
import matplotlib.pyplot as plt
import random

numCol = 2

def random_color():
     colors1 = '0123456789ABCDEF'
     num = "#"
     for i in range(6):
         num += random.choice(colors1)
     return num

# 每个stage对应的颜色和hatch，记得修改
colorDict = {
    'healthy': '#00B050', 
    'failed': '#C00000', 
}

hatchDict = {
    # 'healthy': '\\\\\\\\',
    # 'failure': '////',
    'healthy': '..',
    'failed': 'xx',
}

inFile = open('precision.csv', 'r')

headLine = inFile.readline()
xTick = [x for x in headLine.strip('\n').split(',')[1:] if x != '']

headLine = inFile.readline()
barName = headLine.strip('\n').split(',')[1:numCol+1]

valueArr = []
intervalArr = []

while True:
    curLine = inFile.readline()
    if curLine == '':
        break
    curArr = curLine.strip('\n').split(',')

    intervalArr.append(curArr[0])
    valueArr.append([float(x) for x in curArr[1:]])

print(barName)
print(valueArr)
print(xTick)

for plotNum in range(len(valueArr)):
# for plotNum in range(1):
    # 生成图片实例，figsize的元组是宽高比
    fig = plt.figure(figsize=(9,6))

    curValArr = []
    for i in range(len(barName)):
        curValArr.append([valueArr[plotNum][idx] for idx in range(i, len(valueArr[plotNum]), 3)])
    print(curValArr)

    # 生成背后的网格
    plt.grid(True, linestyle='-.', axis='y')

    # 各项参数
    totalBarNum = len(barName)
    bar_width = 0.8/1.1/totalBarNum
    gap = 0.1*bar_width
    ind = np.arange(len(xTick))

    for i in range(len(barName)):
        offset = 0.0-bar_width*(totalBarNum/2.0)-gap*((totalBarNum-1.0)/2)+(i+0.5)*bar_width+i*gap
        curP = plt.bar(ind+offset, curValArr[i], bar_width, label=barName[i], \
            color='white', edgecolor=colorDict[barName[i]], linewidth=3, hatch=hatchDict[barName[i]])
        
    # 设置坐标轴文字
    plt.ylabel('Precision', fontsize=28)
    plt.xlabel('Method', fontsize=28)

    # 设置坐标轴刻度
    plt.yticks(fontsize=26)
    plt.xticks(range(len(xTick)), xTick, fontsize=24, rotation=-15)

    # 设置图例
    plt.legend(fontsize=26, ncol=2, loc='upper right')

    # 设置坐标轴范围
    # plt.ylim(0, 108)

    # 设置图片边距
    plt.subplots_adjust(left=0.125, right=0.99, top=0.995, bottom=0.19)

    # 保存图片
    plt.savefig('.\\image\\precision_01_%s.pdf' % (intervalArr[plotNum]))

    # 显示图片
    plt.show()
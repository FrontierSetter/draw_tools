import numpy as np
import matplotlib.pyplot as plt
import random

idCol = 3

def random_color():
     colors1 = '0123456789ABCDEF'
     num = "#"
     for i in range(6):
         num += random.choice(colors1)
     return num

# 每个stage对应的颜色和hatch，记得修改
colorDict = {
    '0': '#3478BF', 
    '1': '#F15326', 
    'total(Acc)': '#5B9BD5', 
}

inFile = open('precision.csv', 'r')

headLine = inFile.readline()
xTick = [x for x in headLine.strip('\n').split(',')[1:] if x != '']

headLine = inFile.readline()
barName = headLine.strip('\n').split(',')[idCol]

valueArr = []
intervalArr = []

while True:
    curLine = inFile.readline()
    if curLine == '':
        break
    curArr = curLine.strip('\n').split(',')

    intervalArr.append(curArr[0])
    valueArr.append([float(x) for x in curArr[1:]])

# print(barName)
print(valueArr)
print(xTick)

for plotNum in range(len(valueArr)):
    # 生成图片实例，figsize的元组是宽高比
    fig = plt.figure(figsize=(9,6))

    curValArr = []
    curValArr = [valueArr[plotNum][idx] for idx in range(idCol-1, len(valueArr[plotNum]), 3)]
    print(curValArr)

    # 生成背后的网格
    plt.grid(True, linestyle='-.', axis='y')

    # 各项参数
    bar_width = 0.5
    curP = plt.bar(range(len(xTick)), curValArr, bar_width, label=barName, color=colorDict[barName])
        
    # 设置坐标轴文字
    plt.ylabel('Accuracy', fontsize=28)
    plt.xlabel('Method', fontsize=28)

    # 设置坐标轴刻度
    plt.yticks(fontsize=26)
    plt.xticks(range(len(xTick)), xTick, fontsize=24, rotation=-15)

    # 设置图例
    # plt.legend(fontsize=26, ncol=2, loc='upper right')

    # 设置坐标轴范围
    # plt.ylim(0, 108)

    # 设置图片边距
    plt.subplots_adjust(left=0.125, right=0.99, top=0.995, bottom=0.19)

    # 保存图片
    plt.savefig('.\\image\\precision_total_%s.pdf' % (intervalArr[plotNum]))

    # 显示图片
    plt.show()
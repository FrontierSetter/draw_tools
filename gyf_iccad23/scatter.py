import numpy as np
import matplotlib.pyplot as plt
import random


# 读取real文件
realArr = []
inRealFile = open('real.csv', 'r')
inRealFile.readline()

while True:
    curLine = inRealFile.readline()
    if curLine == '':
        break
    curArr = curLine.strip('\n').split(',')

    curX = float(curArr[1])
    curY = float(curArr[2])
    realArr.append([curX, curY])

# 读取fake文件
fakeArr = []
inFakeFile = open('fake.csv', 'r')
inFakeFile.readline()

while True:
    curLine = inFakeFile.readline()
    if curLine == '':
        break
    curArr = curLine.strip('\n').split(',')

    curX = float(curArr[1])
    curY = float(curArr[2])
    fakeArr.append([curX, curY])


# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(12,6))

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='both')

# 画fake散点
fakeX = [item[0] for item in fakeArr]
fakeY = [item[1] for item in fakeArr]
# plt.scatter(fakeX, fakeY, label='Artifactically\ngenerated', color='#3478BF', edgecolors='white', s=60)
plt.scatter(fakeX, fakeY, color='#3478BF', edgecolors='white', s=60)
plt.scatter([], [], label='Artifactically\ngenerated', color='#3478BF', edgecolors='white', s=300)

# 画real散点
realX = [item[0] for item in realArr]
realY = [item[1] for item in realArr]
# plt.scatter(realX, realY, label='Real', color='#F15326', edgecolors='white', s=60, marker='^')
plt.scatter(realX, realY, color='#F15326', edgecolors='white', s=60, marker='X')
plt.scatter([], [], label='Real', color='#F15326', edgecolors='white', s=300, marker='X')

# 设置坐标轴文字
plt.ylabel('$y_{tsne}$', fontsize=30)
plt.xlabel('$x_{tsne}$', fontsize=30)

# 设置坐标轴刻度
plt.yticks(fontsize=26)
plt.xticks(fontsize=26)

# 设置图例
# plt.legend(fontsize=26, handletextpad=0, ncol=1, loc="lower right")
plt.legend(fontsize=26, handletextpad=0, ncol=1, bbox_to_anchor=(0.99, -0.04), loc="lower left")
# plt.legend(fontsize=26, handletextpad=0, ncol=2, bbox_to_anchor=(0.5, 0.98), loc="lower center")

# 设置坐标轴范围
# plt.ylim(-0.1, 1.1)
# plt.xlim(-0.1, 1.1)

# 设置图片边距
plt.subplots_adjust(left=0.095, right=0.710, top=0.98, bottom=0.15)

# 保存图片
plt.savefig('scatter2.pdf')

# 显示图片
plt.show()
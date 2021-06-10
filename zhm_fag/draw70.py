import xlrd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.font_manager._rebuild()
plt.rcParams['font.sans-serif']=['Times New Roman']#设置字体
import numpy as np

fileName = 'RW70'

data = xlrd.open_workbook('..\\'+fileName+'.xlsx')
table = data.sheets()[1]

colorDict = {'FAG-Conv':'darkviolet','Conv':'dodgerblue','FAG-RP':'skyblue','RP':'gold','FAG-PPR':'mediumseagreen','PPR':'tomato'}  #设置配色

# 以下是业务逻辑
newGroup = True

responstDict = {}
methodArr = []
groupName = []

def constructName(K, R, HS):
    # return ("$(%d,%d,%d)$" % (K, R, HS))
    if K == 4:
        return ("$m_{hs}=%d$" % (HS))
    else:
        return (" $m_{hs}=%d$ " % (HS))
    # return ("$RS(%d,%d)m_{hs}=%d$" % (K, R, HS))

for i in range(table.nrows):
    curK = table.row_values(i)[0]
    curR = table.row_values(i)[1]
    curHS = table.row_values(i)[2]

    curMethod = table.row_values(i)[3]
    curResponse = table.row_values(i)[-2]

    if curMethod == '':
        continue

    if curMethod not in methodArr:
        methodArr.append(curMethod)
        responstDict[curMethod]=[]
    
    if constructName(curK,curR,curHS) not in groupName:
        groupName.append(constructName(curK,curR,curHS))
    responstDict[curMethod].append(curResponse)

#以上是业务逻辑

x=np.arange(len(groupName))
print(x)
bar_width=0.3#设置柱状图的宽度
plt.figure(figsize=(9,7.5))

# 第一幅子图
plt.subplot(311)
curNum = 0
for method in methodArr:
    if 'Conv' not in method:
        continue
    print(method, responstDict[method])
    print(colorDict[method])
    plt.bar(x+curNum*(bar_width+0.01),responstDict[method], bar_width, label=method, color=colorDict[method], hatch='//' if 'FAG' in method else '\\\\')    #实际画图
    curNum += 1

plt.ylabel('Throughput(s^-1)', fontsize=15)

plt.legend(fontsize=14,ncol=2,columnspacing=0.8,handletextpad=0.5)#显示图例，即label
plt.yticks(fontsize=16)
plt.xticks(x+(bar_width+0.01)/2,groupName, fontsize=16)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
# plt.xticks(rotation=352) #x轴标签旋转
plt.subplots_adjust(left=0.09, right=0.98, top=0.98, bottom=0.09)#图片的页边距


# 第二幅子图
plt.subplot(312)
curNum = 0
for method in methodArr:
    if 'RP' not in method:
        continue
    print(method, responstDict[method])
    print(colorDict[method])
    plt.bar(x+curNum*(bar_width+0.01),responstDict[method], bar_width, label=method, color=colorDict[method], hatch='//' if 'FAG' in method else '\\\\')
    curNum += 1

plt.ylabel('Throughput(s^-1)', fontsize=15)

plt.legend(fontsize=14,ncol=2,columnspacing=0.8,handletextpad=0.5)#显示图例，即label
plt.yticks(fontsize=16)
# plt.ylim(ymax=0.75)
plt.xticks(x+(bar_width+0.01)/2,groupName, fontsize=16)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
# plt.xticks(rotation=45)
plt.subplots_adjust(left=0.09, right=0.98, top=0.98, bottom=0.09)


# 第三幅子图
plt.subplot(313)
curNum = 0
for method in methodArr:
    if 'PPR' not in method:
        continue
    print(method, responstDict[method])
    print(colorDict[method])
    plt.bar(x+curNum*(bar_width+0.01),responstDict[method], bar_width, label=method, color=colorDict[method], hatch='//' if 'FAG' in method else '\\\\')
    curNum += 1

plt.ylabel('Throughput(s^-1)', fontsize=15)

plt.legend(fontsize=14,ncol=2,columnspacing=0.8,handletextpad=0.5)#显示图例，即label
plt.yticks(fontsize=16)
# plt.ylim(ymax=1.2)
plt.xticks(x+(bar_width+0.01)/2,groupName, fontsize=16)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
# plt.xticks(rotation=45)
plt.subplots_adjust(left=0.09, right=0.98, top=0.98, bottom=0.12)




plt.savefig(fileName+'.pdf')

plt.show()


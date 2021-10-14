import xlrd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.font_manager._rebuild()
plt.rcParams['font.sans-serif']=['Times New Roman']#设置字体
import numpy as np
from textwrap import fill



# colorDict = {'PRM-Typical':'#008000','Greedy-Typical':'#fa8080','Typical':'#0000FF','PRM-PPR':'#95a2ff','Greedy-PPR':'#87e885','PPR':'gold','PRM-RP':'darkviolet','Greedy-RP':'dodgerblue','RP':'skyblue'}  #设置配色

colorDict = {'PRM-Typical':'#008000','Typical':'#0000FF','PRM-RP':'darkviolet','RP':'skyblue','PRM-PPR':'#95a2ff','PPR':'gold'}  #设置配色



dataArr = [{}]
# readbook = xlrd.open_workbook('RS(4,3)-1.6G-throughput.xlsx')
# readbook = xlrd.open_workbook('RS(4,3)-2.5G-throughput.xlsx')
# readbook = xlrd.open_workbook('RS(4,3)-6.9G-throughput.xlsx')
# readbook = xlrd.open_workbook('RS(4,3)-21.5G-throughput.xlsx')


# readbook = xlrd.open_workbook('RS(4,3)-138G-throughput.xlsx')
# readbook = xlrd.open_workbook('RS(4,3)-513G-throughput.xlsx')

# readbook = xlrd.open_workbook('new_RS(4,3)-1.6G-throughput.xlsx')
# readbook = xlrd.open_workbook('new_RS(4,3)-2.5G-throughput.xlsx')
# readbook = xlrd.open_workbook('new_RS(4,3)-6.9G-throughput.xlsx')
readbook = xlrd.open_workbook('new_RS(4,3)-21.5G-throughput.xlsx')

sheets = readbook.sheets()

for sheetId in range(1, len(sheets)):

    curSheet = sheets[sheetId]

    nrows = curSheet.nrows
    metaRow = curSheet.row_values(0)

    dataArr.append({})

    dataArr[-1]['x-arr'] = []
    dataArr[-1][metaRow[1]] = []
    dataArr[-1][metaRow[2]] = []
    # dataArr[-1][metaRow[3]] = []

    for rowId in range(1, nrows):
        curRow = curSheet.row_values(rowId)

        dataArr[-1]['x-arr'].append(curRow[0])
        dataArr[-1][metaRow[1]].append(curRow[1])
        dataArr[-1][metaRow[2]].append(curRow[2])
        # dataArr[-1][metaRow[3]].append(curRow[2])
# print(dataArr)

# readbook = xlrd.open_workbook('RS(6,9)-1.6G-throughput.xlsx')
# readbook = xlrd.open_workbook('RS(6,9)-2.5G-throughput.xlsx')
# readbook = xlrd.open_workbook('RS(6,9)-6.9G-throughput.xlsx')
# readbook = xlrd.open_workbook('RS(6,9)-21.5G-throughput.xlsx')

# readbook = xlrd.open_workbook('RS(6,9)-138G-throughput.xlsx')
# readbook = xlrd.open_workbook('RS(6,9)-513G-throughput.xlsx')

# readbook = xlrd.open_workbook('new_RS(6,9)-1.6G-throughput.xlsx')
# readbook = xlrd.open_workbook('new_RS(6,9)-2.5G-throughput.xlsx')
# readbook = xlrd.open_workbook('new_RS(6,9)-6.9G-throughput.xlsx')
readbook = xlrd.open_workbook('new_RS(6,9)-21.5G-throughput.xlsx')

sheets = readbook.sheets()

for sheetId in range(1, len(sheets)):

    curSheet = sheets[sheetId]

    nrows = curSheet.nrows
    metaRow = curSheet.row_values(0)
    # print(metaRow)

    # dataArr.append({})

    # dataArr[-1]['x-arr'] = []
    # dataArr[-1][metaRow[1]] = []
    # dataArr[-1][metaRow[2]] = []

    for rowId in range(1, nrows):
        curRow = curSheet.row_values(rowId)
        # print(curRow)
        if curRow[0] == '':
            continue

        dataArr[sheetId]['x-arr'].append(curRow[0])
        dataArr[sheetId][metaRow[1]].append(curRow[1])
        dataArr[sheetId][metaRow[2]].append(curRow[2])
        # dataArr[sheetId][metaRow[3]].append(curRow[3])

print(dataArr)

ind=np.arange(len(dataArr[1]['x-arr']))
bar_width = 0.3#设置柱状图的宽度
gap_width = 0.01
# totalBarNum = 2
totalBarNum = 3
plt.figure(figsize=(9,7.5))

# 第一幅子图
plt.subplot(311)
barCnt = 0
for barId in dataArr[1].keys():
    if barId == 'x-arr':
        continue
    
    offset = 0.0-bar_width*(totalBarNum/2.0)-gap_width*((totalBarNum-1.0)/2)+(barCnt+0.5)*bar_width+barCnt*gap_width
    plt.bar(ind+offset, dataArr[1][barId], bar_width, label=barId, color=colorDict[barId], hatch='//' if barId == 'PRM-Typical' else '\\\\')
    barCnt += 1


'''
plt.ylabel('Throughput(M/s)', fontsize=15)
plt.legend(fontsize=14,ncol=2,columnspacing=0.8,handletextpad=0.5)#显示图例，即label
plt.yticks(fontsize=16)
plt.xticks(ind, dataArr[1]['x-arr'], fontsize=16)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
# plt.xticks(rotation=352) #x轴标签旋转
plt.subplots_adjust(left=0.09, right=0.98, top=0.98, bottom=0.09)#图片的页边距
'''

plt.ylabel('Throughput(M/s)', fontsize=16)
plt.legend(fontsize=16,ncol=3,columnspacing=0.8,handletextpad=0.5)#显示图例，即label
plt.yticks(fontsize=16)
# plt.xticks(ind, dataArr[1]['x-arr'], fontsize=16)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
plt.xticks(ind, dataArr[1]['x-arr'], fontsize=14)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
# plt.xticks(rotation=352) #x轴标签旋转
plt.subplots_adjust(left=0.09, right=0.98, top=0.98, bottom=0.09)#图片的页边距


# 第二幅子图.
plt.subplot(312)
barCnt = 0
for barId in dataArr[2].keys():
    if barId == 'x-arr':
        continue
    
    offset = 0.0-bar_width*(totalBarNum/2.0)-gap_width*((totalBarNum-1.0)/2)+(barCnt+0.5)*bar_width+barCnt*gap_width
    print(dataArr[2][barId])

    plt.bar(ind+offset, dataArr[2][barId], bar_width, label=barId, color=colorDict[barId], hatch='//' if barId == 'PRM-PPR' else '\\\\')
    barCnt += 1



'''
plt.ylabel('Throughput(M/s)', fontsize=15)
plt.legend(fontsize=14,ncol=2,columnspacing=0.8,handletextpad=0.5)#显示图例，即label
plt.yticks(fontsize=16)
plt.xticks(ind, dataArr[2]['x-arr'], fontsize=16)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
# plt.xticks(rotation=352) #x轴标签旋转
plt.subplots_adjust(left=0.09, right=0.98, top=0.98, bottom=0.09)#图片的页边距
'''
plt.ylabel('Throughput(M/s)', fontsize=16)
plt.legend(fontsize=16,ncol=3,columnspacing=0.8,handletextpad=0.5)#显示图例，即label
plt.yticks(fontsize=16)
# plt.xticks(ind, dataArr[2]['x-arr'], fontsize=16)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
plt.xticks(ind, dataArr[2]['x-arr'], fontsize=14)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
# plt.xticks(rotation=352) #x轴标签旋转
plt.subplots_adjust(left=0.09, right=0.98, top=0.98, bottom=0.09)#图片的页边距


# 第三幅子图
plt.subplot(313)
barCnt = 0
for barId in dataArr[3].keys():
    if barId == 'x-arr':
        continue
    
    offset = 0.0-bar_width*(totalBarNum/2.0)-gap_width*((totalBarNum-1.0)/2)+(barCnt+0.5)*bar_width+barCnt*gap_width
    plt.bar(ind+offset, dataArr[3][barId], bar_width, label=barId, color=colorDict[barId], hatch='//' if barId == 'PRM-RP' else '\\\\')
    barCnt += 1

'''
plt.ylabel('Throughput(M/s)', fontsize=15)
plt.legend(fontsize=14,ncol=2,columnspacing=0.8,handletextpad=0.5)#显示图例，即label
plt.yticks(fontsize=16)
plt.xticks(ind, dataArr[3]['x-arr'], fontsize=16)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
# plt.xticks(rotation=352) #x轴标签旋转
plt.subplots_adjust(left=0.09, right=0.98, top=0.98, bottom=0.09)#图片的页边距
'''
plt.ylabel('Throughput(M/s)', fontsize=16)
plt.legend(fontsize=16,ncol=3,columnspacing=0.8,handletextpad=0.5)#显示图例，即label
plt.yticks(fontsize=16)
# plt.xticks(ind, dataArr[3]['x-arr'], fontsize=16)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
plt.xticks(ind, dataArr[3]['x-arr'], fontsize=14)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
# plt.xticks(ind, dataArr[4]['x-arr'], fontsize=16)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
# plt.xticks(rotation=352) #x轴标签旋转
plt.subplots_adjust(left=0.09, right=0.98, top=0.98, bottom=0.09)#图片的页边距

# plt.hlines(-5, 0, 10, colors = "r", linestyles = "dashed")


# plt.savefig('1.6G_throughput.pdf')
# plt.savefig('2.5G_throughput.pdf')
# plt.savefig('6.9G_throughput.pdf')
# plt.savefig('21.5G_throughput.pdf')
# plt.show()

# plt.savefig('138G_throughput.pdf')
# plt.savefig('513G_throughput.pdf')

# plt.savefig('new_25G_throughput.pdf')
# plt.savefig('new_138G_throughput.pdf')
# plt.savefig('new_476G_throughput.pdf')
plt.savefig('new_513G_throughput.pdf')
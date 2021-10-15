import xlrd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from textwrap import fill



# colorDict = {'PRM-Typical':'#008000','Greedy-Typical':'#fa8080','Typical':'#0000FF','PRM-PPR':'#95a2ff','Greedy-PPR':'#87e885','PPR':'gold','PRM-RP':'darkviolet','Greedy-RP':'dodgerblue','RP':'skyblue'}  #设置配色

# colorDict = {'PRM-Typical':'#008000','Typical':'#0000FF','PRM-RP':'darkviolet','RP':'skyblue','PRM-PPR':'#95a2ff','PPR':'gold'}  #设置配色
# colorDict = {'PRM-Typical': '#80499C', 'Typical': '#5088C7', 'PRM-RP': '#87CFEC', 'RP': '#FCD718', 'PRM-PPR': '#3CB474', 'PPR': '#F26750'}  # 设置配色 2021-09-21
colorDict = {'PRM-Typical': '#80499C', 'Typical': '#3478BF', 'PRM-RP': '#219ebc', 'RP': '#B8860B', 'PRM-PPR': '#0a9396', 'PPR': '#F26750', 'GAN': '#C00000'}  # 设置配色 2021-09-21



dataArr = [{}]
# readbook = xlrd.open_workbook('RS(4,3)-1.6G-throughput.xlsx')
# readbook = xlrd.open_workbook('RS(4,3)-2.5G-throughput.xlsx')
# readbook = xlrd.open_workbook('RS(4,3)-6.9G-throughput.xlsx')
# readbook = xlrd.open_workbook('RS(4,3)-21.5G-throughput.xlsx')


# readbook = xlrd.open_workbook('RS(4,3)-138G-throughput.xlsx')
# readbook = xlrd.open_workbook('RS(4,3)-513G-throughput.xlsx')

readbook = xlrd.open_workbook('Places365-Challenge-RS(4,3)减少的网络传输时间-5-dataset-Alexnet.xlsx')
# readbook = xlrd.open_workbook('new_RS(4,3)-2.5G-throughput.xlsx')
# readbook = xlrd.open_workbook('new_RS(4,3)-6.9G-throughput.xlsx')
# readbook = xlrd.open_workbook('new_RS(4,3)-21.5G-throughput.xlsx')

sheets = readbook.sheets()

for sheetId in range(0, len(sheets)):

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

print(dataArr)

ind=np.arange(len(dataArr[1]['x-arr']))
bar_width = 0.3#设置柱状图的宽度
gap_width = 0.06
# totalBarNum = 2
totalBarNum = 2
fig = plt.figure(figsize=(9,7.5))
plt.rc('axes', axisbelow=True)

# 第一幅子图
plt.subplot(311)
barCnt = 0
for barId in dataArr[1].keys():
    if barId == 'x-arr':
        continue
    
    offset = 0.0-bar_width*(totalBarNum/2.0)-gap_width*((totalBarNum-1.0)/2)+(barCnt+0.5)*bar_width+barCnt*gap_width
    plt.bar(ind+offset, dataArr[1][barId], bar_width, label=barId, color='white', linewidth=2, edgecolor=colorDict[barId], hatch='////' if 'PRM' in barId  else '\\\\\\\\')
    barCnt += 1


plt.ylabel('Transmission\nTime(s)', fontsize=22)
plt.legend(fontsize=18,ncol=3,columnspacing=0.8,handletextpad=0.5, loc='upper left')#显示图例，即label
plt.yticks(fontsize=18)
plt.ylim(0, 9100)
# plt.xticks(ind, dataArr[1]['x-arr'], fontsize=16)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
plt.grid(True, linestyle='-.', axis='y')
plt.xticks(ind, dataArr[1]['x-arr'], fontsize=18)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
# plt.xticks(rotation=352) #x轴标签旋转


# 第二幅子图.
plt.subplot(312)
barCnt = 0
for barId in dataArr[2].keys():
    if barId == 'x-arr':
        continue
    
    offset = 0.0-bar_width*(totalBarNum/2.0)-gap_width*((totalBarNum-1.0)/2)+(barCnt+0.5)*bar_width+barCnt*gap_width
    print(dataArr[2][barId])

    plt.bar(ind+offset, dataArr[2][barId], bar_width, label=barId, color='white', linewidth=2, edgecolor=colorDict[barId], hatch='////' if 'PRM' in barId  else '\\\\\\\\')
    barCnt += 1

plt.ylabel('Transmission\nTime(s)', fontsize=22)
plt.legend(fontsize=18,ncol=3,columnspacing=0.8,handletextpad=0.5, loc='upper left')#显示图例，即label
plt.yticks(fontsize=18)
plt.ylim(0, 4200)
# plt.xticks(ind, dataArr[1]['x-arr'], fontsize=16)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
plt.grid(True, linestyle='-.', axis='y')
plt.xticks(ind, dataArr[1]['x-arr'], fontsize=18)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
# plt.xticks(rotation=352) #x轴标签旋转


# 第三幅子图
plt.subplot(313)
barCnt = 0
for barId in dataArr[3].keys():
    if barId == 'x-arr':
        continue
    
    offset = 0.0-bar_width*(totalBarNum/2.0)-gap_width*((totalBarNum-1.0)/2)+(barCnt+0.5)*bar_width+barCnt*gap_width
    plt.bar(ind+offset, dataArr[3][barId], bar_width, label=barId, color='white', linewidth=2, edgecolor=colorDict[barId], hatch='////' if 'PRM' in barId  else '\\\\\\\\')
    barCnt += 1

plt.ylabel('Transmission\nTime(s)', fontsize=22)
plt.legend(fontsize=18,ncol=3,columnspacing=0.8,handletextpad=0.5, loc='upper left')#显示图例，即label
plt.yticks(fontsize=18)
plt.ylim(0, 9000)
# plt.xticks(ind, dataArr[1]['x-arr'], fontsize=16)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
plt.grid(True, linestyle='-.', axis='y')
plt.xticks(ind, dataArr[1]['x-arr'], fontsize=18)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
# plt.xticks(ind, dataArr[4]['x-arr'], fontsize=16)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
# plt.xticks(rotation=352) #x轴标签旋转
plt.subplots_adjust(left=0.175, right=0.98, top=0.99, bottom=0.04)#图片的页边距

# plt.hlines(-5, 0, 10, colors = "r", linestyles = "dashed")



# left,bottom,width,height = 0.002,-0.03,1,0.15
# # left,bottom,width,height = 0.71,0.15,0.25,0.20
# ax1 = fig.add_axes([left,bottom,width,height])
# ax1.axis('off')
# ax1.patch.set_alpha(0.0)
# ax1.spines['top'].set_visible(False)
# ax1.spines['right'].set_visible(False)
# ax1.spines['bottom'].set_visible(False)
# ax1.spines['left'].set_visible(False)


# ax1.set_ylim(0,1)
# ax1.set_xlim(0,1)

# ax1.text(0.3, 0.26, 'RS(4,3)', fontsize=20)

# # ax1.hlines(0.35, 0.16, 0.56, colors='black', lw=3)
# ax1.hlines(0.35, 0.16, 0.29, colors='black', lw=3)
# ax1.hlines(0.35, 0.43, 0.56, colors='black', lw=3)
# ax1.vlines(0.16, 0.23, 0.65, colors='black', lw=3)
# ax1.vlines(0.562, 0.23, 0.65, colors='black', lw=3)

# ax1.text(0.702, 0.26, 'RS(6,3)', fontsize=20)

# ax1.hlines(0.35, 0.562, 0.692, colors='black', lw=3)
# ax1.hlines(0.35, 0.832, 0.962, colors='black', lw=3)
# ax1.vlines(0.962, 0.23, 0.65, colors='black', lw=3)

plt.savefig('place365_transmission_time.pdf')
plt.show()
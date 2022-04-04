t="../../实验数据/smr/vmdk range 20"


import matplotlib.pyplot as  plt
import math
import numpy as np


def gen_target_data(file_name):
    new_file_name=file_name+".txt"
    x=[]
    y=[]
    z=[]
    f_result=open(new_file_name,"r")
    i=1
    for line in f_result.readlines():
        line=line.replace('\n','')
        a=line.split(":::::")
        x.append(int(a[1]))
        y.append(int(a[2]))
        z.append(i)
        i+=1

    return x,y,z

x,y,z=gen_target_data(t)


new_x=[]
new_y=[]
new_z=[]

for i in range(1,len(x),15):
    new_x.append(x[i])
    new_y.append(y[i])
    new_z.append(z[i]*(1.0*16998/12795))

labelArr = [
    "Select Range",
    "Selected",
]

colorDict = {
    "Select Range":"#324665",
    "Selected":"#F15326",
}

lineStyleDict = {
    "Select Range":"--",
    "Selected":"-",
}

dataArr = [
    [new_z,new_x],
    [new_z,new_y],
]

# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(9,6))

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='both')

scalNum = 5
scalFactor = 100000

#绘图
line_width = 2
for i in range(len(dataArr)):
    print(len(dataArr[i][0]))
    curMethod = labelArr[i]
    plt.plot(dataArr[i][0],[x/scalFactor for x in dataArr[i][1]],label=curMethod,color=colorDict[curMethod], \
        linestyle=lineStyleDict[curMethod],linewidth=line_width)

xmin, xmax, ymin, ymax = plt.axis()
plt.text(xmin-0.01*xmax, ymax*1.008, r'$\times10^{%d}$'%(scalNum),fontsize=20,ha='left')

#让图例生效
plt.legend(fontsize=23, loc='upper left', labelspacing=0.25,handletextpad=0.8, handlelength=1.5,ncol=1, columnspacing=0.8)

# plt.tick_params(labelsize=35)
plt.yticks(fontsize=22)
plt.xticks(fontsize=22)

#给坐标轴添加标签
plt.xlabel("Segment", fontsize=28)
plt.ylabel("Range to Select", fontsize=28)

# 设置图片边距
plt.subplots_adjust(top=0.945,bottom=0.135,left=0.116,right=0.96,hspace=0.2,wspace=0.2)

plt.savefig('../image/smr_vmdk_range.pdf')
plt.show()
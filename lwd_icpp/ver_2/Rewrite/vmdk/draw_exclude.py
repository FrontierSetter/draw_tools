t="../../过滤 vmdk 1000"


import matplotlib.pyplot as  plt
import math
import numpy as np


def gen_target_data(file_name):
    new_file_name=file_name+" new_result.txt"
    file_name+=".txt"

    count_item=["before","after"]
    dict1={}
    f = open(file_name, "r")
    for line in f.readlines():
        v=line.split(":")
        if len(v)>1:
            v[1] = v[1].replace('\n', '')
            v[1] = v[1].replace('/s', '')
            v[1] = v[1].replace(' ', '')
            v[1]=v[1].split(",")[0]
            if count_item.count(v[0])==1:
                if v[0] in dict1:
                    dict1[v[0]].append(v[1])
                else:
                    l=[]
                    dict1[v[0]] = l
                    dict1[v[0]].append(v[1])

    f_result=open(new_file_name,"w")
    for key,values in dict1.items():
        f_result.write(key+",")
        for l in values:
            f_result.write(l+",")
        f_result.write("\n")

    x=[]
    y=[]
    z=[]
    f_result=open(new_file_name,"r")
    for line in f_result.readlines():
        line=line.replace('\n','')
        a=line.split(",")
        if a[0]=="before":
            for b in range(1,len(a)-1):
                x.append(int(a[b]))
                z.append(b)
        if a[0]=="after":
            for b in range(1,len(a)-1):
                y.append(int(a[b]))

    return x,y,z

x,y,z=gen_target_data(t)


new_x=[]
new_y=[]
new_z=[]

for i in range(1,len(x),15):
    new_x.append(x[i])
    new_y.append(y[i])
    new_z.append(z[i])

labelArr = [
    "Before Exclusion",
    "After Exclusion",
]

colorDict = {
    "Before Exclusion":"#3478BF",
    "After Exclusion":"#F15326",
}

markerDict = {
    "Before Exclusion":"s",
    "After Exclusion":"d",
}

lineStyleDict = {
    "Before Exclusion":"--",
    "After Exclusion":"-",
}

dataArr = [
    [z,x],
    [z,y],
]

import sys
sys.path.append("..\\header")
from marker import *

# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(9,6))

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='both')

scalNum = 5
scalFactor = 100000
sampleGap = 15

#绘图
line_width = 2
for i in range(len(dataArr)):
    print(len(dataArr[i][0]))
    curMethod = labelArr[i]
    plt.plot([dataArr[i][0][idx] for idx in range(0, len(dataArr[i][0]), sampleGap)],[dataArr[i][1][idx]/scalFactor for idx in range(0, len(dataArr[i][1]), sampleGap)],label=curMethod,color=colorDict[curMethod], \
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

plt.savefig('../image/vmdk_exclude.pdf')
plt.show()
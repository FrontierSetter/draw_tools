t="../../实验数据/过滤 linux 1000"


import matplotlib.pyplot as  plt
import math
import numpy as np


def gen_target_data(file_name):
    new_file_name=file_name+" new_result.txt"
    file_name+=".txt"

    count_item=["before","after","selected fingerprint"]
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
    s=[]
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
        if a[0]=="selected fingerprint":
            for b in range(1,len(a)-1):
                s.append(int(a[b]))
    return x,y,s,z

x,y,s,z=gen_target_data(t)

labelArr = [
    "Before Exclusion",
    "After Exclusion",
    "Selected",
]

colorDict = {
    "Before Exclusion":"#324665",
    "After Exclusion":"#EED777",
    "Selected":"#F15326",
}

markerDict = {
    "Before Exclusion":"",
    "After Exclusion":"s",
    "Selected":"d",
}

lineStyleDict = {
    "Before Exclusion":"--",
    "After Exclusion":"-.",
    "Selected":"-",
}

dataArr = [
    [z,x],
    [z,y],
    [z,s],
]

# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(9,6))

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='both')

scalNum = 5
scalFactor = 100000

import sys
sys.path.append("..\\..\\..\\..\\general\\header")
from marker import *

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

# plt.xlim(right=1500)

# 设置图片边距
plt.subplots_adjust(top=0.945,bottom=0.135,left=0.116,right=0.96,hspace=0.2,wspace=0.2)

plt.savefig('../image/linux_exclude.pdf')
plt.show()
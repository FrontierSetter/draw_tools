t100="../../new method/版本/vmdk t 100"
t300="../../new method/版本/vmdk t 300"
t500="../../new method/版本/vmdk t 500"
t700="../../new method/版本/vmdk t 700"
t900="../../new method/版本/vmdk t 900"


import matplotlib.pyplot as  plt
import math
import sys

def gen_target_data(file_name):
    new_file_name=file_name+" new_result.txt"
    file_name+=".txt"

    count_item=["backup version","speed_factor"]
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
    f_result=open(new_file_name,"r")
    for line in f_result.readlines():
        line=line.replace('\n','')
        a=line.split(",")
        if a[0]=="backup version":
            for b in range(1,len(a)-1):
                x.append(int(a[b]))
        if a[0]=="speed_factor":
            for b in range(1,len(a)-1):
                y.append(float(a[b]))
    return x,y

fileArr = [
    t100,
    t300,
    t500,
    t700,
    t900,
]

labelArr = [
    "threshold-100",
    "threshold-300",
    "threshold-500",
    "threshold-700",
    "threshold-900",
]

colorDict = {
    "threshold-100":"#324665",
    "threshold-300":"#3478BF",
    "threshold-500":"#40A776",
    "threshold-700":"#F15326",
    "threshold-900":"#EED777",
}

markerDict = {
    "threshold-100":"s",
    "threshold-300":"o",
    "threshold-500":"^",
    "threshold-700":"d",
    "threshold-900":"v",
}

dataArr = []
for i in range(len(fileArr)):
    dataArr.append(gen_target_data(fileArr[i]))

sys.path.append("..\\header")
from marker import *

# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(12,6))

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='both')

#绘图
line_width = 4
for i in range(len(dataArr)):
    print(len(dataArr[i][0]))
    curMethod = labelArr[i]
    plt.plot(dataArr[i][0],dataArr[i][1],label=curMethod,color=colorDict[curMethod], \
        marker=markerDict[curMethod],markersize=16,markevery=getMarkerArr(len(dataArr[i][0]), 17),linewidth=line_width)

#让图例生效
plt.legend(fontsize=23, loc='lower left', labelspacing=0.25, handlelength=1.5)

# plt.tick_params(labelsize=35)
plt.yticks(fontsize=22)
plt.xticks(fontsize=22)

#给坐标轴添加标签
plt.xlabel("Backup Version", fontsize=28)
plt.ylabel("Speed Factor", fontsize=28)

# plt.ylim(0)

# 设置图片边距
plt.subplots_adjust(top=0.995,bottom=0.135,left=0.086,right=0.995,hspace=0.2,wspace=0.2)

plt.savefig('../image/vmdk_backup.pdf')

plt.show()
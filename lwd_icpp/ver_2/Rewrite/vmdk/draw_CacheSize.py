t10="../../new method/cache size/vmdk t10"
t50="../../new method/cache size/vmdk t50"
t100="../../new method/cache size/vmdk t100"
t200="../../new method/cache size/vmdk t200"
t400="../../new method/cache size/vmdk t400"
t600="../../new method/cache size/vmdk t600"

total_size=1425021009920
unique_size=73993850880

import matplotlib.pyplot as  plt
import math
import numpy as np


def gen_target_data(file_name):
    new_file_name=file_name+" new_result.txt"
    file_name+=".txt"

    count_item=["lru_num","readContainerNum_lru"]
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
        if a[0]=="lru_num":
            for b in range(1,len(a)-1):
                x.append(a[b])
        if a[0]=="readContainerNum_lru":
            for b in range(1,len(a)-1):
                y.append(total_size / (1024.0 * 1024 * int(a[b])))
    return x,y

fileArr = [
    t10,
    t50,
    t100,
    t200,
    t400,
    t600
]

labelArr = [
    "threshold-10",
    "threshold-50",
    "threshold-100",
    "threshold-200",
    "threshold-400",
    "threshold-600",
]

colorDict = {
    "threshold-10":"#324665",
    "threshold-50":"#3478BF",
    "threshold-100":"#40A776",
    "threshold-200":"#F15326",
    "threshold-400":"#EED777",
    "threshold-600":"#8064A2",
}

markerDict = {
    "threshold-10":"s",
    "threshold-50":"o",
    "threshold-100":"^",
    "threshold-200":"d",
    "threshold-400":"v",
    "threshold-600":"<",
}

dataArr = []
for i in range(len(fileArr)):
    dataArr.append(gen_target_data(fileArr[i]))

# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(9,6))

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='both')

#绘图
line_width = 4
for i in range(len(dataArr)):
    print(len(dataArr[i][0]))
    curMethod = labelArr[i]
    plt.plot(dataArr[i][0],dataArr[i][1],label=curMethod,color=colorDict[curMethod], \
        marker=markerDict[curMethod],markersize=16,markevery=None,linewidth=line_width)

#让图例生效
plt.legend(fontsize=21, loc='lower right', bbox_to_anchor=(1.021, -0.02),\
     labelspacing=0.25, handlelength=1.5,ncol=2, columnspacing=0.6)

# plt.tick_params(labelsize=35)
plt.yticks(fontsize=22)
plt.xticks(fontsize=22)

#给坐标轴添加标签
plt.xlabel("Cache Size", fontsize=28)
plt.ylabel("Speed Factor", fontsize=28)

plt.ylim(0)

# 设置图片边距
plt.subplots_adjust(top=0.995,bottom=0.135,left=0.116,right=0.995,hspace=0.2,wspace=0.2)

plt.savefig('../image/vmdk_cache_size.pdf')
plt.show()
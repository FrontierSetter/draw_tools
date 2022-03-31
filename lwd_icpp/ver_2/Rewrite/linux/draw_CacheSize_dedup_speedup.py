t10="../../new method/cache size/linux t10"
t50="../../new method/cache size/linux t50"
t100="../../new method/cache size/linux t100"
t200="../../new method/cache size/linux t200"
t400="../../new method/cache size/linux t400"
t600="../../new method/cache size/linux t600"

total_size=100021823518
unique_size=2581046673

import matplotlib.pyplot as  plt
import math
import numpy as np
x=[]
y=[]
t=[]
def gen_target_data(file_name):
    new_file_name=file_name+" new_result.txt"
    file_name+=".txt"

    count_item=["lru_num","readContainerNum_lru","rewritesize"]
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

    f_result=open(new_file_name,"r")
    for line in f_result.readlines():
        line=line.replace('\n','')
        a=line.split(",")
        if a[0]=="lru_num":
            for b in range(1,len(a)-1):
                t.append(int(a[b]))
        if a[0]=="readContainerNum_lru":
            for b in range(1,len(a)-1):
                x.append(total_size / (1024.0 * 1024 * int(a[b])))
        if a[0]=="rewritesize":
            for b in range(1,len(a)-1):
                y.append(total_size /(int(a[b])+unique_size))

gen_target_data(t10)
gen_target_data(t50)
gen_target_data(t100)
gen_target_data(t200)
gen_target_data(t400)
gen_target_data(t600)

x_10=[]
y_10=[]
x_20=[]
y_20=[]
x_30=[]
y_30=[]
x_40=[]
y_40=[]
x_50=[]
y_50=[]
x_60=[]
y_60=[]
x_70=[]
y_70=[]
for b in range(0,len(t)):
    if t[b]==10:
        x_10.append(x[b])
        y_10.append(y[b])
    elif t[b]==20:
        x_20.append(x[b])
        y_20.append(y[b])
    elif t[b]==30:
        x_30.append(x[b])
        y_30.append(y[b])
    elif t[b]==40:
        x_40.append(x[b])
        y_40.append(y[b])
    elif t[b]==50:
        x_50.append(x[b])
        y_50.append(y[b])
    elif t[b]==60:
        x_60.append(x[b])
        y_60.append(y[b])
    elif t[b]==70:
        x_70.append(x[b])
        y_70.append(y[b])

labelArr = [
    "cache-size-10",
    "cache-size-20",
    "cache-size-30",
    "cache-size-40",
    "cache-size-50",
    "cache-size-60",
    "cache-size-70",
]

colorDict = {
    "cache-size-10":"#324665",
    "cache-size-20":"#3478BF",
    "cache-size-30":"#40A776",
    "cache-size-40":"#F15326",
    "cache-size-50":"#EED777",
    "cache-size-60":"#8064A2",
    "cache-size-70":"#EC6568"
}

markerDict = {
    "cache-size-10":"s",
    "cache-size-20":"o",
    "cache-size-30":"^",
    "cache-size-40":"d",
    "cache-size-50":"v",
    "cache-size-60":"<",
    "cache-size-70":">",
}

dataArr = [
    [x_10,y_10],
    [x_20,y_20],
    [x_30,y_30],
    [x_40,y_40],
    [x_50,y_50],
    [x_60,y_60],
    # [x_70,y_70],
]

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
plt.legend(fontsize=23, loc='lower left', labelspacing=0.25,handletextpad=0.8, handlelength=1.5,ncol=1, columnspacing=0.8)

# plt.tick_params(labelsize=35)
plt.yticks(fontsize=22)
plt.xticks(fontsize=22)

#给坐标轴添加标签
plt.xlabel("Speed Factor", fontsize=28)
plt.ylabel("Deduplication Ratio", fontsize=28)

plt.ylim(top=40.5)
plt.xlim(right = 3.31)

# 设置图片边距
plt.subplots_adjust(top=0.995,bottom=0.135,left=0.116,right=0.995,hspace=0.2,wspace=0.2)

plt.savefig('../image/linux_cache.pdf')
plt.show()
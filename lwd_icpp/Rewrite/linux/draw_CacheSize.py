t10="F:/论文/实验数据/new method/cache size/linux t10"
t50="F:/论文/实验数据/new method/cache size/linux t50"
t100="F:/论文/实验数据/new method/cache size/linux t100"
t200="F:/论文/实验数据/new method/cache size/linux t200"
t400="F:/论文/实验数据/new method/cache size/linux t400"
t600="F:/论文/实验数据/new method/cache size/linux t600"

total_size=100021823518
unique_size=2581046673

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

x_10,y_10=gen_target_data(t10)
x_50,y_50=gen_target_data(t50)
x_100,y_100=gen_target_data(t100)
x_200,y_200=gen_target_data(t200)
x_400,y_400=gen_target_data(t400)
x_600,y_600=gen_target_data(t600)

plt.figure(figsize=(19,11))
#设置线宽
plt.plot(x_10,y_10,label=u'threshold 10',linewidth=7)
plt.plot(x_50,y_50,label=u'threshold 50',linewidth=7)
plt.plot(x_100,y_100,label=u'threshold 100',linewidth=7)
plt.plot(x_200,y_200,label=u'threshold 200',linewidth=7)
plt.plot(x_400,y_400,label=u'threshold 400',linewidth=7)
plt.plot(x_600,y_600,label=u'threshold 600',linewidth=7)

font={
    'family':'Times New Roman',
    'weight':'normal',
    'size':30
}

#让图例生效
plt.legend(prop=font,frameon=False,loc='lower right')

plt.tick_params(labelsize=35)


#设置图表标题，并给坐标轴添加标签
plt.xlabel("Cache Size",fontsize=40)
plt.ylabel("Speed Factor",fontsize=40)
plt.yticks(np.arange(0.5, 3.1, 0.5))
plt.savefig('../image/linux_cache_size.png')
plt.show()
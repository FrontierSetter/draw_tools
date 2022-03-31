t="../../过滤 chromiun 1000"


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


plt.figure(figsize=(19,11))
#设置线宽
plt.plot(z,x,label=u'Before Exclusion',linewidth=2)
plt.plot(z,y,label=u'After Exclusion',linewidth=2)

font={
    'family':'Times New Roman',
    'weight':'normal',
    'size':30
}

#让图例生效
plt.legend(prop=font,frameon=False,loc='upper left')

plt.tick_params(labelsize=35)


#设置图表标题，并给坐标轴添加标签
plt.xlabel("Segment",fontsize=40)
plt.ylabel("Range to Select",fontsize=40)
plt.savefig('../image/chromiun_exclude.png')
plt.show()
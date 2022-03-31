t10="../../new method/cache size/vmdk t10"
#t50="../../new method/cache size/vmdk t50"
t100="../../new method/cache size/vmdk t100"
t200="../../new method/cache size/vmdk t200"
t400="../../new method/cache size/vmdk t400"
t600="../../new method/cache size/vmdk t600"

total_size=1425021009920
unique_size=73993850880

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
#gen_target_data(t50)
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




plt.figure(figsize=(19,11))
#设置线宽
plt.plot(x_10,y_10,label=u'cache size 10',linewidth=7)
plt.plot(x_20,y_20,label=u'cache size 20',linewidth=7)
plt.plot(x_30,y_30,label=u'cache size 30',linewidth=7)
plt.plot(x_40,y_40,label=u'cache size 40',linewidth=7)
plt.plot(x_50,y_50,label=u'cache size 50',linewidth=7)
plt.plot(x_60,y_60,label=u'cache size 60',linewidth=7)



font={
    'family':'Times New Roman',
    'weight':'normal',
    'size':30
}

#让图例生效
plt.legend(prop=font,frameon=False,loc='lower left')

plt.tick_params(labelsize=35)


#设置图表标题，并给坐标轴添加标签
plt.xlabel("Speed Factor",fontsize=40)
plt.ylabel("Deduplication Ratio",fontsize=40)
plt.savefig('../image/vmdk_cache.png')
plt.show()
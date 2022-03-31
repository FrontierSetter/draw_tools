capping_file_name="../../capping/vmdk new_result.txt"
fcapping_file_name="../../fcapping/vmdk 1 new_result.txt"
smr_file_name="../../smr/vmdk 1-100 new_result.txt"
mine_file_name="../../new method/vmdk new_result.txt"

import matplotlib.pyplot as  plt
import numpy as np
total_size=1425021009920
unique_size=73993850880

x=[]
y=[]
f_result=open(mine_file_name,"r")
for line in f_result.readlines():
    line=line.replace('\n','')
    a=line.split(",")
    if a[0]=="rewrite_time":
        for b in range(1,len(a)-1):#第一个是字符，最后一个是','
            x.append(float(a[b])+30)
    if a[0]=="readContainerNum_lru":
        for b in range(1,len(a)-1):
            y.append(float(a[b]))


new_rewrite_time=[]
new_read_containter=[]
new_speed_factor=[]
#过滤
for i in range(0,len(x)):
    if len(new_rewrite_time)>0:
        if y[i]<new_read_containter[-1]:
            new_rewrite_time.append(x[i])
            new_read_containter.append(y[i])
            new_speed_factor.append(total_size / (1024.0 * 1024 * y[i]))
    else:
        new_rewrite_time.append(x[i])
        new_read_containter.append(y[i])
        new_speed_factor.append(total_size / (1024.0 * 1024 * y[i]))


max_read_container=new_read_containter[0]
min_read_container=new_read_containter[-1]



x=[]
y=[]
f_result=open(capping_file_name,"r")
for line in f_result.readlines():
    line=line.replace('\n','')
    a=line.split(",")
    if a[0]=="read_container_num":
        for b in range(1,len(a)-1):#第一个是字符，最后一个是','
            y.append(float(a[b]))
    if a[0]=="rewrite_time ":
        for b in range(1,len(a)-1):
            x.append(float(a[b]))


capping_rewrite_time=[]
capping_read_container=[]
capping_speed_factor=[]
#过滤
for i in range(0,len(x)):
    if y[i] >= min_read_container and y[i] <= max_read_container:
        capping_rewrite_time.append(x[i])
        capping_read_container.append(y[i])
        capping_speed_factor.append(total_size / (1024.0 * 1024 * y[i]))

x=[]
y=[]
f_result=open(smr_file_name,"r")
for line in f_result.readlines():
    line=line.replace('\n','')
    a=line.split(",")
    if a[0]=="read_container_num":
        for b in range(1,len(a)-1):#第一个是字符，最后一个是','
            y.append(float(a[b]))
    if a[0]=="rewrite_time ":
        for b in range(1,len(a)-1):
            x.append(float(a[b]))


smr_rewrite_time=[]
smr_read_container=[]
smr_speed_factor=[]
#过滤
for i in range(0,len(x)):
    if y[i] >= min_read_container and y[i] <= max_read_container:
        smr_rewrite_time.append(x[i])
        smr_read_container.append(y[i])
        smr_speed_factor.append(total_size / (1024.0 * 1024 * y[i]))



x=[]
y=[]
z=[]
f_result=open(fcapping_file_name,"r")
for line in f_result.readlines():
    line=line.replace('\n','')
    a=line.split(",")
    if a[0]=="read_container_num":
        for b in range(1,len(a)-1):#第一个是字符，最后一个是','
            y.append(int(a[b]))
    if a[0]=="rewrite_time ":
        for b in range(1,len(a)-1):
            x.append(float(a[b]))
    if a[0]=="rewrite_chunk_size":
        for b in range(1,len(a)-1):
            z.append(int(a[b]))

choose_off=[]

now_flag=z[0]
now_value=y[0]
now_off=0
for h in range(0,len(z)):
    if z[h]==now_flag and now_value > y[h]:
        now_value=y[h]
        now_off=h
    elif z[h]!=now_flag:
        choose_off.append(now_off)
        now_flag = z[h]
        now_value = y[h]
        now_off = h

fcapping_rewrite_time=[]
fcapping_read_container=[]
fcapping_speed_factor=[]
#过滤
for i in range(0,len(x)):
    if y[i] >= min_read_container and y[i] <= max_read_container:
        if choose_off.count(i)==1:
            if len(fcapping_read_container)>1:
                if y[i] < fcapping_read_container[-1]:
                    fcapping_rewrite_time.append(x[i])
                    fcapping_read_container.append(y[i])
                    fcapping_speed_factor.append(total_size / (1024.0 * 1024 * y[i]))
            else:
                fcapping_rewrite_time.append(x[i])
                fcapping_read_container.append(y[i])
                fcapping_speed_factor.append(total_size / (1024.0 * 1024 * y[i]))


labelArr = [
    "Capping",
    "SMR",
    "FCRC",
    "ERP",
]

colorDict = {
    "Capping":"#324665",
    "SMR":"#3478BF",
    "FCRC":"#40A776",
    "ERP":"#F15326",
}

markerDict = {
    "Capping":"s",
    "SMR":"o",
    "FCRC":"^",
    "ERP":"d",
}

dataArr = [
    [capping_speed_factor,capping_rewrite_time],
    [smr_speed_factor,smr_rewrite_time],
    [fcapping_speed_factor,fcapping_rewrite_time],
    [new_speed_factor,new_rewrite_time],
]

import sys
sys.path.append("..\\header")
from marker import *

# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(9,6))

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='both')

scalNum = 4
scalFactor = 10000

#绘图
line_width = 4
for i in range(len(dataArr)):
    print(len(dataArr[i][0]))
    curMethod = labelArr[i]
    plt.plot(dataArr[i][0],[x/scalFactor for x in dataArr[i][1]],label=curMethod,color=colorDict[curMethod], \
        marker=markerDict[curMethod],markersize=16,markevery=getMarkerArr(len(dataArr[i][0]), 15),linewidth=line_width)

xmin, xmax, ymin, ymax = plt.axis()
plt.text(xmin-0.04*xmax, ymax*1.008, r'$\times10^{%d}$'%(scalNum),fontsize=20,ha='left')

#让图例生效
plt.legend(fontsize=23, loc='upper left', labelspacing=0.25, handlelength=1.5)

# plt.tick_params(labelsize=35)
plt.yticks(fontsize=22)
plt.xticks(np.arange(0.5, 4.2, 0.5), fontsize=22)

#给坐标轴添加标签
plt.xlabel("Speed Factor", fontsize=28)
plt.ylabel("Rewrite Time (s)", fontsize=28)

plt.xlim(0.4, 4.2)
plt.ylim(top=8)

# 设置图片边距
plt.subplots_adjust(top=0.95,bottom=0.135,left=0.126,right=0.995,hspace=0.2,wspace=0.2)

plt.savefig('../image/vmdk_rewrite_time.pdf')

plt.show()
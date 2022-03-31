capping_file_name="../../capping/chromiun new_result.txt"
smr_file_name="../../smr/chromiun 1-100 new_result.txt"
mine_file_name="../../new method/chromiun new_result.txt"
fcapping_file_name="../../fcapping/chromiun 1 new_result.txt"


total_size=96912415330
unique_size=6923605512

import matplotlib.pyplot as  plt
import math
import numpy as np
new_point=[2,5,10,30,50,75,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000]

xx=[]
yy=[]
tt=[]
f_result=open(mine_file_name,"r")
for line in f_result.readlines():
    line=line.replace('\n','')
    a=line.split(",")
    if a[0]=="rewritesize":
        for b in range(1,len(a)-1):
            xx.append(1.0*total_size/(int(a[b])+unique_size))
    if a[0]=="readContainerNum_lru":
        for b in range(1,len(a)-1):
            yy.append(int(a[b]))
    if a[0]=="threshold":
        for b in range(1,len(a)-1):
            tt.append(int(a[b]))
x=[]
y=[]
t_index=0
for i in range(0,len(tt)):
    if tt[i]==new_point[t_index]:
        x.append(xx[i])
        y.append(yy[i])
        t_index+=1
    if t_index==len(tt):
        break

new_rewrite_chunk=[]
new_read_containter=[]
new_speed_factor=[]
#过滤
for i in range(0,len(x)):
    if len(new_read_containter) > 1:  # 必须是降序的，不然会有很多的交叉
        if y[i] < new_read_containter[-1] and x[i] < new_rewrite_chunk[-1]:
            new_rewrite_chunk.append(x[i])
            new_read_containter.append(y[i])
            new_speed_factor.append(total_size / (1024.0 * 1024 * y[i]))
    else:
        new_rewrite_chunk.append(x[i])
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
            y.append(int(a[b]))
    if a[0]=="size of rewritten chunks":
        for b in range(1,len(a)-1):
            x.append(1.0*total_size/(int(a[b])+unique_size))


capping_rewrite_chunk=[]
capping_read_container=[]
capping_speed_factor=[]
#过滤
for i in range(0,len(x)):
    if y[i]>=min_read_container and y[i]<=max_read_container:
        capping_rewrite_chunk.append(x[i])
        capping_read_container.append(y[i])
        capping_speed_factor.append(total_size / (1024.0 * 1024 * y[i]))


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
    if a[0]=="size of rewritten chunks":
        for b in range(1,len(a)-1):
            x.append(1.0*total_size/(int(a[b])+unique_size))
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
    elif z[h]==now_flag and h==len(z)-1:
        choose_off.append(now_off)

fcapping_rewrite_chunk=[]
fcapping_read_container=[]
fcapping_speed_factor=[]
#过滤
for i in range(0,len(x)):
    if y[i] >= min_read_container and y[i] <= max_read_container:
        if choose_off.count(i)==1:
            if len(fcapping_read_container)>1:#必须是降序的，不然会有很多的交叉
                if y[i] < fcapping_read_container[-1] and x[i]< fcapping_rewrite_chunk[-1]:
                    fcapping_rewrite_chunk.append(x[i])
                    fcapping_read_container.append(y[i])
                    fcapping_speed_factor.append(total_size / (1024.0 * 1024 * y[i]))
            else:
                fcapping_rewrite_chunk.append(x[i])
                fcapping_read_container.append(y[i])
                fcapping_speed_factor.append(total_size / (1024.0 * 1024 * y[i]))

x=[]
y=[]
f_result=open(smr_file_name,"r")
for line in f_result.readlines():
    line=line.replace('\n','')
    a=line.split(",")
    if a[0]=="read_container_num":
        for b in range(1,len(a)-1):#第一个是字符，最后一个是','
            y.append(int(a[b]))
    if a[0]=="size of rewritten chunks":
        for b in range(1,len(a)-1):
            x.append(1.0*total_size/(int(a[b])+unique_size))

smr_rewrite_chunk=[]
smr_read_container=[]
smr_speed_factor=[]
#过滤
for i in range(0,len(x)):
    if y[i] >= min_read_container and y[i] <= max_read_container:
        smr_rewrite_chunk.append(x[i])
        smr_read_container.append(y[i])
        smr_speed_factor.append(total_size / (1024.0 * 1024 * y[i]))

#for i in range(0,len(capping_rewrite_chunk)):
#    capping_rewrite_chunk[i]=math.log(capping_rewrite_chunk[i])

#for i in range(0,len(fcapping_rewrite_chunk)):
#    fcapping_rewrite_chunk[i]=math.log(fcapping_rewrite_chunk[i])

#for i in range(0,len(smr_rewrite_chunk)):
#    smr_rewrite_chunk[i]=math.log(smr_rewrite_chunk[i])

#for i in range(0,len(new_rewrite_chunk)):
#    new_rewrite_chunk[i]=math.log(new_rewrite_chunk[i])

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
    [capping_speed_factor,capping_rewrite_chunk],
    [smr_speed_factor,smr_rewrite_chunk],
    [fcapping_speed_factor,fcapping_rewrite_chunk],
    [new_speed_factor,new_rewrite_chunk],
]

import sys
sys.path.append("..\\header")
from marker import *

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
        marker=markerDict[curMethod],markersize=16,markevery=getMarkerArr(len(dataArr[i][0]), 15),linewidth=line_width)

#让图例生效
plt.legend(fontsize=23, loc='lower left', labelspacing=0.25, handlelength=1.5)

# plt.tick_params(labelsize=35)
plt.yticks(fontsize=22)
plt.xticks(np.arange(1.5, 3.7, 0.25), fontsize=22)

#给坐标轴添加标签
plt.xlabel("Speed Factor", fontsize=28)
plt.ylabel("Deduplication Ratio", fontsize=28)

plt.ylim(0)

# 设置图片边距
plt.subplots_adjust(top=0.995,bottom=0.135,left=0.116,right=0.995,hspace=0.2,wspace=0.2)

plt.savefig('../image/chromiun_dedup.pdf')

plt.show()
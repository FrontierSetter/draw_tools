capping_file_name="../../capping/gcc new_result.txt"
smr_file_name="../../smr/gcc 1-100 new_result.txt"
mine_file_name="../../new method/gcc new_result.txt"
fcapping_file_name="../../fcapping/gcc 1 new_result.txt"


total_size=39794111305
unique_size=9002549528

import matplotlib.pyplot as  plt
import math
import numpy as np

x=[]
y=[]
f_result=open(mine_file_name,"r")
for line in f_result.readlines():
    line=line.replace('\n','')
    a=line.split(",")
    if a[0]=="rewritesize":
        for b in range(1,len(a)-1):
            x.append(1.0*total_size/(int(a[b])+unique_size))
    if a[0]=="readContainerNum_lru":
        for b in range(1,len(a)-1):
            y.append(int(a[b]))
print(len(x))

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


plt.figure(figsize=(19,11))
#设置线宽
plt.plot(capping_speed_factor,capping_rewrite_chunk,label=u'Capping',linewidth=7)
plt.plot(smr_speed_factor,smr_rewrite_chunk,label=u'SMR',linewidth=7)
plt.plot(fcapping_speed_factor,fcapping_rewrite_chunk,label=u'FCRC',linewidth=7)
plt.plot(new_speed_factor,new_rewrite_chunk,label=u'ERP',linewidth=7)


font={
    'family':'Times New Roman',
    'weight':'normal',
    'size':40
}

#让图例生效
plt.legend(prop=font,frameon=False,loc='lower left')

plt.tick_params(labelsize=35)

#设置图表标题，并给坐标轴添加标签
plt.xlabel("Speed Factor",fontsize=40)
plt.ylabel("Deduplication Ratio",fontsize=40)

plt.yticks(np.arange(0, 6, 1))
plt.xticks(np.arange(1, 3.1, 0.5))
plt.savefig('../image/gcc_dedup.png')
plt.show()
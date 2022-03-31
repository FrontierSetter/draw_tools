capping_file_name="../../capping/gcc new_result.txt"
fcapping_file_name="../../fcapping/gcc 1 new_result.txt"
smr_file_name="../../smr/gcc 1-100 new_result.txt"
mine_file_name="../../new method/gcc new_result.txt"


total_size=39794111305
max_near=400

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
        for b in range(1,len(a)-1):#第一个是字符，最后一个是','
            x.append(int(a[b]))
    if a[0]=="readContainerNum_lru":
        for b in range(1,len(a)-1):
            y.append(int(a[b]))


new_rewrite_chunk=[]
new_read_containter=[]
new_speed_factor=[]
#过滤
for i in range(0,len(x)):
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
            x.append(int(a[b]))


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
            x.append(int(a[b]))
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
                if y[i] < fcapping_read_container[-1] and x[i]> fcapping_rewrite_chunk[-1]:
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
            x.append(int(a[b]))


smr_rewrite_chunk=[]
smr_read_container=[]
smr_speed_factor=[]
#过滤
for i in range(0,len(x)):
    if y[i] >= min_read_container and y[i] <= max_read_container:
        smr_rewrite_chunk.append(x[i])
        smr_read_container.append(y[i])
        smr_speed_factor.append(total_size / (1024.0 * 1024 * y[i]))

smr_improve_read_container=[]
smr_improve_precent=[]
smr_improve_speed_factor=[]

capping_improve_read_container=[]
capping_improve_precent=[]
capping_improve_speed_factor=[]

fcapping_improve_read_container=[]
fcapping_improve_precent=[]
fcapping_improve_speed_factor=[]

print(fcapping_read_container)
print(fcapping_rewrite_chunk)
#当前数据量较少，通过遍历应该可以
#找当前可以比较的container
for i in range(len(new_read_containter)-1,-1,-1):
    near_value=max_near #不能超过这个阈值的最接近的距离
    near_off=-1
    for j in range(0,len(capping_read_container)):
        if new_read_containter[i]-capping_read_container[j]<near_value and new_read_containter[i]-capping_read_container[j] >=0 :
            near_value=new_read_containter[i]-capping_read_container[j]
            near_off=j

    if near_off!=-1:
        p=1.0*(capping_rewrite_chunk[near_off]-new_rewrite_chunk[i])/capping_rewrite_chunk[near_off]
        capping_improve_precent.append(p)
        capping_improve_read_container.append(new_read_containter[i])
        capping_read_container[near_off]=-1
        capping_improve_speed_factor.append(new_speed_factor[i])

    near_value=max_near #不能超过这个阈值的最接近的距离
    near_off=-1
    for j in range(0,len(smr_read_container)):
        if new_read_containter[i]-smr_read_container[j]<near_value and new_read_containter[i]-smr_read_container[j] >=0 :
            near_value=new_read_containter[i]-smr_read_container[j]
            near_off=j

    if near_off!=-1:
        p=1.0*(smr_rewrite_chunk[near_off]-new_rewrite_chunk[i])/smr_rewrite_chunk[near_off]
        smr_improve_precent.append(p)
        smr_improve_read_container.append(new_read_containter[i])
        smr_read_container[near_off]=-1
        smr_improve_speed_factor.append(new_speed_factor[i])


    near_value=max_near #不能超过这个阈值的最接近的距离
    near_off=-1
    for j in range(0,len(fcapping_read_container)):
        if new_read_containter[i]-fcapping_read_container[j]<near_value and new_read_containter[i]-fcapping_read_container[j] >=0 :
            near_value=new_read_containter[i]-fcapping_read_container[j]
            near_off=j

    if near_off!=-1:
        p=1.0*(fcapping_rewrite_chunk[near_off]-new_rewrite_chunk[i])/fcapping_rewrite_chunk[near_off]
        fcapping_improve_precent.append(p)
        fcapping_improve_read_container.append(new_read_containter[i])
        fcapping_read_container[near_off]=-1
        fcapping_improve_speed_factor.append(new_speed_factor[i])



def Get_Average(list):
    sum = 0

    for item in list:
        sum += item

    return sum/len(list)

def Get_Max(list):
    sum = -1

    for item in list:
        if item>sum:
            sum=item

    return sum

def Get_Min(list):
    sum = 10000

    for item in list:
        if item<sum:
            sum=item

    return sum


print(Get_Average(capping_improve_precent))
print(Get_Average(smr_improve_precent))
print(Get_Average(fcapping_improve_precent))

print(Get_Max(capping_improve_precent))
print(Get_Max(smr_improve_precent))
print(Get_Max(fcapping_improve_precent))

print(Get_Min(capping_improve_precent))
print(Get_Min(smr_improve_precent))
print(Get_Min(fcapping_improve_precent))

print(fcapping_improve_speed_factor)
print(fcapping_improve_precent)


print(capping_improve_speed_factor)
print(capping_improve_precent)

print(smr_improve_speed_factor)
print(smr_improve_precent)

plt.figure(figsize=(19,11))

#设置线宽
plt.plot(capping_improve_speed_factor,capping_improve_precent,label='Capping',linewidth=7)
plt.plot(smr_improve_speed_factor,smr_improve_precent,label='SMR',linewidth=7)
plt.plot(fcapping_improve_speed_factor,fcapping_improve_precent,label='FCRC',linewidth=7)

font={
    'family':'Times New Roman',
    'weight':'normal',
    'size':35
}

#让图例生效
plt.legend(prop=font,frameon=False,loc='lower left')

plt.tick_params(labelsize=35)

#设置图表标题，并给坐标轴添加标签
plt.xlabel("Speed Factor",fontsize=40)
plt.ylabel("Rewrite Size Reduction",fontsize=40)
plt.yticks(np.arange(0, 1.1, 0.2))
plt.xticks(np.arange(1, 3.1, 0.5))
plt.savefig('../image/gcc_improve.png')




plt.show()
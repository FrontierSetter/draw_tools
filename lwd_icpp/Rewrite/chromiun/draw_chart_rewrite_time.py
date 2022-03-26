capping_file_name="../../capping/chromiun new_result.txt"
fcapping_file_name="../../fcapping/chromiun 1 new_result.txt"
smr_file_name="../../smr/chromiun 1-100 new_result.txt"
mine_file_name="../../new method/chromiun new_result.txt"

import matplotlib.pyplot as  plt
import numpy as np
total_size=96912415330

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
    smr_rewrite_time.append(x[i])
    smr_read_container.append(y[i])
    smr_speed_factor.append(total_size / (1024.0 * 1024 * y[i]))

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
    new_rewrite_time.append(x[i])
    new_read_containter.append(y[i])
    new_speed_factor.append(total_size / (1024.0 * 1024 * y[i]))

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
    if z[h]==now_flag and now_value<y[h]:
        now_value=y[h]
        now_off=h
    elif z[h]!=now_flag:
        choose_off.append(now_off)
        now_flag = z[h]
        now_value = y[h]
        now_off = h
    elif z[h]==now_flag and h==len(z)-1:
        choose_off.append(now_off)
fcapping_rewrite_time=[]
fcapping_read_container=[]
fcapping_speed_factor=[]
#过滤
for i in range(0,len(x)):
    fcapping_rewrite_time.append(x[i])
    fcapping_read_container.append(y[i])
    fcapping_speed_factor.append(total_size / (1024.0 * 1024 * y[i]))



plt.figure(figsize=(19,11))
#设置线宽
plt.plot(capping_speed_factor,capping_rewrite_time,label=u'Capping',linewidth=7)
plt.plot(smr_speed_factor,smr_rewrite_time,label=u'SMR',linewidth=7)
plt.plot(fcapping_speed_factor,fcapping_rewrite_time,label=u'FCRC',linewidth=7)
plt.plot(new_speed_factor,new_rewrite_time,label=u'ERP',linewidth=7)


font={
    'family':'Times New Roman',
    'weight':'normal',
    'size':40
}

#让图例生效
plt.legend(prop=font,frameon=False,loc='upper left')

plt.tick_params(labelsize=35)


#设置图表标题，并给坐标轴添加标签
plt.xlabel("Speed Factor",fontsize=40)
plt.ylabel("Rewrite Time (s)",fontsize=40)
plt.savefig('../image/chromiun_rewrite_time.png')




plt.show()
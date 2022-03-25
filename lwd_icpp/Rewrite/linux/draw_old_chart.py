capping_file_name="F:/论文/实验数据/capping/linux 1-100 new_result.txt"
smr_file_name="F:/论文/实验数据/smr/linux 1-100 new_result.txt"
mine_file_name="F:/论文/实验数据/new method/linux new_result.txt"
fcapping_file_name="F:/论文/实验数据/fcapping/linux 1 new_result.txt"
old_file_name="F:/论文/实验数据/old method/linux new_result.txt"


import matplotlib.pyplot as plt
import math

x=[]
y=[]
f_result=open(old_file_name,"r")
for line in f_result.readlines():
    line=line.replace('\n','')
    a=line.split(",")
    if a[0]=="rewriteNum":
        for b in range(1,len(a)-1):#第一个是字符，最后一个是','
            x.append(int(a[b]))
    if a[0]=="readContainerNum_lru":
        for b in range(1,len(a)-1):
            y.append(int(a[b]))


old_rewrite_chunk=[]
old_read_containter=[]
#过滤
for i in range(0,len(x)):
    old_rewrite_chunk.append(x[i])
    old_read_containter.append(y[i])

max_read_container=old_read_containter[0]
min_read_container=old_read_containter[-1]



x=[]
y=[]
f_result=open(mine_file_name,"r")
for line in f_result.readlines():
    line=line.replace('\n','')
    a=line.split(",")
    if a[0]=="rewriteNum":
        for b in range(1,len(a)-1):#第一个是字符，最后一个是','
            x.append(int(a[b]))
    if a[0]=="readContainerNum_lru":
        for b in range(1,len(a)-1):
            y.append(int(a[b]))


new_rewrite_chunk=[]
new_read_containter=[]
#过滤
for i in range(0,len(x)):
    if y[i] >= min_read_container and y[i] <= max_read_container:
        new_rewrite_chunk.append(x[i])
        new_read_containter.append(y[i])

x=[]
y=[]
f_result=open(capping_file_name,"r")
for line in f_result.readlines():
    line=line.replace('\n','')
    a=line.split(",")
    if a[0]=="read_container_num":
        for b in range(1,len(a)-1):#第一个是字符，最后一个是','
            y.append(int(a[b]))
    if a[0]=="number of rewritten chunks":
        for b in range(1,len(a)-1):
            x.append(int(a[b]))


capping_rewrite_chunk=[]
capping_read_container=[]
#过滤
for i in range(0,len(x)):
    if y[i]>=min_read_container and y[i]<=max_read_container:
        capping_rewrite_chunk.append(x[i])
        capping_read_container.append(y[i])

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
    if a[0]=="number of rewritten chunks":
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
    if z[h]==now_flag and now_value<y[h]:
        now_value=y[h]
        now_off=h
    elif z[h]!=now_flag:
        choose_off.append(now_off)
        now_flag = z[h]
        now_value = y[h]
        now_off = h

fcapping_rewrite_chunk=[]
fcapping_read_container=[]
#过滤
for i in range(0,len(x)):
    if y[i] >= min_read_container and y[i] <= max_read_container:
        if choose_off.count(i)==1:
            fcapping_rewrite_chunk.append(x[i])
            fcapping_read_container.append(y[i])


x=[]
y=[]
f_result=open(smr_file_name,"r")
for line in f_result.readlines():
    line=line.replace('\n','')
    a=line.split(",")
    if a[0]=="read_container_num":
        for b in range(1,len(a)-1):#第一个是字符，最后一个是','
            y.append(int(a[b]))
    if a[0]=="number of rewritten chunks":
        for b in range(1,len(a)-1):
            x.append(int(a[b]))


smr_rewrite_chunk=[]
smr_read_container=[]
#过滤
for i in range(0,len(x)):
    if y[i] >= min_read_container and y[i] <= max_read_container:
        smr_rewrite_chunk.append(x[i])
        smr_read_container.append(y[i])



#设置线宽

for i in range(0,len(capping_rewrite_chunk)):
    capping_rewrite_chunk[i]=math.log(capping_rewrite_chunk[i])

for i in range(0,len(fcapping_rewrite_chunk)):
    fcapping_rewrite_chunk[i]=math.log(fcapping_rewrite_chunk[i])

for i in range(0,len(smr_rewrite_chunk)):
    smr_rewrite_chunk[i]=math.log(smr_rewrite_chunk[i])

for i in range(0,len(new_rewrite_chunk)):
    new_rewrite_chunk[i]=math.log(new_rewrite_chunk[i])

for i in range(0,len(old_rewrite_chunk)):
    old_rewrite_chunk[i]=math.log(old_rewrite_chunk[i])

plt.plot(capping_read_container,capping_rewrite_chunk,label=u'capping')
plt.plot(fcapping_read_container,fcapping_rewrite_chunk,label=u'fcapping')
plt.plot(smr_read_container,smr_rewrite_chunk,label=u'smr')
plt.plot(new_read_containter,new_rewrite_chunk,label=u'mine')
plt.plot(old_read_containter,old_rewrite_chunk,label=u'old')

#让图例生效
plt.legend()

#设置图表标题，并给坐标轴添加标签
plt.title("rewrite cost",fontsize=20)
plt.xlabel("read container numbers",fontsize=12)
plt.ylabel("rewrite chunk numbers",fontsize=12)


plt.show()
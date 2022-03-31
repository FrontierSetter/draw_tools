capping_file_name="../../capping/linux 1-100 new_result.txt"
smr_file_name="../../smr/linux 1-100 new_result.txt"
mine_file_name="../../new method/linux 1-386 new_result.txt"
fcapping_file_name="../../fcapping/linux 1 new_result.txt"

import matplotlib.pyplot as  plt





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
    if x[i]<1000000 and y[i]>45000 and y[i]< 55000:
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
    if x[i]<1000000 and y[i]>45000 and y[i]< 55000 and choose_off.count(i)==1:
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
    if x[i]<1000000 and y[i]>45000 and y[i]< 55000:
        smr_rewrite_chunk.append(x[i])
        smr_read_container.append(y[i])


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
    if x[i]<1000000 and y[i]>45000:
        new_rewrite_chunk.append(x[i])
        new_read_containter.append(y[i])

#设置线宽
plt.plot(capping_read_container,capping_rewrite_chunk,label=u'capping')
plt.plot(fcapping_read_container,fcapping_rewrite_chunk,label=u'fcapping')
plt.plot(smr_read_container,smr_rewrite_chunk,label=u'smr')
plt.plot(new_read_containter,new_rewrite_chunk,label=u'mine')

#让图例生效
plt.legend()

#设置图表标题，并给坐标轴添加标签
plt.title("rewrite cost",fontsize=20)
plt.xlabel("read container numbers",fontsize=12)
plt.ylabel("rewrite chunk numbers",fontsize=12)


plt.show()
t100="../../new method/版本/linux t 100"
t300="../../new method/版本/linux t 300"
t500="../../new method/版本/linux t 500"
t700="../../new method/版本/linux t 700"
t900="../../new method/版本/linux t 900"


import matplotlib.pyplot as  plt
import math


def gen_target_data(file_name):
    new_file_name=file_name+" new_result.txt"
    file_name+=".txt"

    count_item=["backup version","speed_factor"]
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
        if a[0]=="backup version":
            for b in range(1,len(a)-1):
                x.append(int(a[b]))
        if a[0]=="speed_factor":
            for b in range(1,len(a)-1):
                y.append(float(a[b]))
    return x,y

x_100,y_100=gen_target_data(t100)
x_300,y_300=gen_target_data(t300)
x_500,y_500=gen_target_data(t500)
x_700,y_700=gen_target_data(t700)
x_900,y_900=gen_target_data(t900)


plt.figure(figsize=(19,11))
#设置线宽
plt.plot(x_100,y_100,label=u'threshold 100',linewidth=7)
plt.plot(x_300,y_300,label=u'threshold 300',linewidth=7)
plt.plot(x_500,y_500,label=u'threshold 500',linewidth=7)
plt.plot(x_700,y_700,label=u'threshold 700',linewidth=7)
plt.plot(x_900,y_900,label=u'threshold 900',linewidth=7)

font={
    'family':'Times New Roman',
    'weight':'normal',
    'size':30
}


#让图例生效
plt.legend(prop=font,frameon=False,loc='lower left')

plt.tick_params(labelsize=35)

#设置图表标题，并给坐标轴添加标签
plt.xlabel("Backup Version",fontsize=40)
plt.ylabel("Speed Factor",fontsize=40)
plt.savefig('../image/linux_backup.png')



plt.show()
capping_name="../../capping/gcc.txt"
smr_name="../../smr/gcc 1-100.txt"
fcapping_name="../../fcapping/gcc 1.txt"
mine_name="../../new method/gcc.txt"
#old_name="../../old method/linux.txt"

capping_file_name="../../capping/gcc new_result.txt"
smr_file_name="../../smr/gcc 1-100 new_result.txt"
fcapping_file_name="../../fcapping/gcc 1 new_result.txt"
mine_file_name="../../new method/gcc new_result.txt"
#old_file_name="../../old method/linux new_result.txt"


count_item=["rewrite_capping_level","rewrite_time ","number of rewritten chunks","size of rewritten chunks","read_container_num"]

dict1={}
f = open(capping_name, "r")
for line in f.readlines():
    v=line.split(": ")
    if len(v)>1:
        v[1] = v[1].replace('\n', '')
        v[1] = v[1].replace('s', '')
        v[1]=v[1].split(",")[0]
        if count_item.count(v[0])==1:
            if v[0] in dict1:
                dict1[v[0]].append(v[1])
            else:
                l=[]
                dict1[v[0]] = l
                dict1[v[0]].append(v[1])

f_result=open(capping_file_name,"w")
for key,values in dict1.items():
    f_result.write(key+",")
    for l in values:
        f_result.write(l+",")
    f_result.write("\n")

count_item=["fixed_capping_level","rewrite_chunk_size","rewrite_time ","number of rewritten chunks","size of rewritten chunks","read_container_num"]

a=1
dict1={}
f = open(fcapping_name, "r")
for line in f.readlines():
    v=line.split(": ")
    if len(v)>1:
        if v[0]=="size of rewritten chunks" and a==1:
            a*=-1
        elif v[0]=="size of rewritten chunks" and a==-1:
            print(line)

        if v[0]=="read_container_num" and a==-1:
            a*=-1
        elif v[0]=="read_container_num" and a==1:
            print(line)

        v[1] = v[1].replace('\n', '')
        v[1] = v[1].replace('s', '')
        v[1]=v[1].split(",")[0]
        if count_item.count(v[0])==1:
            if v[0] in dict1:
                dict1[v[0]].append(v[1])
            else:
                l=[]
                dict1[v[0]] = l
                dict1[v[0]].append(v[1])


f_result=open(fcapping_file_name,"w")
for key,values in dict1.items():
    f_result.write(key+",")
    print(len(values))
    for l in values:
        f_result.write(l+",")
    f_result.write("\n")



count_item=["threshold","rewrite_time","rewriteNum","rewritesize","readContainerNum_lru"]
dict1={}
f = open(mine_name, "r")
for line in f.readlines():
    v=line.split(":")
    if len(v)>1:
        v[1] = v[1].replace('\n', '')
        v[1] = v[1].replace('/s', '')
        v[1]=v[1].split(",")[0]
        if count_item.count(v[0])==1:
            if v[0] in dict1:
                dict1[v[0]].append(v[1])
            else:
                l=[]
                dict1[v[0]] = l
                dict1[v[0]].append(v[1])

f_result=open(mine_file_name,"w")
for key,values in dict1.items():
    f_result.write(key+",")
    for l in values:
        f_result.write(l+",")
    f_result.write("\n")

'''
count_item=["threshold","rewrite_time","rewriteNum","rewritesize","readContainerNum_lru"]
dict1={}
f = open(old_name, "r")
for line in f.readlines():
    v=line.split(":")
    if len(v)>1:
        v[1] = v[1].replace('\n', '')
        v[1] = v[1].replace('/s', '')
        v[1]=v[1].split(",")[0]
        if count_item.count(v[0])==1:
            if v[0] in dict1:
                dict1[v[0]].append(v[1])
            else:
                l=[]
                dict1[v[0]] = l
                dict1[v[0]].append(v[1])

f_result=open(old_file_name,"w")
for key,values in dict1.items():
    f_result.write(key+",")
    for l in values:
        f_result.write(l+",")
    f_result.write("\n")

'''
count_item=["rewrite_smr_level","rewrite_time ","number of rewritten chunks","size of rewritten chunks","read_container_num"]

dict1={}
f = open(smr_name, "r")
for line in f.readlines():
    v=line.split(": ")
    if len(v)>1:
        v[1] = v[1].replace('\n', '')
        v[1] = v[1].replace('s', '')
        v[1]=v[1].split(",")[0]
        if count_item.count(v[0])==1:
            if v[0] in dict1:
                dict1[v[0]].append(v[1])
            else:
                l=[]
                dict1[v[0]] = l
                dict1[v[0]].append(v[1])

f_result=open(smr_file_name,"w")
for key,values in dict1.items():
    f_result.write(key+",")
    for l in values:
        f_result.write(l+",")
    f_result.write("\n")


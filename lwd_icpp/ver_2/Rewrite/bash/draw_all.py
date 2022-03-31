import os,sys

pathArr = [
    "..\\chromiun\\",
    "..\\gcc\\",
    "..\\linux\\",
    "..\\vmdk\\",
]

targetBash = sys.argv[1]

for i in range(len(pathArr)):
    curBash = pathArr[i]+targetBash
    print(curBash)
    os.system(curBash)
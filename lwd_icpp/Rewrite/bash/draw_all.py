import os,sys

pathArr = [
    "..\\chromiun\\",
    "..\\gcc\\",
    "..\\linux\\",
]

targetBash = sys.argv[1]

for i in range(len(pathArr)):
    os.system(pathArr[i]+targetBash)
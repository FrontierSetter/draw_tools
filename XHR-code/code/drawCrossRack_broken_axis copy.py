import xlrd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from brokenaxes import brokenaxes

def draw(k,dataSize,fault):
    file = '跨rack.xlsx'


    wb = xlrd.open_workbook(filename=file)#打开文件


    sheet = wb.sheet_by_index(fault-1)#通过索引获取表格
    n=k//64-1
    if k==64:
        x1 = sheet.row_values(1)[1:dataSize+1]#获取行内容
        x2 = sheet.row_values(1)[1:dataSize+1]#获取行内容
        x3 = sheet.row_values(1)[1:dataSize+1]#获取行内容
        x4 = sheet.row_values(1)[1:dataSize+1]#获取行内容
        y1=[16]*dataSize #TL
        y2=sheet.row_values(4)[1:dataSize+1] #LRC
        y3=sheet.row_values(3)[1:dataSize+1] #ECWide
        y4=sheet.row_values(2)[1:dataSize+1] #XHR
    if n==1:
        x1 = sheet.row_values(1+7*n)[1:dataSize+1]#获取行内容
        x2 = sheet.row_values(1+7*n)[1:dataSize+1]#获取行内容
        x3 = sheet.row_values(1+7*n)[1:dataSize+1]#获取行内容
        x4 = sheet.row_values(1+7*n)[1:dataSize+1]#获取行内容
        y1=[32]*dataSize #TL
        y2=sheet.row_values(4+7*n)[1:dataSize+1] #LRC
        y3=sheet.row_values(3+7*n)[1:dataSize+1] #ECWide
        y4=sheet.row_values(2+7*n)[1:dataSize+1] #XHR
    if n==2:
        x1 = sheet.row_values(1+7*n)[1:dataSize+1]#获取行内容
        x2 = sheet.row_values(1+7*n)[1:dataSize+1]#获取行内容
        x3 = sheet.row_values(1+7*n)[1:dataSize+1]#获取行内容
        x4 = sheet.row_values(1+7*n)[1:dataSize+1]#获取行内容
        y1=[48]*dataSize #TL
        y2=sheet.row_values(4+7*n)[1:dataSize+1] #LRC
        y3=sheet.row_values(3+7*n)[1:dataSize+1] #ECWide
        y4=sheet.row_values(2+7*n)[1:dataSize+1] #XHR
    if n==3:
        x1 = sheet.row_values(1+7*n)[1:dataSize+1]#获取行内容
        x2 = sheet.row_values(1+7*n)[1:dataSize+1]#获取行内容
        x3 = sheet.row_values(1+7*n)[1:dataSize+1]#获取行内容
        x4 = sheet.row_values(1+7*n)[1:dataSize+1]#获取行内容
        y1=[64]*dataSize #TL
        y2=sheet.row_values(4+7*n)[1:dataSize+1] #LRC
        y3=sheet.row_values(3+7*n)[1:dataSize+1] #ECWide
        y4=sheet.row_values(2+7*n)[1:dataSize+1] #XHR
    x1=[int(i)/k for i in x1]
    x2=[int(i)/k for i in x2]
    x3=[int(i)/k for i in x3]
    x4=[int(i)/k for i in x4]

    TX_x = (k+4)/k
    TL_y = k/4

    main_min_x = min([min(x1), min(x2), min(x3), min(x4)])
    main_max_x = max([max(x1), max(x2), max(x3), max(x4)])
    main_min_y = min([min(y1), min(y2), min(y3), min(y4)])
    main_max_y = max([max(y1), max(y2), max(y3), max(y4)])
    main_max_y_1 = max([max(y3), max(y4)])

    print(x1)

    x_gap = (main_max_x-main_min_x)/len(x2)

    fig=plt.figure(figsize=(9,6))

    bax = brokenaxes(ylims=((0, main_max_y_1+5), (main_max_y_1+10,main_max_y_1+22)))

    # 画图
    bax.plot([(k+4)/k], [k/4], label='TL', linestyle=' ', marker='s',  markersize=10)
    # plt.scatter([(k+4)/k], [k/4], s=30, label='TL', linestyle='-', marker='s')
    bax.plot(x2, y2, label='Azure LRC', linestyle='-', marker='p', markersize=10)
    bax.plot(x3, y3, label='ECWide CL', linestyle='-', marker='o', markersize=10)
    bax.plot(x4, y4, label='XHR', linestyle='-', marker='x', markersize=10)
    # 设置坐标轴
    # ax2.set_xlim(1, 1.2)
    # ax2.set_ylim(0, 1.4)
    bax.set_xlabel('Redundancy', fontsize=13)
    if fault==1:
        bax.set_ylabel('single failure cross-rack repair bandwidth', fontsize=13)
    if fault==2:
        bax.set_ylabel('double failure cross-rack repair bandwidth', fontsize=13)
    if fault==3:
        bax.set_ylabel('triple failure cross-rack repair bandwidth', fontsize=13)
    bax.set_xscale('linear')
    # 添加图例
    legend = bax.legend(loc='best')
    # 添加标题
    plt.title(f'k={k}')
    plt.legend(fontsize=18)
    plt.show()
    fig.savefig(f'./{k}-{fault}-total.pdf')


if __name__=="__main__":
    # draw(64,13,1)
    # draw(128,27,1)
    # draw(192,39,1)
    # draw(256,51,1)
    # draw(64,13,2)
    # draw(128,27,2)
    # draw(192,39,2)
    # draw(256,51,2)
    # draw(64,13,3)
    # draw(128,27,3)
    # draw(192,39,3)
    # draw(256,51,3)

    draw(64,10,1)
    draw(128,16,1)
    draw(192,17,1)
    draw(256,19,1)
    # draw(64,10,2)
    # draw(128,16,2)
    # draw(192,17,2)
    # draw(256,19,2)
    # draw(64,10,3)
    # draw(128,16,3)
    # draw(192,17,3)
    # draw(256,19,3)
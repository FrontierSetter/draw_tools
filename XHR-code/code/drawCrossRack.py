import xlrd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math


def draw(k,len,fault):
    file = '10.8.xlsx'


    wb = xlrd.open_workbook(filename=file)#打开文件


    sheet = wb.sheet_by_index(fault-1)#通过索引获取表格
    n=k//64-1
    if k==64:
        x1 = sheet.row_values(1)[1:len+1]#获取行内容
        x2 = sheet.row_values(1)[1:len+1]#获取行内容
        x3 = sheet.row_values(1)[1:len+1]#获取行内容
        x4 = sheet.row_values(1)[1:len+1]#获取行内容
        y1=[16]*len #TL
        y2=sheet.row_values(4)[1:len+1] #LRC
        y3=sheet.row_values(3)[1:len+1] #ECWide
        y4=sheet.row_values(2)[1:len+1] #XHR
    if n==1:
        x1 = sheet.row_values(1+7*n)[1:len+1]#获取行内容
        x2 = sheet.row_values(1+7*n)[1:len+1]#获取行内容
        x3 = sheet.row_values(1+7*n)[1:len+1]#获取行内容
        x4 = sheet.row_values(1+7*n)[1:len+1]#获取行内容
        y1=[32]*len #TL
        y2=sheet.row_values(4+7*n)[1:len+1] #LRC
        y3=sheet.row_values(3+7*n)[1:len+1] #ECWide
        y4=sheet.row_values(2+7*n)[1:len+1] #XHR
    if n==2:
        x1 = sheet.row_values(1+7*n)[1:len+1]#获取行内容
        x2 = sheet.row_values(1+7*n)[1:len+1]#获取行内容
        x3 = sheet.row_values(1+7*n)[1:len+1]#获取行内容
        x4 = sheet.row_values(1+7*n)[1:len+1]#获取行内容
        y1=[48]*len #TL
        y2=sheet.row_values(4+7*n)[1:len+1] #LRC
        y3=sheet.row_values(3+7*n)[1:len+1] #ECWide
        y4=sheet.row_values(2+7*n)[1:len+1] #XHR
    if n==3:
        x1 = sheet.row_values(1+7*n)[1:len+1]#获取行内容
        x2 = sheet.row_values(1+7*n)[1:len+1]#获取行内容
        x3 = sheet.row_values(1+7*n)[1:len+1]#获取行内容
        x4 = sheet.row_values(1+7*n)[1:len+1]#获取行内容
        y1=[64]*len #TL
        y2=sheet.row_values(4+7*n)[1:len+1] #LRC
        y3=sheet.row_values(3+7*n)[1:len+1] #ECWide
        y4=sheet.row_values(2+7*n)[1:len+1] #XHR
    x1=[int(i)/k for i in x1]
    x2=[int(i)/k for i in x2]
    x3=[int(i)/k for i in x3]
    x4=[int(i)/k for i in x4]
    fig,ax=plt.subplots(figsize=(9,6), dpi=100)
    # 画图
    ax.plot(x1, y1, label='TL', linestyle='-', marker='s',  markersize='5')
    ax.plot(x2, y2, label='Azure LRC', linestyle='-', marker='p', markersize='5')
    ax.plot(x3, y3, label='ECWide CL', linestyle='-', marker='o', markersize='5')
    ax.plot(x4, y4, label='XHR', linestyle='-', marker='x', markersize='5')
    # 设置坐标轴
    # ax.set_xlim(1, 1.2)
    # ax.set_ylim(0, 1.4)
    ax.set_xlabel('Redundancy', fontsize=13)
    if fault==1:
        ax.set_ylabel('single failure cross-rack repair bandwidth', fontsize=13)
    if fault==2:
        ax.set_ylabel('double failure cross-rack repair bandwidth', fontsize=13)
    if fault==3:
        ax.set_ylabel('triple failure cross-rack repair bandwidth', fontsize=13)
    ax.set_xscale('linear')
    # ax.set_yscale('symlog')
    # ax.set_yticks([0, 1, 10, 100])
    # 设置刻度
    ax.tick_params(axis='both', labelsize=11)
    # 显示网格
    ax.grid(True, linestyle='-.')
    ax.yaxis.grid(True, linestyle='-.')
    # 添加图例
    legend = ax.legend(loc='best')
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
    draw(64,10,2)
    draw(128,16,2)
    draw(192,17,2)
    draw(256,19,2)
    draw(64,10,3)
    draw(128,16,3)
    draw(192,17,3)
    draw(256,19,3)
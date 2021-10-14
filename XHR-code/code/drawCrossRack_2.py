import xlrd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math


def draw(k,len,fault):
    file = '跨rack.xlsx'


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

    plt.figure(figsize=(9,6))

    # 画图
    plt.plot([(k+4)/k], [k/4], label='TL', linestyle=' ', marker='D',  markersize=12, linewidth=4)
    # ax.plot(x1, y1, label='TL', linestyle='-', marker='s',  markersize='5')
    plt.plot(x2, y2, label='Azure LRC', linestyle='-', marker='^', markersize=12, linewidth=4)
    plt.plot(x3, y3, label='ECWide CL', linestyle='-', marker='o', markersize=12, linewidth=4)
    plt.plot(x4, y4, label='XHR', linestyle='-', marker='x', markersize=12, linewidth=4)
    # 设置坐标轴
    # ax.set_xlim(1.05, max([max(x3), max(x4)])+0.01)
    # ax.set_ylim(0, max([max(y3), max(y4)])*1.2)
    plt.xlabel('Redundancy', fontsize=28)
    if fault==1:
        plt.ylabel('single failure cross-rack\nrepair bandwidth', fontsize=28)
    if fault==2:
        plt.ylabel('double failure cross-rack\nrepair bandwidth', fontsize=28)
    if fault==3:
        plt.ylabel('triple failure cross-rack\nrepair bandwidth', fontsize=28)
    # plt.xscale('linear')
    # ax.set_yscale('symlog')
    # ax.set_yticks([0, 1, 10, 100])
    # ax.set_yticks([0, 1, 10, 100])
    # ax.set_xticklabels(labels=x3, fontsize=20)
    # ax.set_yticklabels(fontsize=20)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=20)
    # 设置刻度
    # ax.tick_params(axis='both', labelsize=13)
    # 显示网格
    plt.grid(True, linestyle='-.')
    # ax.yaxis.grid(True, linestyle='-.')
    # 添加图例
    legend = plt.legend(loc='best')
    # 添加标题
    plt.title(f'k={k}')
    plt.legend(fontsize=22)

    left,bottom,width,height = 0.68,0.45,0.29,0.25
    # left,bottom,width,height = 0.71,0.15,0.25,0.20
    # ax1 = fig.add_axes([left,bottom,width,height])
    # ax1.plot([(k+4)/k], [k/4], label='TL', linestyle=' ', marker='s',  markersize=10)
    # # ax.plot(x1, y1, label='TL', linestyle='-', marker='s',  markersize='5')
    # ax1.plot(x2, y2, label='Azure LRC', linestyle='-', marker='p', markersize='5')
    # ax1.plot(x3, y3, label='ECWide CL', linestyle='-', marker='o', markersize='5')
    # ax1.plot(x4, y4, label='XHR', linestyle='-', marker='x', markersize='5')
    # ax1.tick_params(axis='both', labelsize=11)
    # ax1.grid(True, linestyle='-.')
    # ax1.yaxis.grid(True, linestyle='-.')

    plt.subplots_adjust(left=0.18, right=0.98, top=0.99, bottom=0.15)

    plt.savefig(f'./{k}-{fault}-total.pdf')
    plt.show()


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
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

    print(x1)

    x_gap = (main_max_x-main_min_x)/len(x2)

    fig=plt.figure(figsize=(9,6))

    rect1 = [0.05, 0.05, 0.9, 0.15] # [左, 下, 宽, 高] 规定的矩形区域 （全部是0~1之间的数，表示比例）
    rect2 = [0.05, 0.16, 0.9, 0.75]

    ax1 = plt.axes(rect1)
    ax2 = plt.axes(rect2)

    ax1.spines['top'].set_visible(False)#关闭子图1中底部脊
    ax2.spines['bottom'].set_visible(False)##关闭子图2中顶部脊
    d = .85  #设置倾斜度

    #绘制断裂处的标记
    kwargs = dict(marker=[(-1, -d), (1, d)], markersize=15,
                linestyle='none', color='black', mec='r', mew=1, clip_on=False)
    ax1.plot([1, 1], [1, 0],transform=ax1.transAxes, **kwargs)
    ax2.plot([0, 0], [0, 1], transform=ax2.transAxes, **kwargs)

    ax1.set_ylim(0, max([main_max_y, TL_y])*1.01)
    ax2.set_ylim(0, max([main_max_y, TL_y])*1.01)


    # 画图
    ax1.plot([(k+4)/k], [k/4], label='TL', linestyle=' ', marker='s',  markersize=10)
    # plt.scatter([(k+4)/k], [k/4], s=30, label='TL', linestyle='-', marker='s')
    ax2.plot(x2, y2, label='Azure LRC', linestyle='-', marker='p', markersize=10)
    ax2.plot(x3, y3, label='ECWide CL', linestyle='-', marker='o', markersize=10)
    ax2.plot(x4, y4, label='XHR', linestyle='-', marker='x', markersize=10)
    # 设置坐标轴
    # ax2.set_xlim(1, 1.2)
    # ax2.set_ylim(0, 1.4)
    ax2.set_xlabel('Redundancy', fontsize=13)
    if fault==1:
        ax1.set_ylabel('single failure cross-rack repair bandwidth', fontsize=13)
    if fault==2:
        ax1.set_ylabel('double failure cross-rack repair bandwidth', fontsize=13)
    if fault==3:
        ax1.set_ylabel('triple failure cross-rack repair bandwidth', fontsize=13)
    ax2.set_xscale('linear')
    # ax2.set_yscale('symlog')
    # ax2.set_yticks([])
    # ax2.get_yaxis().set_visible(False)
    plt.setp(ax2.get_yticklabels(), visible=False)
    # 设置刻度
    ax2.tick_params(axis='both', labelsize=11)
    ax1.tick_params(axis='both', labelsize=11)
    # 显示网格
    ax2.grid(True, linestyle='-.')
    ax1.grid(True, linestyle='-.')
    ax1.yaxis.grid(True, linestyle='-.')
    # 添加图例
    legend = ax2.legend(loc='best')
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
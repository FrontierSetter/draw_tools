from ast import arg
import numpy as np
import os, sys
import matplotlib.pyplot as plt
import random
import argparse

parser = argparse.ArgumentParser(description='画单条折线图，各项参数见https://matplotlib.org/3.1.1/api/pyplot_summary.html')
parser.add_argument('-f','--file', help='输入的csv文件，第一行是xtick，第二行是值')
parser.add_argument('-c','--color', default='#1f497d', help='曲线颜色，默认#1f497d')
parser.add_argument('-x','--x_label', default='xlabel', help='x轴的名字')
parser.add_argument('-y','--y_label', default='ylabel', help='y轴的名字')
parser.add_argument('-l','--legend', default='1', help='是否需要图例，1表示要，其他不要')
parser.add_argument('--x_rotate', default='0', help='x轴标签逆时针旋转')
parser.add_argument('--tick_font_size', default='26', help='横纵坐标轴的字体大小')
parser.add_argument('--label_font_size', default='28', help='横纵坐标轴名字大小')
parser.add_argument('--legend_font_size', default='26', help='图例大小')
parser.add_argument('--y_max', default='x', help='纵轴上限，默认自动设置')
parser.add_argument('--y_min', default='x', help='纵轴下限，默认自动设置')
parser.add_argument('--format', default='pdf', help='输出格式，默认pdf')
parser.add_argument('--margin', default=[0.15, 0.99, 0.975, 0.15], nargs='*', help='页边距，顺序：左右上下，怎么快速找合适的值跟谷说明过了')
parser.add_argument('-s', '--stack', action='store_true', help='是否要画线下阴影区域，默认不画')

args = parser.parse_args()
print(args)

fileName = args.file
(filePath,tempFileName) = os.path.split(fileName)
(fileNameLite,fileExtension) = os.path.splitext(tempFileName)

lineColor = args.color

inFile = open(fileName, 'r')

# x轴的tick要改的话改一下
xTick = [int(float(x)) for x in inFile.readline().strip('\n').split(',')]
# 百分比
valueArr = [float(x)*100 for x in inFile.readline().strip('\n').split(',')]
print(valueArr)
print(xTick)

# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(9,6))

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='both')

# 各项参数
line_lw = 2
curP = plt.plot(range(len(valueArr)), valueArr, label=fileNameLite, lw=line_lw, color=lineColor)
if args.stack != 'x':
    plt.stackplot(range(len(valueArr)), valueArr, colors=lineColor, alpha=0.2)

    
# 设置坐标轴文字
plt.ylabel(args.y_label, fontsize=int(args.label_font_size))
plt.xlabel(args.x_label, fontsize=int(args.label_font_size))

# 设置坐标轴刻度
plt.yticks(fontsize=int(args.tick_font_size))
plt.xticks(fontsize=int(args.tick_font_size), rotation=float(args.x_rotate))

# 设置图例
if args.legend == '1':
    plt.legend(fontsize=int(args.legend_font_size))

# 设置坐标轴范围
plt.xlim(0, len(xTick)-1)
bottom, top = plt.ylim()
if args.y_max != 'x':
    top = float(args.y_max)
if args.y_min != 'x':
    bottom = float(args.y_min)
plt.ylim(bottom, top)

# 设置图片边距
plt.subplots_adjust(left=float(args.margin[0]), right=float(args.margin[1]), top=float(args.margin[2]), bottom=float(args.margin[3]))

# 保存图片

plt.savefig('%s.%s' % (fileNameLite, args.format))
# plt.savefig('line.png', dpi=600)

# 显示图片
plt.show()
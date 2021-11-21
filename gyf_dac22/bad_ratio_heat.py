import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
from scipy.interpolate import griddata
import xlrd
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

readbook = xlrd.open_workbook('bad ratio.xlsx')
configSheet = readbook.sheet_by_name('Sheet1')

nrows = configSheet.nrows

X = []
Y = []
Z = []

for i in range(1, nrows):
    curRow = configSheet.row_values(i)
    Z.append(curRow)

X_len = len(Z)
Y_len = len(Z[-1])

yIdx = [0, 2, 4, 6, 8]
yNum = ['0', '2', '4', '6', '8']

xIdx = []
xNum = []

for i in range(0, 256, 32):
    xIdx.append(i)

for i in xIdx:
    xNum.append("%d" % (i))


fig = plt.figure(figsize=(12,6))
ax = plt.axes()
plt.subplots_adjust(left=0.06, right=0.99, top=0.96, bottom=0.12, hspace=0.36)

plt.gca().xaxis.set_ticks_position('top')

# 定制色卡
clist = ['#EBEDF0', '#9BE9A8', '#40C463', '#30A14E', '#216E39', '#00441B']
gitHub = LinearSegmentedColormap.from_list('gitHub', clist)

im = plt.imshow(Z, cmap=gitHub, aspect=6)   #用aspect调整每个cell的横纵比例
plt.xticks(xIdx, xNum, fontsize=16)
plt.yticks(yIdx, yNum, fontsize=16)

# 调整colorbar的位置和字体等属性
position=fig.add_axes([0.16, 0.275, 0.7, 0.03])#位置[左,下,右,上]
cb=plt.colorbar(im, cax=position, orientation='horizontal', shrink=0.6)#方向
cb.ax.tick_params(labelsize=16)

plt.savefig('bad_ratio_heat.pdf')
plt.show()

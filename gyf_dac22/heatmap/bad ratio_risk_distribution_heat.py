import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
from scipy.interpolate import griddata
import xlrd
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import seaborn as sns

readbook = xlrd.open_workbook('bad ratio_risk_distribution.xlsx')
configSheet = readbook.sheet_by_name('Sheet1')

nrows = configSheet.nrows

X = []
Y = []
Z = []

for i in range(0, nrows):
    curRow = configSheet.row_values(i)
    Z.append(curRow[:])

X_len = len(Z)
Y_len = len(Z[-1])

yIdx = [0, 2, 4, 6, 8]
yNum = ['0', '2', '4', '6', '8']

xIdx = []
xNum = []

for i in range(0, 256, 32):
    xIdx.append(i+0.5)
xIdx.append(255.5)

for i in xIdx:
    xNum.append("%d" % (i))


fig = plt.figure(figsize=(12,2.2))
ax = plt.axes()
plt.subplots_adjust(left=0.055, right=0.985, top=0.865, bottom=0.275, hspace=0.36)

# plt.gca().xaxis.set_ticks_position('top')
# plt.gca().xaxis.set_label_position('top')

# 定制色卡
clist = ['#EBEDF0', '#9BE9A8', '#40C463', '#30A14E', '#216E39', '#00441B']
clist_black = ['#FFFFFF', '#9D9D9D', '#333333', '#333333', '#000000']
clist_blue = ['#FFFFFF', '#1967AD', '#084991', '#083E80', '#08316C']
# clist_blue = ['#FFFFFF', '#D3E3F3', '#1967AD', '#084991', '#083E80', '#08316C']
# clist_blue = ['#FFFFFF', '#559FCD', '#1967AD', '#084991', '#083E80', '#08316C']
# clist_blue = ['#FFFFFF', '#D3E3F3', '#559FCD', '#1967AD', '#084991', '#083E80', '#08316C']
gitHub = LinearSegmentedColormap.from_list('gitHub', clist)
grey_color = LinearSegmentedColormap.from_list('grey', clist_black)
blue_color = LinearSegmentedColormap.from_list('blue', clist_blue)

# im = plt.imshow(Z, cmap=grey_color, aspect=3)   #用aspect调整每个cell的横纵比例
# plt.grid(color="w", linestyle='-', linewidth=5)
ax = sns.heatmap(Z, cmap=blue_color, linewidth=0.2, cbar=False, yticklabels=2)
for _, spine in ax.spines.items():
    spine.set_visible(True)

# for i in range(X_len):
#     ax.axhline(i+0.5, color='white', lw=1)
# for i in range(Y_len):
#     ax.axvline(i+0.5, color='white', lw=0.8)

# plt.xlim()

# plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.xticks(xIdx, xNum, fontsize=16, rotation=0)
# plt.yticks(yIdx, yNum, fontsize=16)

plt.xlabel('the Number of Error Bit per Data Frame', fontsize=20)
plt.ylabel('Loop Number', fontsize=20)

# 调整colorbar的位置和字体等属性
# position=fig.add_axes([0.16, 0.275, 0.7, 0.03])#位置[左,下,右,上]
# cb=plt.colorbar(im, cax=position, orientation='horizontal', shrink=0.6)#方向
# cb.ax.tick_params(labelsize=16)

plt.savefig('bad_ratio_risk_distribution.pdf')
plt.show()

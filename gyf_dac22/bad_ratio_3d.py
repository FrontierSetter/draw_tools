import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
from scipy.interpolate import griddata
import xlrd

readbook = xlrd.open_workbook('bad ratio.xlsx')
configSheet = readbook.sheet_by_name('Sheet1')

nrows = configSheet.nrows

X = []
Y = []
Z = []
globalMax = 0

for i in range(1, nrows):
    curRow = configSheet.row_values(i)
    Z.append(curRow)

X_len = len(Z)
Y_len = len(Z[-1])

# 生成用于画散点图的数据
X_s = []
Y_s = []
Z_s = []

for curX in range(len(Z)):
    for curY in range(len(Z[curX])):
        if Z[curX][curY] != 0:
            X_s.append(curX)
            Y_s.append(curY)
            Z_s.append(Z[curX][curY])

# 生成用于画平面图的数据
X = np.arange(len(Z))
Y = np.arange(len(Z[-1]))

X,Y = np.meshgrid(X,Y)
Z = np.array(Z).transpose()
print(Z.shape)

fig = plt.figure(figsize=(12,6))
ax = Axes3D(fig,auto_add_to_figure=False)
fig.add_axes(ax)

# ax.plot_surface(X, Y, Z) #生成表面，alpha用于控制透明度

# ax.scatter(X_s, Y_s, Z_s)

width = 1#x,y方向的宽厚
depth = 1
for i in range(X_len):
    for j in range(Y_len):
        # print(i, j)
        z = Z[j][i] #该柱的高
        if z == 0:
            continue
        color = np.array([255, 255, 255])/255.0#颜色 其中每个元素在0~1之间
        ax.bar3d(i, j, 0, width, depth, z, color=color)   #每次画一个柱

ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([0.1, 2, 1, 1]))
ax.view_init(16, -30)

ax.set_ylim(0, Y_len)


ax.set_zlabel('Z', fontdict={'size': 15, 'color': 'black'})
ax.set_xlabel('X', fontdict={'size': 15, 'color': 'black'})
ax.set_ylabel('Y', fontdict={'size': 15, 'color': 'black'})

plt.savefig('bad_ration_3d.pdf')
plt.show()

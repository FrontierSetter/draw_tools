import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
from scipy.interpolate import griddata
import xlrd

readbook = xlrd.open_workbook('reliability risk_bad.xlsx')
configSheet = readbook.sheet_by_name('Sheet1')

nrows = configSheet.nrows

X = []
Y = []
Z = []

for i in range(0, nrows):
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

fig = plt.figure()
ax = Axes3D(fig,auto_add_to_figure=False)
fig.add_axes(ax)

# ax.plot_surface(X, Y, Z, cmap=plt.get_cmap('rainbow')) #生成表面，alpha用于控制透明度
# ax.plot_surface(X, Y, Z) #生成表面，alpha用于控制透明度
# ax.scatter(X_s, Y_s, Z_s)

width = depth = 1#x,y方向的宽厚
for i in range(X_len):
    for j in range(Y_len):
        # print(i, j)
        z = Z[j][i] #该柱的高
        if z == 0:
            continue
        color = np.array([255, 255, 255])/255.0#颜色 其中每个元素在0~1之间
        ax.bar3d(i, j, 0, width, depth, z, color=color)   #每次画一个柱


ax.set_ylim(0, Y_len)


# ax.set_zlabel('single chunk repair cross-rack λ', fontdict={'size': 15, 'color': 'black'})
# ax.set_xlabel('$m_l / (m_l + m_g + 1)$', fontdict={'size': 15, 'color': 'black'})
# ax.set_ylabel('k', fontdict={'size': 15, 'color': 'black'})

plt.savefig('reliability risk_bad_4d.pdf')
plt.show()

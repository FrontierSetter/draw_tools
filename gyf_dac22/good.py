import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
from scipy.interpolate import griddata
import xlrd

readbook = xlrd.open_workbook('good.xlsx')
configSheet = readbook.sheet_by_name('good')

nrows = configSheet.nrows

X = []
Y = []
Z = []

for i in range(1, nrows):
    curRow = configSheet.row_values(i)
    Z.append(curRow)

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




fig = plt.figure()
ax = Axes3D(fig,auto_add_to_figure=False)
fig.add_axes(ax)

# ax.plot_surface(X, Y, Z, cmap=plt.get_cmap('rainbow')) #生成表面，alpha用于控制透明度
# ax.plot_surface(X, Y, Z) #生成表面，alpha用于控制透明度
ax.scatter(X_s, Y_s, Z_s) #生成表面，alpha用于控制透明度

ax.set_ylim(0, 256)


# ax.set_zlabel('single chunk repair cross-rack λ', fontdict={'size': 15, 'color': 'black'})
# ax.set_xlabel('$m_l / (m_l + m_g + 1)$', fontdict={'size': 15, 'color': 'black'})
# ax.set_ylabel('k', fontdict={'size': 15, 'color': 'black'})

plt.savefig('good.pdf')
plt.show()

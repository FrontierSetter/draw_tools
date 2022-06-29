import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
from scipy.interpolate import griddata

# data1 = np.arange(24).reshape((8, 3))

# x1 = data1[:, 0]
# y1 = data1[:, 1]
# z1 = data1[:, 2]
# z1 = np.zeros((8,), dtype = np.int)

# data2 = np.random.randint(0, 23, (6, 3))

# x2 = data2[:, 0]
# y2 = data2[:, 1]
# z2 = data2[:, 2]

x3 = np.arange(4, 13, 1)
y3 = np.arange(4, 13, 1)
x3,y3 = np.meshgrid(x3,y3)
z3 = 132/(x3*y3)

x4 = np.arange(4, 13, 1)
y4 = np.arange(4, 13, 1)
x4,y4 = np.meshgrid(x4,y4)
z4 = 132/(4*y4)

x5_1 = np.arange(1, 9, 0.01) / 10
y5_1 = np.arange(1, 256, 1)
x5,y5 = np.meshgrid(x5_1,y5_1)
z5 = y5/((1-x5)*x5*100)

print(x5)
print(y5)
print(z5)

# z6 = y5/(10*(1-x5))

fig = plt.figure()
ax = Axes3D(fig,auto_add_to_figure=False)
fig.add_axes(ax)
# ax = plt.axes(projection="3d")
# ax.scatter(x1, y1, z1, c='r', label='a')
# ax.scatter(x2, y2, z2, c='g', label='b')
# ax.scatter(x3, y3, z3, c='b', label='XHR')
# ax.scatter(x4, y4, z4, c='r', label='ECWide')
# ax.scatter(x5, y5, z5, c='r', label='$\lambda$')
# ax.scatter(x5, y5, z6, c='b', label='$z$')


# ax.plot_surface(x3,y3,z3,alpha=0.5,cmap="winter") #生成表面，alpha用于控制透明度
# ax.plot_surface(x4,y4,z4,alpha=0.5,cmap="summer") #生成表面，alpha用于控制透明度
# ax.contour(x3,y3,z3,zdir="x",offset=-6,cmap="rainbow")   #x轴投影
# ax.contour(x3,y3,z3,zdir="y",offset=6,cmap="rainbow")    #y轴投影
# ax.contour(x3,y3,z3,zdir="z",offset=-3,cmap="rainbow")   #z轴投影
# ax.contour(x3,y3,z3,zdir="x",offset=2,cmap="rainbow")   #x轴投影
# ax.contour(x3,y3,z3,zdir="y",offset=2,cmap="rainbow")    #y轴投影
# ax.contour(x3,y3,z3,zdir="z",cmap="rainbow")   #z轴投影

# ax.contour(x4,y4,z4,zdir="x",offset=4,cmap="rainbow")
# ax.contour(x3,y3,z3,zdir="x",offset=4,cmap="rainbow")

# xi, yi = np.meshgrid(np.linspace(x5.min(), x5.max(), 20), np.linspace(y5.min(), y5.max(), 20))

# triang = mtri.Triangulation(x5, y5)
# interp_lin = mtri.LinearTriInterpolator(triang, z5)

# zi_lin = interp_lin(xi, yi)
# zi_lin = griddata((x5, y5), z5, (xi[None,:], yi[:,None]), method='nearest')

ax.plot_surface(x5, y5,z5,cmap=plt.get_cmap('rainbow')) #生成表面，alpha用于控制透明度
# ax.legend(loc='best')


ax.set_zlabel('λ', fontdict={'size': 15, 'color': 'black'})
ax.set_xlabel('$m_l / (m_l + m_g + 1)$', fontdict={'size': 15, 'color': 'black'})
ax.set_ylabel('k', fontdict={'size': 15, 'color': 'black'})

plt.show()
plt.savefig('3d.pdf')






















# z3 = np.zeros((13,), dtype = np.int)
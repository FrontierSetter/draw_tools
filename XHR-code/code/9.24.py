import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data1 = np.arange(24).reshape((8, 3))

x1 = data1[:, 0]
y1 = data1[:, 1]
z1 = data1[:, 2]
z1 = np.zeros((8,), dtype = np.int)

data2 = np.random.randint(0, 23, (6, 3))

x2 = data2[:, 0]
y2 = data2[:, 1]
z2 = data2[:, 2]

x3 = np.arange(4, 13, 1)
y3 = np.arange(4, 13, 1)
x3,y3 = np.meshgrid(x3,y3)
z3 = 132/(x3*y3)

x4 = np.arange(4, 13, 1)
y4 = np.arange(4, 13, 1)
x4,y4 = np.meshgrid(x4,y4)
z4 = 132/(4*y4)

fig = plt.figure()
ax = Axes3D(fig)
# ax = plt.axes(projection="3d")
# ax.scatter(x1, y1, z1, c='r', label='a')
# ax.scatter(x2, y2, z2, c='g', label='b')
ax.scatter(x3, y3, z3, c='b', label='XHR')
ax.scatter(x4, y4, z4, c='r', label='ECWide')

ax.legend(loc='best')

ax.plot_surface(x3,y3,z3,alpha=0.5,cmap="winter") #生成表面，alpha用于控制透明度
ax.plot_surface(x4,y4,z4,alpha=0.5,cmap="summer") #生成表面，alpha用于控制透明度
# ax.contour(x3,y3,z3,zdir="x",offset=-6,cmap="rainbow")   #x轴投影
# ax.contour(x3,y3,z3,zdir="y",offset=6,cmap="rainbow")    #y轴投影
# ax.contour(x3,y3,z3,zdir="z",offset=-3,cmap="rainbow")   #z轴投影
# ax.contour(x3,y3,z3,zdir="x",offset=2,cmap="rainbow")   #x轴投影
# ax.contour(x3,y3,z3,zdir="y",offset=2,cmap="rainbow")    #y轴投影
# ax.contour(x3,y3,z3,zdir="z",cmap="rainbow")   #z轴投影
ax.contour(x4,y4,z4,zdir="x",offset=4,cmap="rainbow")
ax.contour(x3,y3,z3,zdir="x",offset=4,cmap="rainbow")


ax.set_zlabel('single chunk repair cross-rack λ', fontdict={'size': 15, 'color': 'red'})
ax.set_ylabel('m_XOR', fontdict={'size': 15, 'color': 'red'})
ax.set_xlabel('m_HH', fontdict={'size': 15, 'color': 'red'})

plt.show()






















# z3 = np.zeros((13,), dtype = np.int)
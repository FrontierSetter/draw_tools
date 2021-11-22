import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
from scipy.interpolate import griddata
import xlrd

readbook = xlrd.open_workbook('show_all_bad_original.xlsx')
configSheet = readbook.sheet_by_name('show_all_bad_original')

nrows = configSheet.nrows

X = []
Y = []
Z = []

for i in range(1, nrows):
    curRow = configSheet.row_values(i)
    Z.append(curRow)

X_len = len(Z)
Y_len = len(Z[-1])


plt.figure(figsize=(9,6))
plt.subplots_adjust(left=0.12, right=0.99, top=0.96, bottom=0.12, hspace=0.36)

plt.imshow(Z, cmap=plt.cm.hot)

plt.savefig('bad_heat.pdf')
plt.show()

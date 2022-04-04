import numpy as np
import matplotlib.pyplot as plt

inFile = open('spearman.csv', 'r')

xTick = inFile.readline().strip('\n').split(',')
inFile.readline()
valueArr = [float(x) for x in inFile.readline().strip('\n').split(',')]

xTick.reverse()
valueArr.reverse()

# valueArr = [1,2,3,4]
# xTick = ['xx','yy','zz','aa']

# 生成图片实例，figsize的元组是宽高比
fig = plt.figure(figsize=(18,6))
ax = plt.gca()

# 隐藏边框
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.spines['left'] .set_linewidth(4)

# 生成背后的网格
plt.grid(True, linestyle='-.', axis='x')

curP = plt.barh(range(len(xTick)), valueArr, height=0.6, color='#5B9BD5')

#为横向水平的柱图右侧添加数据标签。
font={
    'family':'Times New Roman',
    'weight':'normal',
    'size':22
}
for rect in curP:
    # width是宽度，y是上边沿纵坐标，height是厚度
    w = rect.get_width()
    print("%f, %f, %f" % (w, rect.get_y(), rect.get_height()))
    plt.text(w+0.01, rect.get_y()+rect.get_height()/2, '%.3f' %
            w, ha='left', va='center', fontsize=22)

# 设置坐标轴文字
# plt.ylabel('yName (unit)', fontsize=26)
# plt.xlabel('xName (unit)', fontsize=28)

# 设置坐标轴刻度
for size in ax.get_yticklabels():   #获取x轴上所有坐标，并设置字号
    size.set_fontname('Times New Roman')  

plt.xticks(np.arange(0, 1.1, 0.2), fontsize=26)
plt.yticks(range(len(xTick)), xTick, fontsize=22)

# 设置坐标轴范围
plt.xlim(0, 0.61)

# 设置图片边距
plt.subplots_adjust(left=0.32, right=0.995, top=1, bottom=0.07)

# 保存图片
plt.savefig('spearman.pdf')

# 显示图片
plt.show()

# font={
#     'family':'Times New Roman',
#     'weight':'normal',
#     'size':30
# }


# #让图例生效
# plt.legend(prop=font,frameon=False,loc='lower left')
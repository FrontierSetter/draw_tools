人工调整参数说明（以draw_normal_two为例）：

详细参数说明请搜索：https://matplotlib.org/3.1.1/api/pyplot_summary.html

大图比例
第194行：plt.figure(figsize=(36,15))
    figsize调整整个大图的比例

轴刻度
第265行：plt.xticks(ind, dataDict[figType][curSubFigK]['x-value'], fontsize=20)
    fontsize调整x轴 刻度 的字号

轴标题
第266行：plt.xlabel(figXLabel[figType], fontsize=26)
    fontsize调整x轴 标题 的字号

科学计数法小标签
第281、285行：plt.text(xmin, ymax*1.005, r'$\times10^{%d}$'%(scalNum),fontsize=20,ha='left')
    fontsize调整 科学计数法小标签 的字号
    第一、第二个参数调整小标签的位置，xmin，ymax代表很坐标的最小值和纵坐标的最大值
    ha表示左端对齐，和上一行匹配，表示小标签的左下角正好放在坐标系的左上角

子标题
第294行:plt.title(fill(('(%s) %s' % (letterArr[subFigCnt-1], subTitleDict[figType][curSubFigK])), 60), fontsize=16, y=-0.25)
    '(%s) %s'代表子标题格式，第一个字符串是字母序，第二个是excel里的文字
    , 60表示自动换行的最大值
    fontsize表示字号
    y代表位置（不是纵坐标，我也不知道这个数字代表什么）

图例
第297行：plt.figlegend(legendArr, legendEntryArr, ncol=len(legendEntryArr), loc="upper center", fontsize=22, columnspacing=1, handletextpad=0.3, bbox_to_anchor=(0.5, 1.01))
    ncol调整图例的列数
    loc调整位置（此处弃用）
    bbox_to_anchor微调位置，第一个参数表示左右，越大越往右，第二个参数表示上下，越大越往上
    fontsize表示字号
    columnspacing行间距
    handletextpad图和文字之间的间距

子图间距、页边距
第298行：plt.subplots_adjust(left=0.03, right=0.99, top=0.93, bottom=0.11, hspace=0.3)
    前四个参数调整整个大图的四边距，left=0.03表示左侧边在3%的位置
    hspace调整子图间上下间距，vspace调整左右间距


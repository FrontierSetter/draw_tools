from numpy.lib.function_base import median
import xlrd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator

# colorDict = {'Full Recovery-PPR': 'darkviolet', 'Full Recovery-RP': 'dodgerblue', 'PRM': 'gold',
#              'Baseline': 'skyblue','GAN': '#fa8080'}  # 设置配色 2021-09-21

# colorDict = {'PRM-Typical': '#80499C', 'PRM-PPR': '#87CFEC', 'PRM-RP': '#3CB474', 'GAN': '#F26750'}  # 设置配色 2021-09-21
# hatchDict = {'PRM-Typical': '////', 'PRM-PPR': '\\\\\\\\', 'PRM-RP': 'xxxx', 'GAN': '--'}

colorDict = {'PRM-Typical': '#80499C', 'Typical': '#3478BF', 'PRM-RP': '#219ebc', 'RP': '#B8860B', 'PRM-PPR': '#0a9396', 'PPR': '#F26750', 'GAN': '#C00000'}  # 设置配色 2021-09-21
markerDict = {'PRM-Typical': '^', 'Typical': 'o', 'PRM-RP': 'v', 'RP': 'D', 'PRM-PPR': '>', 'PPR': 's', 'GAN': 'x'}  # 设置配色 2021-09-21
legacyPositionDict = ['lower right', 'upper left', 'lower right', 'lower right']

def setBoxplotStyle(bp, name):
    for box in bp['boxes']:
        # change outline color
        box.set(color=colorDict[name], linewidth=2)
        # change fill color
        box.set(facecolor = 'white' )
        # change hatch
        box.set(hatch='////' if 'PRM' in name  else '\\\\\\\\')
    for whisker in bp['whiskers']:
        whisker.set(color=colorDict[name], linewidth=2)
    ## change color and linewidth of the caps
    for cap in bp['caps']:
        cap.set(color=colorDict[name], linewidth=2)
    ## change color and linewidth of the medians
    for median in bp['medians']:
        median.set(color=colorDict[name], linewidth=2)

dataDict = {}
paraDict = {}

readbook = xlrd.open_workbook('RS(6,3)数据-PRM-GAN_all_box.xlsx')

sheets = readbook.sheets()
sheetNames = readbook.sheet_names()

for i in range(2, len(sheets)):
    if 'rand' in sheetNames[i]:
        continue

    curSheet = sheets[i]

    curModelName = curSheet.row_values(1)[0]

    print(curModelName)

    dataDict[curModelName] = {'x-arr': [str(int(x)) for x in curSheet.row_values(0)[2:] if len(str(x)) > 1]}
    paraDict[curModelName] = {
        'yMin': curSheet.row_values(2)[0],
        'yMax': curSheet.row_values(3)[0],
    }
    paraDict[curModelName]['full_line'] = curSheet.row_values(4)[0]
    paraDict[curModelName]['base_line'] = curSheet.row_values(5)[0]

    for curLineNum in range(4, curSheet.nrows):
        curRow = curSheet.row_values(curLineNum)
        # if "Full Recovery" in curRow[1] or 'Baseline' in curRow[1]:
        #     continue
        if len(curRow[1]) == 0:
            continue

        curMethod = curRow[1]

        if curMethod not in dataDict[curModelName]:
            dataDict[curModelName][curMethod] = []

        curOffset = curRow[10]
        dataDict[curModelName][curMethod].append([x-curOffset for x in curRow[2:7] if type(x) != type('')])


print(dataDict)
print(len(dataDict))

for subFigId in range(len(dataDict)):
    fig = plt.figure(figsize=(9,12))

    curModelName = list(dataDict.keys())[subFigId]
    ind=np.arange(len(dataDict[curModelName]['x-arr']))
    bar_width = 0.8#设置柱状图的宽度
    gap_width = 0.06
    line_width = 1.65
    totalBarNum = 2
    totalGroupNum = len(dataDict[curModelName]['x-arr'])

    # 第一幅子图
    plt.subplot(311)
    legendArr = []
    legendEntryArr = []
    bp = plt.boxplot(dataDict[curModelName]['PRM-Typical'], positions=[x*3+1 for x in range(totalGroupNum)], widths=bar_width, patch_artist=True)
    legendArr.append(bp["boxes"][0])
    legendEntryArr.append('PRM-Typical')
    # plt.bar([],[], color='white', linewidth=2, edgecolor=colorDict['PRM-Typical'], hatch='//////')
    setBoxplotStyle(bp, 'PRM-Typical')
    
    # plot_x = []
    # plot_y = []
    # for x in range(totalGroupNum):
    #     plot_x.append(x*3+1-bar_width/2)
    #     plot_x.append(x*3+1+bar_width/2)
    # for medline in bp['medians']:
    #     plot_y.append(medline.get_ydata()[0])
    #     plot_y.append(medline.get_ydata()[1])
    # plt.plot(plot_x, plot_y, color=colorDict['PRM-Typical'], alpha=0.6)
    plt.plot([x*3+1 for x in range(totalGroupNum)], [medline.get_ydata()[0] for medline in bp['medians']], \
        lw=line_width, color=colorDict['PRM-Typical'], alpha=0.9, ls='-')
    
    bp = plt.boxplot(dataDict[curModelName]['Typical'], positions=[x*3+2 for x in range(totalGroupNum)], widths=bar_width, patch_artist=True)
    legendArr.append(bp["boxes"][0])
    legendEntryArr.append('Typical')
    # plt.bar([],[], color='white', linewidth=2, edgecolor=colorDict['Typical'], hatch='//////')
    setBoxplotStyle(bp, 'Typical')
    plt.plot([x*3+2 for x in range(totalGroupNum)], [medline.get_ydata()[0] for medline in bp['medians']], \
        lw=line_width, color=colorDict['Typical'], alpha=0.9, ls='-')


    plt.ylabel('acc(%)', fontsize=22)
    plt.legend(legendArr, legendEntryArr, fontsize=18,ncol=2,columnspacing=0.8,handletextpad=0.5, loc=legacyPositionDict[subFigId])#显示图例，即label
    plt.yticks(fontsize=18)
    plt.xlabel('Recovery Ratio(%)', fontsize=22)
    plt.xlim(0, 3*totalGroupNum)
    plt.xticks([x*3+1.5 for x in range(totalGroupNum)], dataDict[curModelName]['x-arr'], fontsize=18)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
    plt.grid(True, linestyle='-.', axis='y')
    # plt.xticks(rotation=352) #x轴标签旋转

    left,bottom,width,height = 0.002,0.03,1,0.15
    # left,bottom,width,height = 0.71,0.15,0.25,0.20
    ax1 = fig.add_axes([left,bottom,width,height])
    ax1.set_ylim(0,1)
    ax1.set_xlim(0,1)

    # 第二幅子图
    plt.subplot(312)
    legendArr = []
    legendEntryArr = []
    bp = plt.boxplot(dataDict[curModelName]['PRM-RP'], positions=[x*3+1 for x in range(totalGroupNum)], widths=bar_width, patch_artist=True)
    legendArr.append(bp["boxes"][0])
    legendEntryArr.append('PRM-RP')
    # plt.bar([],[], color='white', linewidth=2, edgecolor=colorDict['PRM-Typical'], hatch='//////')
    setBoxplotStyle(bp, 'PRM-RP')
    plt.plot([x*3+1 for x in range(totalGroupNum)], [medline.get_ydata()[0] for medline in bp['medians']], \
        lw=line_width, color=colorDict['PRM-RP'], alpha=0.9, ls='-')
    
    bp = plt.boxplot(dataDict[curModelName]['RP'], positions=[x*3+2 for x in range(totalGroupNum)], widths=bar_width, patch_artist=True)
    legendArr.append(bp["boxes"][0])
    legendEntryArr.append('RP')
    # plt.bar([],[], color='white', linewidth=2, edgecolor=colorDict['Typical'], hatch='//////')
    setBoxplotStyle(bp, 'RP')
    plt.plot([x*3+2 for x in range(totalGroupNum)], [medline.get_ydata()[0] for medline in bp['medians']], \
        lw=line_width, color=colorDict['RP'], alpha=0.9, ls='-')

    plt.ylabel('acc(%)', fontsize=22)
    plt.legend(legendArr, legendEntryArr, fontsize=18,ncol=2,columnspacing=0.8,handletextpad=0.5, loc=legacyPositionDict[subFigId])#显示图例，即label
    plt.yticks(fontsize=18)
    plt.xlabel('Recovery Ratio(%)', fontsize=22)
    plt.xlim(0, 3*totalGroupNum)
    plt.xticks([x*3+1.5 for x in range(totalGroupNum)], dataDict[curModelName]['x-arr'], fontsize=18)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
    plt.grid(True, linestyle='-.', axis='y')

    # 第三幅子图
    plt.subplot(313)
    legendArr = []
    legendEntryArr = []
    bp = plt.boxplot(dataDict[curModelName]['PRM-PPR'], positions=[x*3+1 for x in range(totalGroupNum)], widths=bar_width, patch_artist=True)
    legendArr.append(bp["boxes"][0])
    legendEntryArr.append('PRM-PPR')
    # plt.bar([],[], color='white', linewidth=2, edgecolor=colorDict['PRM-Typical'], hatch='//////')
    setBoxplotStyle(bp, 'PRM-PPR')
    plt.plot([x*3+1 for x in range(totalGroupNum)], [medline.get_ydata()[0] for medline in bp['medians']], \
        lw=line_width, color=colorDict['PRM-PPR'], alpha=0.9, ls='-')

    bp = plt.boxplot(dataDict[curModelName]['PPR'], positions=[x*3+2 for x in range(totalGroupNum)], widths=bar_width, patch_artist=True)
    legendArr.append(bp["boxes"][0])
    legendEntryArr.append('PPR')
    # plt.bar([],[], color='white', linewidth=2, edgecolor=colorDict['Typical'], hatch='//////')
    setBoxplotStyle(bp, 'PPR')
    plt.plot([x*3+2 for x in range(totalGroupNum)], [medline.get_ydata()[0] for medline in bp['medians']], \
        lw=line_width, color=colorDict['PPR'], alpha=0.9, ls='-')

    plt.ylabel('acc(%)', fontsize=22)
    plt.legend(legendArr, legendEntryArr, fontsize=18,ncol=2,columnspacing=0.8,handletextpad=0.5, loc=legacyPositionDict[subFigId])#显示图例，即label
    plt.yticks(fontsize=18)
    plt.xlabel('Recovery Ratio(%)', fontsize=22)
    plt.xlim(0, 3*totalGroupNum)
    plt.xticks([x*3+1.5 for x in range(totalGroupNum)], dataDict[curModelName]['x-arr'], fontsize=18)#显示x坐r标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
    plt.grid(True, linestyle='-.', axis='y')



    plt.subplots_adjust(left=0.085, right=0.98, top=0.99, bottom=0.07, hspace=0.295)#图片的页边距

    plt.savefig('RS(6,3)_4_model_GAN_%s_box_line.pdf' % (curModelName))
    plt.show()
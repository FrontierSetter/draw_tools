import argparse
from cmath import inf

parser = argparse.ArgumentParser(description='画性能图')
parser.add_argument('-f','--file')
args = parser.parse_args()

inFile = open("%s.CSV" % (args.file), 'r', encoding='UTF-8')

curLine = inFile.readline()
nameArr = curLine.strip('\n').split(',')

dataArr = []
for i in range(len(nameArr)):
    dataArr.append([])

while True:
    curLine = inFile.readline()

    if curLine == '':
        break
    
    curArr = curLine.strip('\n').split(',')
    
    for i in range(1, len(nameArr)):
        dataArr[i].append(float(curArr[i]))
    
    dataArr[0].append(curArr[0])

    dataArr[3][-1] *= 100
    dataArr[4][-1] *= (32/100)
    dataArr[5][-1] *= (47/100)
    dataArr[6][-1] /= (1024*1024*1024*1024)

yIndexArr = [0,0,0,1,1,1]

legendArrStr = '['
for i in range(1, len(nameArr)):
    legendArrStr += ('\''+nameArr[i]+'\',')
legendArrStr += ']'

seriesDataArr = []
for i in range(1, len(dataArr)):
    seriesDataArr.append('[')
    for j in range(len(dataArr[i])):
        seriesDataArr[-1] += ('[\'%s\', %f],' % (dataArr[0][j], dataArr[i][j]))
    seriesDataArr[-1] += ']'

suffixDic = {
    'zhoushan': '（舟山电信）',
    'wenzhou':'（温州移动）',
    'wuxi':'（无锡联通）',
    'santong':'（舟山电信+温州移动+无锡联通）',
}

chartName = ""
for suf in suffixDic.keys():
    if suf in args.file:
        chartName += suffixDic[suf]
        break

outHtml = open("%s.html" % (args.file), 'w', encoding='UTF-8')

outHtml.write("<!--\n")
outHtml.write("  THIS EXAMPLE WAS DOWNLOADED FROM https://echarts.apache.org/examples/zh/editor.html?c=line-stack\n")
outHtml.write("-->\n")
outHtml.write("<!DOCTYPE html>\n")
outHtml.write("<html lang=\'zh-CN\' style=\'height: 100%\'>\n")
outHtml.write("\n")
outHtml.write("<head>\n")
outHtml.write("    <meta charset=\'utf-8\'>\n")
outHtml.write("</head>\n")
outHtml.write("\n")
outHtml.write("<body style=\'height: 100%; margin: 0\'>\n")
outHtml.write("    <div id=\'container\' style=\'height: 100%\'></div>\n")
outHtml.write("\n")
outHtml.write("\n")
outHtml.write("    <script type=\'text/javascript\' src=\'https://cdn.jsdelivr.net/npm/echarts@5.3.2/dist/echarts.min.js\'></script>\n")
outHtml.write("\n")
outHtml.write("    <script type=\'text/javascript\'>\n")
outHtml.write("        var dom = document.getElementById(\'container\');\n")
outHtml.write("        var myChart = echarts.init(dom, null, {\n")
outHtml.write("            renderer: \'canvas\',\n")
outHtml.write("            useDirtyRect: false\n")
outHtml.write("        });\n")
outHtml.write("        var app = {};\n")
outHtml.write("\n")
outHtml.write("        var option;\n")
outHtml.write("\n")
outHtml.write("        option = {\n")
outHtml.write("            title: {\n")
outHtml.write("                text: \'"+chartName+"\'\n")
outHtml.write("            },\n")
outHtml.write("            tooltip: {\n")
outHtml.write("                trigger: \'axis\'\n")
outHtml.write("            },\n")
outHtml.write("            legend: {\n")
outHtml.write("                type: \'scroll\',\n")
outHtml.write("                orient: \'horizontal\',\n")
outHtml.write("                top: 25,\n")
outHtml.write("                right: \'10%\',\n")
outHtml.write("                left: \'10%\',\n")
outHtml.write("                data: "+legendArrStr+",\n")
outHtml.write("            },\n")
outHtml.write("            grid: {\n")
outHtml.write("                top: \'15%\',\n")
outHtml.write("                left: \'5%\',\n")
outHtml.write("                right: \'5%\',\n")
outHtml.write("                bottom: \'8%\',\n")
outHtml.write("                y2: \'5%\',\n")
outHtml.write("                containLabel: true\n")
outHtml.write("            },\n")
outHtml.write("            toolbox: {\n")
outHtml.write("                right: \'5%\',\n")
outHtml.write("                feature: {\n")
outHtml.write("                    saveAsImage: {}\n")
outHtml.write("                }\n")
outHtml.write("            },\n")
outHtml.write("            xAxis: [{\n")
outHtml.write("                type: \'time\',\n")
outHtml.write("                boundaryGap: false,\n")
outHtml.write("            },\n")
outHtml.write("            ],\n")
outHtml.write("            dataZoom: [\n")
outHtml.write("                {\n")
outHtml.write("                    xAxisIndex: 0,\n")
outHtml.write("                    filterMode: \'none\',\n")
outHtml.write("                    type: \'inside\',\n")
outHtml.write("                },\n")
outHtml.write("                {\n")
outHtml.write("                    xAxisIndex: 0,\n")
outHtml.write("                    filterMode: \'none\',\n")
outHtml.write("                },\n")
outHtml.write("                {\n")
outHtml.write("                    yAxisIndex: 0,\n")
outHtml.write("                    type: \'inside\',\n")
outHtml.write("                    filterMode: \'none\',\n")
outHtml.write("                },\n")
outHtml.write("                {\n")
outHtml.write("                    yAxisIndex: 0,\n")
outHtml.write("                    filterMode: \'none\',\n")
outHtml.write("                },\n")
outHtml.write("            ],\n")
outHtml.write("         yAxis: [{");
outHtml.write("				name: \'回源率(%)\',");
outHtml.write("				type: \'value\',");
outHtml.write("				axisLabel: {");
outHtml.write("					show: true,");
outHtml.write("					interval: \'auto\',");
outHtml.write("					formatter: \'{value} %\'");
outHtml.write("				},");
outHtml.write("			},");
outHtml.write("			{");
outHtml.write("				name: \'存储量(TB)\',");
outHtml.write("				type: \'value\',");
outHtml.write("				offset: 80,");
outHtml.write("				axisLabel: {");
outHtml.write("					show: true,");
outHtml.write("					interval: \'auto\',");
outHtml.write("					formatter: \'{value} TB\'");
outHtml.write("				},");
outHtml.write("				splitNumber: 10,");
outHtml.write("				splitLine: {");
outHtml.write("					show: true,");
outHtml.write("					lineStyle: {");
outHtml.write("						type: \'dashed\'");
outHtml.write("					}");
outHtml.write("				},");
outHtml.write("				splitArea: {");
outHtml.write("					show: false");
outHtml.write("				},");
outHtml.write("			}],");
outHtml.write("            series: [\n")

for i in range(len(seriesDataArr)):
    outHtml.write("                {\n")
    outHtml.write("                    name: \'"+nameArr[i+1]+"\',\n")
    outHtml.write("                    type: \'line\',\n")
    outHtml.write("                    symbol: \'emptyCircle\',\n")
    outHtml.write("                    showAllSymbol: true,\n")
    outHtml.write("                    symbolSize: 3,\n")
    outHtml.write("                    smooth: true,\n")
    outHtml.write("                    yAxisIndex: "+str(int(yIndexArr[i]))+",\n")
    outHtml.write("                    data:"+seriesDataArr[i]+"\n")
    outHtml.write("                },\n")

outHtml.write("            ]\n")
outHtml.write("        };\n")
outHtml.write("\n")
outHtml.write("        if (option && typeof option === \'object\') {\n")
outHtml.write("            myChart.setOption(option);\n")
outHtml.write("        }\n")
outHtml.write("\n")
outHtml.write("        window.addEventListener(\'resize\', myChart.resize);\n")
outHtml.write("    </script>\n")
outHtml.write("</body>\n")
outHtml.write("\n")
outHtml.write("</html>\n")
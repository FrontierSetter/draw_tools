import plotly.graph_objects as go
import pandas as pd
import plotly.offline as offline
import sys
import argparse
from plotly.subplots import make_subplots

# 通用画图脚本，输入多个csv文件，各自包含x/y/group，画图

parser = argparse.ArgumentParser(
                    description='自动化处理trace',
                    epilog='version 0.2')
parser.add_argument('--in_file', dest="inFileNameArr", nargs='+', type=str, help='input file path')
parser.add_argument('--out_file', type=str, help='out file path')
args = parser.parse_args()

inFileNameArr = args.inFileNameArr
outFileName = args.out_file

fig = make_subplots(rows=len(inFileNameArr), cols=1, shared_xaxes=True, 
                    subplot_titles=inFileNameArr)

curPIdx = 0
for curFileNameIdx in range(len(inFileNameArr)):
    curFileName = inFileNameArr[curFileNameIdx]

    curDF = pd.read_csv(curFileName)

    curPIdx += 1
    for group in curDF['group'].unique():
        group_data = curDF[curDF['group'] == group]
        fig.add_trace(go.Scatter(
            x=group_data['x'],
            y=group_data['y'],
            name=str(group)
        ), row=curPIdx, col=1)

offline.plot(fig, filename=outFileName, auto_open=True)
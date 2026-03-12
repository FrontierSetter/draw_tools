import plotly.graph_objects as go
import pandas as pd
import plotly.offline as offline
import sys
import argparse
from plotly.subplots import make_subplots
from datetime import datetime

# 通用画图脚本，把x列按照给定的秒数求均值

parser = argparse.ArgumentParser(
                    description='自动化处理trace',
                    epilog='version 0.2')
parser.add_argument('--in_file', type=str, help='out file path')
parser.add_argument('--out_file', type=str, help='out file path')
parser.add_argument('--second', type=int, help='out file path')

args = parser.parse_args()

inFileName = args.in_file
outFileName = args.out_file
avgSecond = args.second

rawDF = pd.read_csv(inFileName)
resultData = []
prevTime = 0
prevValue = 0

for index, rowData in rawDF.iterrows():
    curTimeStamp = datetime.strptime(rowData['x'], '%Y-%m-%d %H:%M:%S').timestamp()
    targetTimeStamp = curTimeStamp - (curTimeStamp % avgSecond)

    if index == 0:
        prevTime = targetTimeStamp
    
    if targetTimeStamp != prevTime:
        resultData.append({'x': datetime.fromtimestamp(prevTime).strftime('%Y-%m-%d %H:%M:%S'), 'y': prevValue, 'group':  rowData['group']})
        prevTime = targetTimeStamp
        prevValue = 0

    prevValue += rowData['y']

df = pd.DataFrame(resultData)
df.to_csv(outFileName, index=False)
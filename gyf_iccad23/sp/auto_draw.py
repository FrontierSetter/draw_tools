import argparse
import os

parser = argparse.ArgumentParser(description='画性能图')
parser.add_argument('-f','--file')
args = parser.parse_args()

# bashArr = ['TPR', 'FPR', 'AUC', 'Accuracy', 'F1', 'Precision']
bashArr = ['TPR', 'FPR', 'AUC', 'F1']

for bashFile in bashArr:
    commandStr = 'python %s.py -f %s' % (bashFile, args.file)
    print(commandStr)
    os.system(commandStr)
    print()
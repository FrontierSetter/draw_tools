import os
import argparse

parser = argparse.ArgumentParser(description='画性能图')
parser.add_argument('-f','--file')
args = parser.parse_args()

fileArr = [
    'auc.py',
    'tpr.py',
    'fpr.py',
    'f1_1.py',
    # 'auc_single.py',
    # 'tpr_single.py',
    # 'fpr_single.py',
]

for curBash in fileArr:
    os.system("%s -f %s" % (curBash, args.file))
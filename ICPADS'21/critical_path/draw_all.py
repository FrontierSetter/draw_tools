import sys, os

perfix = ['alloc', 'free']
workload = ['ramspeed', 'scalability', 'sysbench', 'stream', 'threadtest']

for p in perfix:
    for w in workload:
        os.system('python %s_%s.py' % (p, w))
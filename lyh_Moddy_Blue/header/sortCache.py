import functools

def sortCache(c1, c2):
    n1 = c1.split('_')[0]
    n2 = c2.split('_')[0]

    if n1 == n2:
        capatity1 = int(c1.split('_')[1][:-1])
        capatity2 = int(c2.split('_')[1][:-1])
        if capatity1 > capatity2:
            return 1
        else:
            return -1        
    else:
        if n1 > n2:
            return 1
        else:
            return -1
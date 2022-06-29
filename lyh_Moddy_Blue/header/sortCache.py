import functools

def sortCache(c1, c2):
    arr1 = c1.split('_')
    arr2 = c2.split('_')
    n1 = arr1[0]
    n2 = arr2[0]

    capatity1 = int(arr1[-1][:-1])
    capatity2 = int(arr2[-1][:-1])

    p1 = 1
    p2 = 1
    if len(arr1) != 2:
        p1 = int(arr1[1])
    if len(arr2) != 2:
        p2 = int(arr2[1])

    if n1 == n2:
        if capatity1 == capatity2:
            if p1 > p2:
                return 1
            else:
                return -1
        else:
            if capatity1 > capatity2:
                return 1
            else:
                return -1        
    else:
        if n1 > n2:
            return 1
        else:
            return -1
def getMarkerArr(targetLen, targetNum):
    gap = int(targetLen / targetNum)
    if gap < 1:
        gap = 1
    resultArr = [x for x in range(0, targetLen, gap)]
    if resultArr[-1] != targetLen-1:
        if targetLen-1-resultArr[-1] < gap/3:
            resultArr.pop()
        resultArr.append(targetLen-1)
    print("gap: %d->%d, markerNum: %d" % (int(targetLen / targetNum), gap, len(resultArr)))
    return resultArr

def isIncrement(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return true
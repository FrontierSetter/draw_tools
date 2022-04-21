def strToS(tStr):
    tNum = int(tStr[:-1])
    tUnit = tStr[-1]
    if tUnit == 's':
        return tNum
    elif tUnit == 'm':
        return tNum*60;
    elif tUnit == 'h':
        return tNum*60*60;

def sToStr(tNum):
    tUnitArr = ['s', 'm', 'h']
    tUnitIdx = 0
    while tNum % 60 == 0 and tUnitIdx < len(tUnitArr)-1:
        tNum /= 60
        tNum = int(tNum)
        tUnitIdx += 1
    return str(tNum)+tUnitArr[tUnitIdx]
import os

def getFileName(filePath):
    (filepath, tempfilename) = os.path.split(filePath)
    (filename, extension) = os.path.splitext(tempfilename)
    return filename
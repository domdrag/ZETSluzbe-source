
def readWarningMessage():
    fileR = open('data/data/warnings.txt', 'r', encoding='utf-8')
    lines = fileR.readlines()
    fileR.close()
    return lines

import re

def isAlphaWithSpaces(x):
    if(x == ''):
        return False
    y = re.split('\n|\.| ',x)
    for el in y:
        if(el == ''):
            continue
        if(not el.isalpha()):
            return False
    return True

def getServiceLayout(serviceLine, serviceNum, days, day):
    if(len(serviceLine) == 1):
        if serviceLine[0] == '' or serviceLine[0] == ' ':
            return [days[day], 'empty']
        return [days[day], serviceLine[0]]
    serviceLayout = []
    serviceStartIndex = 0
    if(not serviceNum.isnumeric()):
        serviceLayout.append(days[day])
        serviceLayout.append(serviceNum)
        return [days[day], 'empty']
    if(serviceLine == []):
        return [days[day], 'empty']
    if(any(x is None for x in serviceLine)):
        return [days[day], 'empty']
    if(serviceLine[8] == serviceNum):
        serviceStartIndex = 8
    if(serviceLine[15] == serviceNum):
        serviceStartIndex = 15
    if(serviceLine[serviceStartIndex+2] == ''):
        return [days[day], 'empty']
    
    serviceNumber = serviceLine[serviceStartIndex]
    driveOrder = serviceLine[serviceStartIndex+1]
    receptionPoint = serviceLine[serviceStartIndex+2].replace('\n',' ')
    receptionPoint = re.sub(' +', ' ', receptionPoint)  
    receptionTime = serviceLine[serviceStartIndex+3]
    releaseTime = serviceLine[serviceStartIndex+4]

    if('\n' in receptionTime): # dvokratne
        startingTimes = re.split('\n| ', receptionTime)
        startingTimes = list(filter(('').__ne__, startingTimes))
        if(len(startingTimes[0]) == 1):
            startingTimes[0] = startingTimes[0] + startingTimes[1]
            del startingTimes[1]
        receptionTime = startingTimes[0] + ', ' + startingTimes[1]

        startingTimes = re.split('\n| ', releaseTime)
        startingTimes = list(filter(('').__ne__, startingTimes))
        if(len(startingTimes[0]) == 1):
            startingTimes[0] = startingTimes[0] + startingTimes[1]
            del startingTimes[1]
        releaseTime = startingTimes[0] + ', ' + startingTimes[1]
        
        startingPlaces = re.split(' ', receptionPoint)
        startingPlaces = list(filter(('').__ne__, startingPlaces))
        receptionPoint = startingPlaces[0]
        releasePoint = startingPlaces[1]

    elif(driveOrder == ''): # pricuva
        driveOrder = 'PRIČUVA'
        releasePoint = receptionPoint
        
    else:
        releasePoint = 'PTD/PTT'
        for element in serviceLine[serviceStartIndex+3:]:
            if(isAlphaWithSpaces(element)):
                releasePoint = element.replace('\n',' ')
                releasePoint = re.sub(' +', ' ', releasePoint) 
                break
    
            
    # slaganje za layout
    serviceLayout = []
    serviceLayout.append(days[day])
    serviceLayout.append('broj sluzbe: ' + serviceNumber)
    serviceLayout.append('vozni red: ' + driveOrder)
    serviceLayout.append(receptionTime + ', ' + receptionPoint)
    serviceLayout.append(releaseTime + ', ' + releasePoint)
    return serviceLayout
    

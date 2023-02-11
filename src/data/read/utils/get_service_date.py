import re
from datetime import date

def getServiceDate(service):
    serviceDate = (re.split(' ', service[0]))[1]
    firstDot = serviceDate.index('.')
    secondDot = firstDot+1 + serviceDate[firstDot+1:].index('.')
    thirdDot = secondDot+1 + serviceDate[secondDot+1:].index('.')
    day = int(serviceDate[0:firstDot])
    month = int(serviceDate[firstDot+1:secondDot])
    year = int(serviceDate[secondDot+1:thirdDot])
    serviceRealDate = date(year, month, day)
    return serviceRealDate

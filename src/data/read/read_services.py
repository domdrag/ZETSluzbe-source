import ast

from src.data.read.utils.check_service_date_validity import (
    checkServiceDateValidity
    )

def readServices(offNum):
    filePath = 'data/data/all_services_by_driver_decrypted/' + offNum + '.txt'
    weekServices = ''
    
    try:
        fileR = open(filePath, 'r', encoding='utf-8')
        weekServices = fileR.readlines()
        fileR.close()
    except:
        return []
    
    weekServicesData = []
    for weekServiceRawString in weekServices:
        weekService = ast.literal_eval(weekServiceRawString)
        if(not checkServiceDateValidity(weekService)):
           continue
        if(len(weekService) == 2):
            bgColor = (0.13, 0.55, 0.13, 1)
            if(weekService[1] == 'empty' or
               weekService[1] == '' or # za svaki slucaj case-vi
               weekService[1] == ' '):
                bgColor = (0.545, 0, 0, 1)
            weekServicesData.append({'day': weekService[0],
                                     'service': '\n'.join(weekService[1:]),
                                     'bg_color': bgColor})
        else:
            weekServicesData.append({'day': weekService[0],
                                     'service': '\n'.join(weekService[1:]),
                                     'bg_color': (0, 0, 1, 1)})
    return weekServicesData


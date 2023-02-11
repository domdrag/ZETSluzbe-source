import ast

from src.data.admin.collect.utils.get_service_layout import getServiceLayout
from src.data.admin.collect.utils.get_service_line import getServiceLine

def writeDecryptedServices(days, weekSchedule):
    fileR = open('data/data/week_services_by_driver_encrypted.txt',
                 'r',
                 encoding='utf-8')
    weekServicesALL = fileR.readlines()
    fileR.close()
    for weekServicesRaw in weekServicesALL:
        weekServices = ast.literal_eval(weekServicesRaw)
        offNum = int(weekServices[0])
        filePath = 'data/data/all_services_by_driver_decrypted/' \
                    + str(offNum) \
                    + '.txt'
        fileW = open(filePath, 'a', encoding='utf-8')
        for i in range(1,8):
            serviceNum = weekServices[i]
            serviceLine = getServiceLine(serviceNum, i-1, weekSchedule)
            serviceLayout = getServiceLayout(serviceLine, serviceNum, days, i-1)
            fileW.write(f"{serviceLayout}\n")
        fileW.close()

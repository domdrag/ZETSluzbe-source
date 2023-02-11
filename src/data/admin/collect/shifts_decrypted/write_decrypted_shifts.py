import ast

from src.data.admin.collect.shifts_decrypted.utils.get_driver_info import (
    getDriverInfo
    )
from src.data.admin.collect.utils.get_service_layout import getServiceLayout
from src.data.admin.collect.utils.get_service_line import getServiceLine

def writeDecryptedShifts(days, weekSchedule):
    fileR = open('data/data/week_services_by_driver_encrypted.txt',
                 'r',
                 encoding='utf-8')
    weekServicesALL = fileR.readlines()
    fileR.close()

    fileR = open('data/data/all_drivers.txt', 'r', encoding='utf-8')
    driversRaw = fileR.readlines()
    fileR.close()
    driverList = []
    for driverRaw in driversRaw:
        driver = driverRaw.split()
        driverList.append(driver)
        
    for weekServicesRaw in weekServicesALL:
        weekServices = ast.literal_eval(weekServicesRaw)
        offNum = int(weekServices[0])
        filePath = 'data/data/all_shifts_by_driver_decrypted/' \
                    + str(offNum) \
                    + '.txt'
        fileW = open(filePath, 'a', encoding='utf-8')        
        for i in range(1,8):
            serviceNum = weekServices[i]
            serviceLine = getServiceLine(serviceNum, i-1, weekSchedule)
            if(len(serviceLine) == 1):
                serviceLayout = getServiceLayout(serviceLine,
                                                 serviceNum,
                                                 days,
                                                 i-1)
                fileW.write(f"{serviceLayout}\n")
                continue
            if(serviceLine == []):
                fileW.write(f"{[days[i-1], 'UNABLE TO FIND SERVICE LINE']}\n")
                continue
            for j in [0,8,15]:
                wantedServiceNum = serviceLine[j]
                serviceLayout = getServiceLayout(serviceLine,
                                                 wantedServiceNum,
                                                 days,
                                                 i-1)
                if(serviceLayout[1] == 'empty'):
                    fileW.write(f"{serviceLayout}\n")
                    continue
                driverInfo = getDriverInfo(wantedServiceNum, driverList, i)
                serviceLayout.append(driverInfo[0] + '\n' + driverInfo[1])
                fileW.write(f"{serviceLayout}\n")
        fileW.close()

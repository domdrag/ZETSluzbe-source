import ast

def getDriverInfo(serviceNum, driverList, day):
    fileR = open('data/data/week_services_by_driver_encrypted.txt',
                 'r',
                 encoding='utf-8')
    weekServicesALL = fileR.readlines()
    fileR.close()
    wantedOffNum = -1
    for weekServicesRaw in weekServicesALL:
        weekServices = ast.literal_eval(weekServicesRaw)
        if(weekServices[day] == serviceNum):
            wantedOffNum = int(weekServices[0])
            break
        
    if(wantedOffNum == -1):
        return ['ANON', 'XXX-XXX-XXXX']

    for driver in driverList:
        if(driver[0] == str(wantedOffNum)):
            driverName = driver[1] + ' ' + driver[2][:-1]
            telNum = driver[3]
            driverTelNumber = f"{telNum[:3]}-{telNum[3:6]}-{telNum[6:]}"
            return [driverName, driverTelNumber]
    return ['ANON', 'XXX-XXX-XXXX']

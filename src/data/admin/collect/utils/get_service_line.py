import ast

def getServiceLine(serviceNum, day, weekSchedule):
    if(not serviceNum.isnumeric()):
        return [serviceNum]
    if(weekSchedule[day] == 'W'):
        fileR = open('data/data/rules_work_day.txt', 'r', encoding='utf-8')
    elif(weekSchedule[day] == 'St'):
        fileR = open('data/data/rules_saturday.txt', 'r', encoding='utf-8')
    else:
        fileR = open('data/data/rules_sunday.txt', 'r', encoding='utf-8')
    serviceLines = fileR.readlines()
    fileR.close()
    for serviceLine in serviceLines:
        serviceLine = ast.literal_eval(serviceLine)
        if(serviceNum in serviceLine):
            return serviceLine
    return []

from datetime import date
import ast

from src.data.read.utils.get_today_date import getTodayDate

MAX_ALLOWED_DATE_DIFF = 3 # friday - monday = 4

def updateRequiredDateCheck():
    todayDate = getTodayDate()
    fileR = open('data/dropbox/last_record_date.txt', 'r')
    rawDateString = (fileR.readlines())[0]
    fileR.close()
    rawDateList = ast.literal_eval(rawDateString)

    lastRecordDate = date(int(rawDateList[0]),
                          int(rawDateList[1]),
                          int(rawDateList[2]))

    dateDiff = todayDate - lastRecordDate
    if dateDiff.days > MAX_ALLOWED_DATE_DIFF:
        return True
    return False

from datetime import date
import datetime

def getTodayDate():
    now = datetime.datetime.now()
    todayDate = date(now.year, now.month, now.day)
    return todayDate

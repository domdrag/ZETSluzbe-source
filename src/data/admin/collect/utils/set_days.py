import pdfplumber
import datetime
import re
import ast
from datetime import date
from dateutil.relativedelta import relativedelta, FR

from src.data.admin.collect.utils.download_pdf_file import downloadPDFFile

firstURL = ("https://www.zet.hr/interno/UserDocsImages/tp%20dubrava/"
            "Slu%C5%BEbe%20za%20sve%20voza%C4%8De/tpd.pdf")

def getStringDate(date):
    return str(date.day) + '.' + str(date.month) + '.' + str(date.year) + '.'

def getDays(days, textFirstPDF):
    odIndex = textFirstPDF.find('od')
    stringForMonth = textFirstPDF[odIndex:odIndex+50]
    stringForMonthList = re.split(' |\.', stringForMonth)
    day = stringForMonthList[1]
    month = stringForMonthList[2]
    year = stringForMonthList[3]
    mondayDate = date(int(year), int(month), int(day))
    mondayDate + datetime.timedelta(days = 1)

    fileR = open('data/data/last_record_date.txt', 'r', encoding='utf-8')
    line = fileR.readline()
    fileR.close()
    lastRecordDateList = ast.literal_eval(line)
    lastRecordedDate = date(lastRecordDateList[0],
                            lastRecordDateList[1],
                            lastRecordDateList[2])

    if(mondayDate == lastRecordedDate):
        return {'mondayDate': mondayDate, 'updateNeeded': False}

    monday = 'Ponedjeljak, ' + getStringDate(mondayDate)
    nextDate = mondayDate + datetime.timedelta(days = 1)
    tuesday = 'Utorak, ' + getStringDate(nextDate)
    nextDate = nextDate + datetime.timedelta(days = 1)
    wednesday = 'Srijeda, ' + getStringDate(nextDate)
    nextDate = nextDate + datetime.timedelta(days = 1)
    thursday = 'Cetvrtak, ' + getStringDate(nextDate)
    nextDate = nextDate + datetime.timedelta(days = 1)
    friday = 'Petak, ' + getStringDate(nextDate)
    nextDate = nextDate + datetime.timedelta(days = 1)
    saturday = 'Subota, ' + getStringDate(nextDate)
    nextDate = nextDate + datetime.timedelta(days = 1)
    sunday = 'Nedjelja, ' + getStringDate(nextDate)

    days.append(monday)
    days.append(tuesday)
    days.append(wednesday)
    days.append(thursday)
    days.append(friday)
    days.append(saturday)
    days.append(sunday)
    return {'mondayDate': mondayDate, 'updateNeeded': True}

def setDays(days):
    PDFFile = downloadPDFFile(firstURL, 'tpd.pdf')
    with pdfplumber.open(PDFFile) as PDF:
        page = PDF.pages[0]
        textFirstPDF = page.extract_text()
    return getDays(days, textFirstPDF)

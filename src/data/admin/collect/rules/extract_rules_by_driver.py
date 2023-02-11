import pdfplumber

from src.data.admin.collect.rules.utils.determine_week_schedule import (
    determineWeekSchedule
    )

def extractRulesByDriver(weekSchedule):
    PDFFile = 'data/data/tpd.pdf' # downloaded in setDays util
    with pdfplumber.open(PDFFile) as PDF:
        determineWeekSchedule(PDF.pages[0], weekSchedule)       
        fileW = open('data/data/week_services_by_driver_encrypted.txt',
                     'w',
                     encoding='utf-8')
        for page in PDF.pages:            
            tables = page.dedupe_chars().find_tables()
            for tableId in tables:
                table = tableId.extract()
                for services in table:
                    if(isinstance(services[0], str) and services[0].isnumeric()):
                        if(not services[0]):
                            continue
                        fileW.write(f"{services[0:8]}\n")
                        if(not services[8]):
                            continue
                        fileW.write(f"{services[8:]}\n")
        fileW.close()

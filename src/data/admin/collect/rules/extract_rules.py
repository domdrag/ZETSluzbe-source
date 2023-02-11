import pdfplumber

from src.data.admin.collect.utils.download_pdf_file import downloadPDFFile

#### pomogao jsvine
def extractRule(typeOfDay, URL, fileName):
    PDFFile = downloadPDFFile(URL, fileName)
    with pdfplumber.open(PDFFile) as PDF:
        fileW = open('data/data/rules_' + typeOfDay + '.txt',
                     'w',
                     encoding='utf-8')
        for page in PDF.pages:
            filtered = (page.filter(
                lambda obj: not (obj.get("non_stroking_color") == (0, 0, 1)
                                 and
                                 obj.get("width", 100) < 100)).dedupe_chars())
            tables = filtered.extract_tables()
            for table in tables:
                for serviceLine in table:
                    if(isinstance(serviceLine[0], str)
                       and serviceLine[0].isnumeric()):
                        fileW.write(f"{serviceLine}\n")
    fileW.close()
####

def extractRules(workDayURL, saturdayURL, sundayURL):
    extractRule('work_day', workDayURL, 'workDay.pdf')
    extractRule('saturday', saturdayURL, 'saturday.pdf')
    extractRule('sunday', sundayURL, 'sunday.pdf')

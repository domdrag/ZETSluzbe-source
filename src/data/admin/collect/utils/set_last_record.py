
def setLastRecord(mondayDate):
    fileW = open('data/data/last_record_date.txt', 'w', encoding='utf-8')
    fileW.write(f"{[mondayDate.year, mondayDate.month, mondayDate.day]}\n")
    fileW.close()

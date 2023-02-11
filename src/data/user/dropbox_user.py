import dropbox
import ast

RFRSH_TOKEN = 'HIDDEN_INFO'

def updateNeeded():
    dbx = dropbox.Dropbox(app_key = 'HIDDEN_INFO',
                          app_secret = 'HIDDEN_INFO',
                          oauth2_refresh_token = RFRSH_TOKEN)
    
    dbx.files_download_to_file('data/dropbox/last_record_date.txt',
                               '/last_record_date.txt')
    fileR = open('data/data/last_record_date.txt', 'r')
    currentDate = fileR.read()
    currentDate = ast.literal_eval(currentDate)
    fileR.close()
    fileR = open('data/dropbox/last_record_date.txt', 'r')
    oldDate = fileR.read()
    oldDate = ast.literal_eval(oldDate)
    fileR.close()

    if currentDate == oldDate:
        return False
    return True


def downloadData():
    dbx = dropbox.Dropbox(app_key = 'HIDDEN_INFO',
                          app_secret = 'HIDDEN_INFO',
                          oauth2_refresh_token = RFRSH_TOKEN)
    dbx.files_download_to_file('data/dropbox/data.zip',
                               '/data.zip')
                               


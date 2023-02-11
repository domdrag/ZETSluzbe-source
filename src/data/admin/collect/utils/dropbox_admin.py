import dropbox

RFRSH_TOKEN = 'HIDDEN_INFO'
                               
def uploadData():
    dbx = dropbox.Dropbox(app_key = 'HIDDEN_INFO',
                          app_secret = 'HIDDEN_INFO',
                          oauth2_refresh_token = RFRSH_TOKEN)
    with open('data/dropbox/data.zip', 'rb') as f:
            dbx.files_upload(f.read(),
                             '/data.zip',
                             mode = dropbox.files.WriteMode.overwrite)
    with open('data/data/last_record_date.txt', 'rb') as f:
            dbx.files_upload(f.read(),
                             '/last_record_date.txt',
                             mode = dropbox.files.WriteMode.overwrite)


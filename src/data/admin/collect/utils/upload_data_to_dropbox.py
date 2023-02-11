from src.data.admin.collect.utils.dropbox_admin import uploadData
from src.data.admin.collect.utils.compress_util import compressData

def uploadDataToDropbox():
    compressData()
    uploadData()

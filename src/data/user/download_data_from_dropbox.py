from src.data.user.dropbox_user import (
    downloadData,
    updateNeeded
    )
from src.data.user.decompress_util import decompressData

def downloadDataFromDropbox():
    if updateNeeded():
        downloadData()
        decompressData()


import shutil

def decompressData():
    shutil.unpack_archive('data/dropbox/data.zip', 'data/data')
    

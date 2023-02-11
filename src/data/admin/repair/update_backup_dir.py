from distutils.dir_util import copy_tree

def updateBackupDir():
    copy_tree('data/data',
              'data/backup_admin')


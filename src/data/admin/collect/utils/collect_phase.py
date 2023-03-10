from enum import Enum

class CollectPhase(Enum):
    SEARCH_LINKS = 0
    SET_DAYS = 1
    DELETE_NECESSARY_DATA = 2
    EXTRACT_RULES_BY_DRIVER = 3
    EXTRACT_RULES = 4
    WRITE_DECRYPTED_SERVICES = 5
    WRITE_DECRYPTED_SHIFTS = 6
    SET_LAST_RECORD = 7
    UPLOAD_DATA_TO_DROPBOX = 8
    END = 9

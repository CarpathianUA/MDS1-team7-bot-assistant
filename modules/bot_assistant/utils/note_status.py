from enum import Enum


class Status(Enum):
    NOTSTARTED = 1
    INPROGRESS = 2
    COMPLETED = 3
    POSTPONED = 4


def is_valid_status(status_string):
    try:
        status = Status[status_string]
        return True
    except:
        return False
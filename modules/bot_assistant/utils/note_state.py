from enum import Enum


class State(Enum):
    NOTSTARTED = 1
    INPROGRESS = 2
    COMPLETED = 3
    POSTPONED = 4


def is_valid_state(state_string_or_enum):
    if isinstance(state_string_or_enum, str):
        try:
            state = State[state_string_or_enum.upper()]
            return True
        except KeyError:
            return False
    elif isinstance(state_string_or_enum, State):
        return True
    return False

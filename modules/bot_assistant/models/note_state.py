from enum import Enum


class State(Enum):
    NOT_STARTED = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    POSTPONED = 4

    def __str__(self):
        if self == State.NOT_STARTED:
            return "not started"
        elif self == State.IN_PROGRESS:
            return "in progress"
        elif self == State.COMPLETED:
            return "completed"
        elif self == State.POSTPONED:
            return "postponed"


def is_valid_state(state_string_or_enum):
    if isinstance(state_string_or_enum, str):
        try:
            if State[state_string_or_enum.upper()]:
                return True
            else:
                return False
        except KeyError:
            return False
    elif isinstance(state_string_or_enum, State):
        return True
    return False

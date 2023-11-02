"""Module providing a note state model."""
from enum import Enum


class State(Enum):
    """Class representing a note state"""

    NOTSTARTED = 1
    INPROGRESS = 2
    COMPLETED = 3
    POSTPONED = 4


def is_valid_state(state_string_or_enum):
    """Function validates a state."""

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

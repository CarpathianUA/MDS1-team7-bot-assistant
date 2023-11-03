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

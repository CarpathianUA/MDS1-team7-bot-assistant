from modules.bot_assistant.models.exceptions import InvalidArgsError
from modules.bot_assistant.decorators.decorators import input_error


@input_error
def parse_input(user_input):
    if not user_input:
        raise InvalidArgsError
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

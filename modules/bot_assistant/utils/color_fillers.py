from modules.bot_assistant.constants.colors import COLOR_CODE, RESET_COLOR


def fill_background_color(input_string, target_sequence):
    output_string = ""
    target = str.lower(target_sequence)
    i = 0

    while i < len(input_string):
        if str.lower(input_string[i:i + len(target)]) == target:
            output_string += f"{COLOR_CODE}{str.upper(target)}{RESET_COLOR}"
            i += len(target)
        else:
            output_string += input_string[i]
            i += 1

    return output_string

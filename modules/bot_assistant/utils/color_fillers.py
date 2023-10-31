from modules.bot_assistant.constants.colors import COLOR_CODE, RESET_COLOR


def fill_background_color(input_string, target_sequence):
    output_string = ""
    i = 0

    while i < len(input_string):
        if input_string[i : i + len(target_sequence)] == target_sequence:
            output_string += f"{COLOR_CODE}{target_sequence}{RESET_COLOR}"
            i += len(target_sequence)
        else:
            output_string += input_string[i]
            i += 1

    return output_string

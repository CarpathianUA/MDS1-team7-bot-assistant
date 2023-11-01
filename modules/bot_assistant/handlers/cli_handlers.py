from modules.bot_assistant.constants.commands import (
    COMMANDS,
    CONTACT_COMMANDS,
    NOTES_COMMANDS,
    EXIT_COMMANDS,
    COMMANDS_INFO,
)


def show_help():
    command_col_width = max(len(command) for command in COMMANDS_INFO.keys()) + 2
    description_col_width = (
        max(len(description) for _, (description, _) in COMMANDS_INFO.items()) + 2
    )
    example_col_width = (
        max(len(example) for _, (_, example) in COMMANDS_INFO.items()) + 2
    )

    print(
        f"{'Command':<{command_col_width}} {'Description':<{description_col_width}} {'Example':<{example_col_width}}"
    )
    print("\n")

    for command, (description, example) in COMMANDS_INFO.items():
        print(
            f"{command:<{command_col_width}} {description:<{description_col_width}} {example:<{example_col_width}}"
        )
    print()


def execute_command(command, args, address_book, notes):
    if command in EXIT_COMMANDS:
        print("Good bye!")
        return True

    if command == "help":
        show_help()
        return False

    if command in CONTACT_COMMANDS:
        process_command(command, args, CONTACT_COMMANDS.get(command), address_book)
    elif command in NOTES_COMMANDS:
        process_command(command, args, NOTES_COMMANDS.get(command), notes)
    else:
        print("Invalid command. Available commands: " + ", ".join(COMMANDS.keys()))

    return False


def process_command(command, args, handler, entity):
    try:
        if command in ["hello", "all"]:
            print(handler(entity))  # no args for these commands
        else:
            print(
                handler(args, entity)
            )  # address_book is required for rest of the commands
    except TypeError as e:
        print(f"Error executing command {command}: {str(e)}")

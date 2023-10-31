from modules.bot_assistant.constants.commands import (
    COMMANDS,
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


def execute_command(command, args, address_book):
    if command in EXIT_COMMANDS:
        print("Good bye!")
        return True

    if command == "help":
        show_help()
        return False

    handler = COMMANDS.get(command)
    if handler:
        try:
            if command in ["hello", "all"]:
                print(handler(address_book))  # no args for these commands
            else:
                print(
                    handler(args, address_book)
                )  # address_book is required for rest of the commands
        except TypeError as e:
            print(f"Error executing command {command}: {str(e)}")
    else:
        print("Invalid command. Available commands: " + ", ".join(COMMANDS.keys()))

    return False

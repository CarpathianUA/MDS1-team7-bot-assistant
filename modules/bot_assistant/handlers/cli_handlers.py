from modules.bot_assistant.constants.commands import (
    COMMANDS,
    EXIT_COMMANDS,
    COMMANDS_INFO,
)


def show_help():
    print("Available commands:\n")
    print(f"{'Command':<15} {'Description':<40} {'Example':<40}")
    print("\n")
    for command, (description, example) in COMMANDS_INFO.items():
        print(f"{command:<15} {description:<40} {example:<40}")
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
            if command in ["hello", "all", "birthdays"]:
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

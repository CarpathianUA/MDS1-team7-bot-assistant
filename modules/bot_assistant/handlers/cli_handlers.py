from modules.bot_assistant.constants.commands import (
    COMMANDS,
    NOTES_COMMANDS,
    EXIT_COMMANDS,
    COMMANDS_INFO,
    NOTES_COMMANDS_INFO
)


def show_help():
    print("Available commands:\n")
    print("Contacts:")
    print(f"{'Command':<15} {'Description':<40} {'Example':<40}")
    print("\n")
    for command, (description, example) in COMMANDS_INFO.items():
        print(f"{command:<15} {description:<40} {example:<40}")
    print("\n")
    print("Notes:")
    for command, (description, example) in NOTES_COMMANDS_INFO.items():
        print(f"{command:<15} {description:<40} {example:<40}")
    print("\n")
    print()


def execute_command(command, args, address_book):
    if command in EXIT_COMMANDS:
        print("Good bye!")
        return True

    if command == "help":
        show_help()
        return False
    
    commands = COMMANDS.update(NOTES_COMMANDS)
    handler = commands.get(command)
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

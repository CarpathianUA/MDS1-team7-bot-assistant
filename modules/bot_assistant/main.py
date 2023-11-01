import modules.bot_assistant.handlers.cli_handlers as cli_handlers
from modules.bot_assistant.handlers.input_parsers import parse_input
from modules.bot_assistant.constants.commands import COMMANDS, EXIT_COMMANDS

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from modules.bot_assistant.models.address_book import AddressBook
from modules.bot_assistant.models.notes import Notes


def main():
    address_book = AddressBook.load_from_file()
    notes = Notes.load_from_file()

    print("Welcome to the assistant bot!")

    command_completer = WordCompleter(
        list(COMMANDS.keys()) + ["help"] + list(EXIT_COMMANDS), ignore_case=True
    )

    while True:
        user_input = prompt("Enter a command: ", completer=command_completer)
        command, *args = parse_input(user_input)

        if cli_handlers.execute_command(command, args, address_book, notes):
            address_book.save_to_file()
            break


if __name__ == "__main__":
    main()

import modules.bot_assistant.handlers.cli_handlers as cli_handlers
from modules.bot_assistant.handlers.input_parsers import parse_input
from modules.bot_assistant.models.address_book import AddressBook


def main():
    address_book = AddressBook.load_from_file()

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if cli_handlers.execute_command(command, args, address_book):
            address_book.save_to_file()
            break


if __name__ == "__main__":
    main()

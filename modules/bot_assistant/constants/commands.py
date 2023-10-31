from modules.bot_assistant.handlers import contact_handlers

COMMANDS = {
    "hello": contact_handlers.hello,
    "add": contact_handlers.add_contact,
    "delete": contact_handlers.delete_contact,
    "change": contact_handlers.change_contact,
    "phone": contact_handlers.get_contact_phone,
    "remove-phone": contact_handlers.remove_phone,
    "add-address": contact_handlers.add_address,
    "change-address": contact_handlers.change_address,
    "show-address": contact_handlers.show_address,
    "remove-address": contact_handlers.remove_address,
    "all": contact_handlers.get_all_contacts,
    "add-birthday": contact_handlers.add_birthday,
    "show-birthday": contact_handlers.show_birthday,
    "birthdays": contact_handlers.show_birthdays_per_week,
    "help": None,  # we define and call help in cli_handlers.py
}

COMMANDS_INFO = {
    "hello": ("Say hello to the bot.", "Example: hello"),
    "add": (
        "Add a new contact.",
        "Example: add AlanWake (that's a great game btw, try it!) 0987654321",
    ),
    "change": (
        "Change a one of contact's phones.",
        "Example: change AlanWake 0987654322",
    ),
    "delete": ("Delete a contact.", "Example: delete AlanWake"),
    "phone": (
        "Show a contact's phone.",
        "Example: phone AlanWake (don't try to call him, he's busy!)",
    ),
    "remove-phone": (
        "Remove a contact's phone.",
        "Example: remove-phone AlanWake 0987654321",
    ),
    "add-address": (
        "Add a contact's address",
        "Example: add-address AlanWake str.Sevchenko,18/5",
    ),
    "change-address": (
        "Change a contact's address",
        "Example: change-address AlanWake ave.Khmelnitsky,40/32",
    ),
    "show-address": ("Show a contact's address.", "Example: show-address AlanWake"),
    "remove-address": (
        "Remove a contact's address.",
        "Example: remove-address AlanWake",
    ),
    "all": ("Show all contacts.", "Example: all"),
    "add-birthday": (
        "Add a birthday to a contact.",
        "Example: add-birthday AlanWake 30.10.1982",
    ),
    "show-birthday": ("Show a contact's birthday.", "Example: show-birthday AlanWake"),
    "birthdays": ("Show all birthdays for the next week.", "Example: birthdays"),
    "help": ("Show this help message.", "Example: help"),
}

EXIT_COMMANDS = ("close", "exit", "quit", "bye")

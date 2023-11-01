from modules.bot_assistant.handlers import contact_handlers

COMMANDS = {
    "hello": contact_handlers.hello,
    "add": contact_handlers.add_contact,
    "delete": contact_handlers.delete_contact,
    "add-phone": contact_handlers.add_phone,
    "edit-phone": contact_handlers.edit_phone,
    "phone": contact_handlers.get_contact_phone,
    "remove-phone": contact_handlers.remove_phone,
    "add-address": contact_handlers.add_address,
    "edit-address": contact_handlers.edit_address,
    "address": contact_handlers.get_contact_address,
    "remove-address": contact_handlers.remove_address,
    "all": contact_handlers.get_all_contacts,
    "add-birthday": contact_handlers.add_birthday,
    "show-birthday": contact_handlers.show_birthday,
    "birthdays": contact_handlers.show_birthdays_per_period,
    "find": contact_handlers.find_contact,
    "help": None,  # we define and call help in cli_handlers.py
}

COMMANDS_INFO = {
    "hello": ("Say hello to the bot.", "Example: hello"),
    "add": (
        "Add a new contact.",
        "Example: add AlanWake (that's a great game btw, try it!) 0987654321",
    ),
    "add-phone": (
        "Add a phone to contact's phones list",
        "Example: add-phone AlanWake 0987654322",
    ),
    "delete": ("Delete a contact.", "Example: delete AlanWake"),
    "phone": (
        "Show a contact's phone.",
        "Example: phone AlanWake (don't try to call him, he's busy!)",
    ),
    "edit-phone": (
        "Edit a contact's phone number",
        "Example: edit-phone AlanWake 0987654321 0987654322",
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
        "Example: change-address AlanWake str.Sevchenko,18/5 ave.Khmelnitsky,40/32",
    ),
    "show-address": ("Show a contact's address.", "Example: show-address AlanWake"),
    "remove-address": (
        "Remove a contact's address.",
        "Example: remove-address AlanWake ave.Khmelnitsky,40/32"),
    "all": ("Show all contacts.", "Example: all"),
    "add-birthday": (
        "Add a birthday to a contact.",
        "Example: add-birthday AlanWake 30.10.1982",
    ),
    "show-birthday": ("Show a contact's birthday.", "Example: show-birthday AlanWake"),
    "birthdays": (
        "Show all birthdays for specified period in days. Default is 7 days.",
        "Example: birthdays 30",
    ),
    "help": ("Show this help message.", "Example: help"),
    "find": (
        "Shows all contacts that contain the entered characters.",
        "Example: find 050",
    ),
}

EXIT_COMMANDS = ("close", "exit", "quit", "bye")

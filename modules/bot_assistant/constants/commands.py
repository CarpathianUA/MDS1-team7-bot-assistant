from modules.bot_assistant.handlers import contact_handlers

COMMANDS = {
    "hello": contact_handlers.hello,
    "add": contact_handlers.add_contact,
    "edit": contact_handlers.edit_contact,
    "delete": contact_handlers.delete_contact,
    "add-phone": contact_handlers.add_phone,
    "edit-phone": contact_handlers.edit_phone,
    "show-phone": contact_handlers.get_contact_phone,
    "remove-phone": contact_handlers.remove_phone,
    "add-address": contact_handlers.add_address,
    "edit-address": contact_handlers.edit_address,
    "show-address": contact_handlers.get_contact_address,
    "remove-address": contact_handlers.remove_address,
    "all": contact_handlers.get_all_contacts,
    "add-birthday": contact_handlers.add_birthday,
    "remove-birthday": contact_handlers.remove_birthday,
    "show-birthday": contact_handlers.show_birthday,
    "add-email": contact_handlers.add_email,
    "show-email": contact_handlers.get_contact_email,
    "edit-email": contact_handlers.edit_email,
    "remove-email": contact_handlers.remove_email,
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
    "edit": (
        "Edit a contact's name",
        "Example: edit AlanWake AlanAwaken",
    ),
    "add-phone": (
        "Add a phone to contact's phones list",
        "Example: add-phone AlanWake 0987654322",
    ),
    "delete": ("Delete a contact.", "Example: delete AlanWake"),
    "show-phone": (
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
        "Example: add-address AlanWake 6A Bright Falls Ave",
    ),
    "edit-address": (
        "Change a contact's address",
        "Example: edit-address AlanWake 6A Bright Falls Ave 6A Bright Falls Ave, Bright Falls, WA",
    ),
    "show-address": ("Show a contact's address.", "Example: show-address AlanWake"),
    "remove-address": (
        "Remove a contact's address.",
        "Example: remove-address AlanWake 6A Bright Falls Ave",
    ),
    "add-email": (
        "Add an email to a contact.",
        "Example: add-email alanwake@remedy.com",
    ),
    "show-email": ("Shows an email of a contact.", "Example: show-email AlanWake"),
    "edit-email": (
        "Edits an email of a contact.",
        "Example: edit-email alanwake@email.com alanwake1@remedy.com",
    ),
    "remove-email": (
        "Remove a contact's email.",
        "Example: remove-email AlanWake alanwake@remedy.com",
    ),
    "all": ("Show all contacts.", "Example: all"),
    "add-birthday": (
        "Add a birthday to a contact.",
        "Example: add-birthday AlanWake 30.10.1982",
    ),
    "show-birthday": ("Show a contact's birthday.", "Example: show-birthday AlanWake"),
    "remove-birthday": (
        "Remove a contact's birthday.",
        "Example: remove-birthday AlanWake",
    ),
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

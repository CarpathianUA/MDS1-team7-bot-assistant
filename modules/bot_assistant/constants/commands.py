from modules.bot_assistant.handlers import contact_handlers, notes_handlers

COMMANDS = {
    "hello": contact_handlers.hello,
    "add": contact_handlers.add_contact,
    "delete": contact_handlers.delete_contact,
    "add-phone": contact_handlers.add_phone,
    "edit-phone": contact_handlers.edit_phone,
    "phone": contact_handlers.get_contact_phone,
    "remove-phone": contact_handlers.remove_phone,
    "all": contact_handlers.get_all_contacts,
    "add-birthday": contact_handlers.add_birthday,
    "show-birthday": contact_handlers.show_birthday,
    "birthdays": contact_handlers.show_birthdays_per_period,
    "find": contact_handlers.find_contact,
    "help": None,  # we define and call help in cli_handlers.py
}

NOTES_COMMANDS = {
    "add-note": notes_handlers.add_note,
    "add-tag": notes_handlers.add_tag,
    "add-text": notes_handlers.add_text,
    "delete-note": notes_handlers.delete_note,
    "edit-title": notes_handlers.edit_title,
    "edit-text": notes_handlers.edit_text,
    "remove-tag": notes_handlers.remove_tag,
    "notes": notes_handlers.get_all_notes,
    "find-note": notes_handlers.find_note,
    "find-note-filter": notes_handlers.find_note_by_filter,
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

NOTES_COMMANDS_INFO = {
    "add-note": (
        "Add a new note.",
        "Example: add-note Weather",
    ),
    "add-tag": (
        "Add a tag to note list",
        "Example: add-tag Weather sunny",
    ),
    "add-text": (
        "Add a text to note.",
        "Example: add-text Weather good day...",
    ),
    "delete-note": ("Delete a note.", "Example: delete Weather"),
    "edit-title": (
        "Change a title.",
        "Example: edit-title Weather Sun",
    ),
    "edit-text": (
        "Change a text",
        "Example: edit-text Weather one day...",
    ),
    "remove-tag": (
        "Remove a tag.",
        "Example: remove-tag Weather sunny",
    ),
    "notes": ("Show all notes.", "Example: notes"),
    "find-note": (
        "Shows all notes that contain the entered characters.",
        "Example: find sun",
    ),
    "find-note-by-filter": ("Shows notes that contain the entered characters by filter.",
                         "Example: find-note-filter sun sunny")
}

EXIT_COMMANDS = ("close", "exit", "quit", "bye")

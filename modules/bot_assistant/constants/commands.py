from modules.bot_assistant.handlers import contact_handlers, notes_handlers

CONTACT_COMMANDS = {
    "hello": contact_handlers.hello,
    "add": contact_handlers.add_contact,
    "edit": contact_handlers.edit_contact,
    "delete": contact_handlers.delete_contact,
    "add-phone": contact_handlers.add_phone,
    "edit-phone": contact_handlers.edit_phone,
    "show-phone": contact_handlers.get_contact_phone,
    "remove-phone": contact_handlers.remove_phone,
    "all": contact_handlers.get_all_contacts,
    "add-birthday": contact_handlers.add_birthday,
    "remove-birthday": contact_handlers.remove_birthday,
    "show-birthday": contact_handlers.show_birthday,
    "add-email": contact_handlers.add_email,
    "show-email": contact_handlers.show_email,
    "edit-email": contact_handlers.edit_email,
    "remove-email": contact_handlers.remove_email,
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
    "find-note-filter": notes_handlers.find_note_by_filter
}

CONTACT_COMMANDS_INFO = {
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
    "add-email": (
        "Add an email to a contact.",
        "Example: add-email alanwake@email.com",
    ),
    "show-email": ("Shows an email of a contact.", "Example: show-email AlanWake"),
    "edit-email": (
        "Edits an email of a contact.",
        "Example: edit-email alanwake@email.com alanwake1@email.com",
    ),
    "remove-email": (
        "Remove a contact's email.",
        "Example: remove-email AlanWake alanwake@email.com",
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
                         "Example: find-note-filter sun sunny"),
    "help": ("Show this help message.", "Example: help")
}

EXIT_COMMANDS = ("close", "exit", "quit", "bye")

COMMANDS = {**CONTACT_COMMANDS, **NOTES_COMMANDS}

COMMANDS_INFO = {**CONTACT_COMMANDS_INFO, **NOTES_COMMANDS_INFO}

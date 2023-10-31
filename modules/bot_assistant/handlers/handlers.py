import handlers.contact_handlers
import handlers.notes_handlers


def hello(address_book):
    return f"Hello! You have {len(address_book)} contacts in your address book. How can I help you?"
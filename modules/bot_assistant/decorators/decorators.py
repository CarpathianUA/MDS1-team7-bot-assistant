import modules.bot_assistant.models.exceptions as exceptions


def input_error(func):
    """
    Decorator for input errors.
    :param func:
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except exceptions.InvalidArgsError:
            return "Invalid number of arguments. Type 'help' to see available commands and their usage."
        except exceptions.ContactAlreadyExistsError:
            return "Contact already exists."
        except exceptions.ContactDoesNotExistError:
            return "Contact doesn't exist."
        except exceptions.PhoneDoesNotExistError:
            return "Phone doesn't exist."
        except exceptions.AddressDoesNotExistError:
            return "Address doesn't exist."
        except exceptions.InvalidPhoneError:
            return "Invalid phone number. Phone number must contain 10 digits, with or without '+' sign"
        except exceptions.InvalidBirthdayFormatError:
            return "Invalid birthday format. Please use DD.MM.YYYY format."
        except exceptions.InvalidBirthdayRangeError:
            return "The period for showing birthdays is limited to 365 days."
        except exceptions.InvalidSearchPatternError:
            return "Invalid symbols length. Please enter two or more symbols."

    return wrapper

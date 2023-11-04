import re


def validate_e164(phone):
    """
    Validate phone number in a basic E.164 format.
    :param phone:
    """
    pattern = re.compile(r"^\+?\d{10,12}$")
    return bool(pattern.match(phone))


def is_valid_phone(phone):
    if validate_e164(phone):
        return phone

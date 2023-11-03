import re


def validate_birth_date(birth_date):
    # DD.MM.YYYY
    pattern = re.compile(r"^\d{2}\.\d{2}\.\d{4}$")
    return bool(pattern.match(birth_date))


def is_valid_birth_date(birth_date):
    """
    Check if birth date is valid.
    :param birth_date:
    """
    if validate_birth_date(birth_date):
        return birth_date

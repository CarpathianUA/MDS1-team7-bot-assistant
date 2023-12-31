import re


def validate_email(email):
    pattern = re.compile(
        r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    )
    return bool(pattern.fullmatch(email))


def is_valid_email(email):
    if validate_email(email):
        return email

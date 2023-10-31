import re


def validate_email(email):
    """
    Validate email.
    :param email:
    """
    # john@email.com
    pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
    return bool(pattern.match(email))


def is_valid_email(email):
    """
    Check if email is valid.
    :param email:
    """
    if validate_email(email):
        return email

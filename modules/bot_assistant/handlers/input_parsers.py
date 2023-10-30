def parse_input(user_input):
    """
    Parse input from user.
    :param user_input:
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

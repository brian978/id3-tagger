import os


def prompt(text, default=""):
    user_input = raw_input(text)
    if 0 == len(user_input):
        user_input = default

    return user_input


def resolve_path(abs_path):
    if not isinstance(abs_path, str):
        return ""

    if abs_path[0] == "~":
        return os.path.join(os.path.expanduser("~/"), abs_path[2:])

    return abs_path

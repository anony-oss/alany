def remove_all_space(string: str):
    return string.replace(' ', '')


def is_string(str):
    if str[0] == '"' and str[-1] == '"':
        return True
    elif str[0] == "'" and str[-1] == "'":
        return True
    return False


def add_str(str):
    return '"' + str + '"'


def to_len(index, ln):
    if index >= ln:
        index -= ln
        index = to_len(index, ln)
    return index


def remove_start_spaces(str):
    try:
        if str[0] == ' ':
            str = str[1:]
            return remove_start_spaces(str)
        if str[-1] == ' ':
            str = str[:-1]
            return remove_start_spaces(str)
    except Exception:
        pass
    return str


def remove_space(string: str):
    if string and string[0] == ' ':
        string = string[1:]
        return remove_space(string)
    else:
        return string

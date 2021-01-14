from colorama import Fore


def apply_color(string, color1=Fore.WHITE, color2=Fore.WHITE, no_colors=False):
    if not no_colors:
        result = color1 + string + color2
    else:
        result = string
    return result


def complex_value(value):
    if isinstance(value, dict):
        value = "complex"
    return value


#def give_result(seq, no_color):
def give_result(seq):
    result = []
    for (path, status, value) in seq:
        if status == "nested":
            result.extend(value)

        if status == "deleted":
            string = f"'{path}' is '{status}'\n"
            #result.append(apply_color(string, Fore.RED, no_colors=no_color))
            result.append(string)

        elif status == "added":
            value = complex_value(value)
            string = f"'{path}' is '{status}' with value '{value}'\n"
            #result.append(apply_color(string, Fore.GREEN, no_colors=no_color))
            result.append(string)

        elif status == "changed":
            original_value = value[0]
            changed_value = value[1]
            original_value = complex_value(original_value)
            changed_value = complex_value(changed_value)
            string = f"'{path}' is '{status}' from '{original_value}'"\
                "to '{changed_value}'\n"
            #result.append(apply_color(string, Fore.YELLOW, no_colors=no_color))
            result.append(string)
    return result


def plain(diff, no_color=False):
    def inner(dict_, root=None):
        strings = []
        for key, (status, value) in dict_.items():
            path = f"{root}.{key}" if root else key
            if status == "nested":
                strings.append([path, status, inner(value, path)])
            else:
                strings.append((path, status, value))
        strings = list(map(list, strings))
        strings.sort()
        #res = (give_result(strings, no_color))
        res = (give_result(strings))
        return "".join(res)
    return inner(diff)

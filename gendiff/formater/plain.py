from colorama import Fore


simple_types = (float, str, int, bool)
complex_value = "[complex value]"
json_encode_values_list = [
    "false",
    "true",
    "null",
]

property_string = "Property '{}' was "
updated_string = property_string + "updated. From {} to {}"
added_string = property_string + "added with value: {}"
removed_string = property_string + "removed"


def apply_color(string, color1=Fore.WHITE, color2=Fore.WHITE, no_colors=False):
    if not no_colors:
        result = color1 + string + color2
    else:
        result = string
    return result


def path_maker(path, key):
    if path == "":
        return key
    return path + "." + key


def get_value(value):
    if type(value) in simple_types:
        if value == 0 or value in json_encode_values_list:
            return f"{value}"
        return f"'{value}'"
    return complex_value


def plain(diffs):
    result = []

    def walk(diff, path):
        for key, value in sorted(diff.items()):
            if isinstance(value, dict):
                before_value = value.get("removed")
                after_value == value.get("added")
                if "stable" in value:
                    continue
                elif after_value is not None and befor_value is not None:
                    before_value = get_value(before_value)
                    after_value = get_value(after_value)
                    result.append(
                        updated_string.format(
                            path_maker(path, key),
                            before_value,
                            after_value
                        )
                    )
                elif before_value and "added" not in value:
                    result.append(
                        removed_string.format(
                            path_maker(
                                path,key
                                )
                            )
                        )
                elif after_value and "removed" not in value:
                    after_value = get_value(after_value)
                    result.append(
                        added_string.format(
                            path_maker(
                                path,
                                key
                                ),
                            after_value
                            )
                        )
                else:
                    walk(value, path_maker(path, key))
    
    walk(diffs, "")
    return "\n".join(lines)




#def complex_value(value):
#    if isinstance(value, dict):
#        value = "complex"
#    return value

#def give_result(seq):
#    result = []
#    for (path, status, value) in seq:
#        if status == "nested":
#            result.extend(value)
#
#        if status == "deleted":
#            string = f"'{path}' is '{status}'\n"
#            result.append(string)
#
#        elif status == "added":
#            value = complex_value(value)
#            string = f"'{path}' is '{status}' with value '{value}'\n"
#            result.append(string)
#
#        elif status == "changed":
#            original_value = value[0]
#            changed_value = value[1]
#            original_value = complex_value(original_value)
#            changed_value = complex_value(changed_value)
#            string = f"'{path}' is '{status}' from '{original_value}'"\
#                "to '{changed_value}'\n"
#            result.append(string)
#    return result


#def plain(diff, no_color=False):
#    def inner(dict_, root=None):
#        strings = []
#        for key, (status, value) in dict_.items():
#            path = f"{root}.{key}" if root else key
#            if status == "nested":
#                strings.append([path, status, inner(value, path)])
#            else:
#                strings.append((path, status, value))
#        strings = list(map(list, strings))
#        strings.sort()
#        res = (give_result(strings))
#        return "".join(res)
#    return inner(diff)

def stylish(diffs):
    lines = ["{"]

    def walk(diff, tabs):
        for key, value in diff.items():
            if key[0] not in ("+","-"," "):
                key = " " + key
            if isinstance(value, dict):
                lines.append(f"{tabs}{key}: {{")
                walk(value, tabs + "    ")
            else:
                #TRAP HERE
                #if value == "" or value == '':
                if value == "":
                    lines.append(f"{tabs}{key} ")
                else:
                    lines.append(f"{tabs}{key}: {value}")
        lines.append(f"{tabs[:-2]}}}")

    walk(coverter(diffs), "  ")
    return "\n".join(lines)


def converter(tree):
    result = {}
    for key, value in sorted(tree.items()):
        if isinstance(value, dict):
            if value.get("stable"):
                new_key = "" + "" + key
                result[new_key] = value.get("same")
            if value.get("removed") or value.get("removed") == "" or value.get("removed") == 0 or value.get("removed") == "null":
                new_key = "-" + " " + key
                result[new_key] = value.get("removed")
            if value.get("added") or value.get("added") == "" or value.get("added") == 0 or value.get("added") == "null":
                new_key = "+" + "" + key
                result[new_key] = value.get("added")
            if value.get("added") is None and value.get("removed") is None and value.get("stable"):
                result[key] = converter(value)
        else:
            result[key] = value
    return result

#def converter(list_, tabs):
#    string_spaces = " " * tabs
#    result = ["{\n"]
#    for (key, status, value) in list_:
#        if status == "nested":
#            string = f" {string_spaces} {key}: {value}\n"
#            result.append(string)
#            if result[-1][-1] == "\n" and result[-1][-2] == "\n":
#                result[-1] = result[-1][:-1]
#
#        elif status == "deleted":
#            string = f"{string_spaces}- {key}: {value}\n"
#            result.append(string)
#            if result[-1][-1] == "\n" and result[-1][-2] == "\n":
#                result[-1] = result[-1][:-1]
#
#        elif status == "added":
#            string = f"{string_spaces}+ {key}: {value}\n"
#            result.append(string)
#            if result[-1][-1] == "\n" and result[-1][-2] == "\n":
#                result[-1] = result[-1][:-1]
#
#        elif status == "changed":
#            string_before = f"{string_spaces}- {key}: {value[0]}\n"
#            string_after = f"{string_spaces}+ {key}: {value[1]}\n"
#            result.append(string_before)
#            if result[-1][-1] == "\n" and result[-1][-2] == "\n":
#                result[-1] = result[-1][:-1]
#
#            result.append(string_after)
#            if result[-1][-1] == "\n" and result[-1][-2] == "\n":
#                result[-1] = result[-1][:-1]
#
#        else:
#            result.append(f"{string_spaces}  {key}: {value}\n")
#            if result[-1][-1] == "\n" and result[-1][-2] == "\n":
#                result[-1] = result[-1][:-1]
#
#    result.append(' ' * (tabs - 2) + '}')
#    result.append('\n')
#    return result
#
#
#def stylish(diff, tabs=2):
#    strings = []
#    for key, (status, value) in diff.items():
#        if isinstance(value, dict):
#            strings.append((key, status, stylish(value, tabs=tabs + 4)))
#        else:
#            strings.append((key, status, value))
#    strings.sort()
#    res = (converter(strings, tabs))
#    return "".join(res)

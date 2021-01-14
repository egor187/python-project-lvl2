def converter(list_, tabs):
    string_spaces = " " * tabs
    result = ["{\n"]
    for (key, status, value) in list_:
        if status == "nested":
            #if result[-1][-1] == "\n" and result[-1][-2] == "\n":
            #    string = f" {string_spaces} {key}: {value}"
            #else:
            #    string = f" {string_spaces} {key}: {value}\n"
            
            string = f" {string_spaces} {key}: {value}\n"
            #if result[-1][-1] == "\n" or result[-1][-1] == False:
            #    result.append(string[:-1])
            #else:
            #    result.append(string)
            
            result.append(string)
 
            if result[-1][-1] == "\n" and result[-1][-2] == "\n":
                result[-1] = result[-1][:-1]

        
        elif status == "deleted":
            
            #if result[-1][-1] == "\n":
            #    string = f" {string_spaces} {key}: {value}"
            #else:
            #    string = f" {string_spaces} {key}: {value}\n"
            
            string = f"{string_spaces}- {key}: {value}\n"
            
            result.append(string)

            if result[-1][-1] == "\n" and result[-1][-2] == "\n":
                result[-1] = result[-1][:-1]

        elif status == "added":

            #if result[-1][-1] == "\n":
            #    string = f" {string_spaces} {key}: {value}"
            #else:
            #    string = f" {string_spaces} {key}: {value}\n"

            string = f"{string_spaces}+ {key}: {value}\n"

            result.append(string)
            
            if result[-1][-1] == "\n" and result[-1][-2] == "\n":
                result[-1] = result[-1][:-1]

        elif status == "changed":
            string_before = f"{string_spaces}- {key}: {value[0]}\n"
            string_after = f"{string_spaces}+ {key}: {value[1]}\n"
            result.append(string_before)
            
            if result[-1][-1] == "\n" and result[-1][-2] == "\n":
                result[-1] = result[-1][:-1]

            result.append(string_after)
            
            if result[-1][-1] == "\n" and result[-1][-2] == "\n":
                result[-1] = result[-1][:-1]

        else:
            result.append(f"{string_spaces}  {key}: {value}\n")
            
            if result[-1][-1] == "\n" and result[-1][-2] == "\n":
                result[-1] = result[-1][:-1]


    result.append(' ' * (tabs - 2) + '}')
    result.append('\n')
    return result


def stylish(diff, tabs=2):
    strings = []
    for key, (status, value) in diff.items():
        if isinstance(value, dict):
            strings.append((key, status, stylish(value, tabs=tabs + 4)))
        else:
            strings.append((key, status, value))
    strings.sort()
    res = (converter(strings, tabs))
    return "".join(res)

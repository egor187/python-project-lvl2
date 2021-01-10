import yaml


def yaml_diff(filepath_1, filepath_2):
    """
    YAML - language like dict syntax. By safe_load .yml module convert to a
    Python dict-type obj.
    """
    first_file = yaml.safe_load(open(filepath_1))
    second_file = yaml.safe_load(open(filepath_2))
    result = ''
    for key in sorted(first_file.keys()):
        if key not in sorted(second_file.keys()):
            result += '-' + key + ':' + str(first_file[key]) + '\n'
        else:
            if first_file[key] != second_file[key]:
                result += '-' + key + ':' + str(first_file[key]) + \
                        '\n' + '+' + key + ':' + str(second_file[key]) + '\n'
            else:
                result += key + ':' + str(first_file[key]) + '\n'
    for key in sorted(second_file.keys()):
        if key not in sorted(first_file.keys()):
            result += '+' + key + ':' + str(second_file[key]) + '\n'
    return result

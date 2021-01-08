import json


def generate_diff(filepath_1, filepath_2):
    first_file, second_file = json.load(open(filepath_1)), \
            json.load(open(filepath_2))
    result = ''
    for key in first_file.keys():
        if key not in second_file.keys():
            result += '-' + key + ':' + str(first_file[key]) + '\n'
        else:
            if first_file[key] != second_file[key]:
                result += '-' + key + ':' + str(first_file[key]) + \
                        '\n' + '+' + key + ':' + str(second_file[key]) + '\n'
            else:
                result += key + ':' + str(first_file[key]) + '\n'
    for key in second_file.keys():
        if key not in first_file.keys():
            result += '+' + key + ':' + str(second_file[key]) + '\n'
    return result

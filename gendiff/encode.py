import json


json_encoding_list = [
        None,
        False,
        True,
        float,
        int,
        str,
        dict,
        list,
    ]


def encode(value):
    if value == 0 and type(value) == int:
        return 0
    if value == 1 and type(value) == int:
        return 1
    if value in json_encoding_list:
        return json.dumps(value)
    return value

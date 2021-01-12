import json


def json_formatter(dict_):
    return json.dumps(dict_, indent=2, sort_keys=True)

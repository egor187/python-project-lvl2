import json


#def json_formatter(dict_):
#    res = json.dumps(dict_, indent=2, sort_keys=True)
#    return res + "\n"

def json_formatter(dict_):
    return json.dumps(dict_)

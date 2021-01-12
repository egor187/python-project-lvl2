import os.path
import json
import yaml

yaml_formats = [".yml", ".yaml"]


def check_type(path):
    path = os.path.abspath(path)
    file_format = os.path.splitext(path)
    file_format = file_format[1].lower()
    result = ""
    if file_format == ".json":
        result = json.load(open(path))
    elif file_format in yaml_formats:
        result = yaml.safe_load(open(path))
    return result

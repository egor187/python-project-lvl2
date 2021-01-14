from gendiff.check_type import check_type
from gendiff.formater.plain import plain
from gendiff.formater.stylish import stylish
from gendiff.formater.json import json_formatter
from gendiff.core_diff import core_diff_plug


def generate_diff(source1, source2, formatter="stylish"):
    formatter_dict = {
        "plain": plain,
        "json": json_formatter,
        "stylish": stylish,
    }
    source1 = check_type(source1)
    source2 = check_type(source2)
    if formatter:
        if formatter == 'raw':
            return core_diff_plug(source1, source2)
        else:
            formatter = formatter_dict[formatter]
            return formatter(core_diff_plug(source1, source2))
    else:
        return core_diff_plug(source1, source2)

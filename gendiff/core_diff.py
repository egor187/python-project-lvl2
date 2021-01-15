from gendiff.encode import encode


def get_value(node, key):
    if key in node:
        return encode(node.get(key))
    return None


def mark(before, after):
    before_encoded = encode(before)
    after_encoded = encode(after)
    if before_encoded == after_encoded:
        return {"stable": before_encoded}
    elif before is None and type(before) != str:
        return {"added": after_encoded}
    elif after is None and type(after) != str:
        return {"removed": before_encoded}
    elif before_encoded != after_encoded:
        if isinstance(after, dict) and isinstance(before, dict):
            return core_diff_plug(before, after)
        return {"removed": before_encoded, "added": after_encoded}


def core_diff_plug(filepath_1, filepath_2):
    return dict(
            map(
                lambda x: (
                    x, mark(
                        get_value(filepath_1, x), get_value(filepath_2, x),
                    ),
                ), (filepath_1.keys() | filepath_2.keys()),
            ),
        )

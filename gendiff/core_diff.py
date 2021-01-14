from gendiff.encode import encode


def get_value(node, key):
    if key in node:
        return encode(node, key)
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





#def core_diff_plug(filepath_1, filepath_2):
#    result = {}
#    for key in filepath_1.keys():
#        if filepath_1[key] == False:
#            filepath_1[key] = "false"
#        if filepath_1[key] == True:
#            filepath_1[key] = "true"
#        if filepath_1[key] == None:
#            filepath_1[key] = "null"
#    for key in filepath_2.keys():
#        if filepath_2[key] == False:
#            filepath_2[key] = "false"
#        if filepath_2[key] == True:
#            filepath_2[key] = "true"
#        if filepath_2[key] == None:
#            filepath_2[key] = "null"
#    for key in filepath_1.keys() & filepath_2.keys():
#        if filepath_1[key] == filepath_2[key]:
#            if isinstance(filepath_1[key], dict):
#                result[key] = (
#                    'stable',
#                    core_diff_plug(
#                        filepath_1[key],
#                        filepath_1[key]
#                    )
#                )
#            else:
#                result[key] = ('stable', filepath_1[key])
#        else:
#            if isinstance(filepath_1[key], dict) \
#                    and isinstance(
#                        filepath_2[key], dict
#            ):
#                result[key] = (
#                    'nested',
#                    core_diff_plug(
#                        filepath_1[key],
#                        filepath_2[key]
#                    )
#                )
#            else:
#                result[key] = ('changed', (filepath_1[key], filepath_2[key]))
#
#    for key in filepath_1.keys() - filepath_2.keys():
#        if isinstance(filepath_1[key], dict):
#            result[key] = (
#                'deleted',
#                core_diff_plug(
#                    filepath_1[key],
#                    filepath_1[key]
#                )
#            )
#        else:
#            result[key] = ('deleted', filepath_1[key])
#
#    for key in filepath_2.keys() - filepath_1.keys():
#        if isinstance(filepath_2[key], dict):
#            result[key] = (
#                'added',
#                core_diff_plug(
#                    filepath_2[key],
#                    filepath_2[key]
#                )
#            )
#        else:
#            result[key] = ('added', filepath_2[key])
#    return result

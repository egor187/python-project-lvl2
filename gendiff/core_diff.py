def null_converter(dict_):
    for key in dict_.keys():
        if not dict_[key]:
            dict_[key] = "false"
        if dict_[key] == True:
            dict_[key] = "true"
        if dict_[key] == None:
            dict_[key] = "null"
    return dict_



def core_diff_plug(filepath_1, filepath_2):
    result = {}
    for key in filepath_1.keys():
        if filepath_1[key] == False:
            filepath_1[key] = "false"
        if filepath_1[key] == True:
            filepath_1[key] = "true"
        if filepath_1[key] == None:
            filepath_1[key] = "null"
        #print(filepath_1[key], type(filepath_1[key]))
    for key in filepath_2.keys():
        if filepath_2[key] == False:
            filepath_2[key] = "false"
        if filepath_2[key] == True:
            filepath_2[key] = "true"
        if filepath_2[key] == None:
            filepath_2[key] = "null"
        #print(filepath_2[key], type(filepath_2[key]))

    for key in filepath_1.keys() & filepath_2.keys():
        if filepath_1[key] == filepath_2[key]:
            if isinstance(filepath_1[key], dict):
                result[key] = (
                                'stable',
                                core_diff_plug(
                                    filepath_1[key],
                                    filepath_1[key])
                                )
            else:
                result[key] = ('stable', filepath_1[key])
        else:
            if isinstance(filepath_1[key], dict) \
                    and isinstance(
                            filepath_2[key], dict):
                result[key] = (
                                'nested',
                                core_diff_plug(
                                    filepath_1[key],
                                    filepath_2[key]
                                    )
                                )
            else:
                result[key] = ('changed', (filepath_1[key], filepath_2[key]))

    for key in filepath_1.keys() - filepath_2.keys():
        if isinstance(filepath_1[key], dict):
            result[key] = (
                    'deleted',
                    core_diff_plug(
                        filepath_1[key],
                        filepath_1[key]
                        )
                    )
        else:
            result[key] = ('deleted', filepath_1[key])

    for key in filepath_2.keys() - filepath_1.keys():
        if isinstance(filepath_2[key], dict):
            result[key] = (
                            'added',
                            core_diff_plug(
                                filepath_2[key],
                                filepath_2[key]
                                )
                    )
        else:
            result[key] = ('added', filepath_2[key])
    return result

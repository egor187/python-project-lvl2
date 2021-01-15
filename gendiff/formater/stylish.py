def stylish(diffs):
    lines = ["{"]

    def walk(diff, tabs):
        for key, value in diff.items():
            if key[0] not in ("+", "-", " "):
                key = "  " + key
            if isinstance(value, dict):
                lines.append(f"{tabs}{key}: {{")
                walk(value, tabs + "    ")
            else:
                if value == "":
                    lines.append(f"{tabs}{key}: ")
                else:
                    lines.append(f"{tabs}{key}: {value}")
        lines.append(f"{tabs[:-2]}}}")

    walk(converter(diffs), "  ")
    return "\n".join(lines)


def converter(tree):
    result = {}
    for key, value in sorted(tree.items()):
        if isinstance(value, dict):
            if value.get("stable"):
                new_key = "" + "" + key
                result[new_key] = value.get("stable")
            if value.get("removed") \
                    or value.get("removed") == "" \
                    or value.get("removed") == 0 \
                    or value.get("removed") == "null":
                new_key = "-" + " " + key
                result[new_key] = value.get("removed")
            if value.get("added") \
                    or value.get("added") == "" \
                    or value.get("added") == 0 \
                    or value.get("added") == "null":
                new_key = "+" + " " + key
                result[new_key] = value.get("added")
            if value.get("added") is None \
                    and value.get("removed") is None \
                    and value.get("stable") is None:
                result[key] = converter(value)
        else:
            result[key] = value
    return result

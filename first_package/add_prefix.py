def add_prefix_1(names: list, pref: str) -> list:
    counter = 0
    new_names: list = []
    while counter < len(names):
        name = f"{pref} {names[counter]}"
        new_names.append(name)
        counter += 1
    return new_names


def add_prefix_2(coll, prefix):
    result = []
    for word in coll:
        result.append(f"{prefix} {word}")
    return result

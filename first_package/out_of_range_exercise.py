def get(cities: list, index: int, default: str = None):
    if (index < 0) and (len(cities) > abs(index + 1)):
        return cities[index]
    elif index >= 0 and len(cities) > index:
        return cities[index]
    else:
        return default

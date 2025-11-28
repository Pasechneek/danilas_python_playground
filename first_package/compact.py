class Compact:
    def compact(coll: list[int|None]):
    # Инициализация результата
    # Для пустой входной коллекции результатом будет пустой список
        result = []

        for item in coll:
            if item is not None:
                result.append(item)

        return result
class ChangeList:
    def fill_with_first_1(items: list) -> None:
        if len(items) > 0:
            first_item = items[0]
            for item in range(0, len(items)):
                print(f"\nitems[{item}] = {first_item}\n")
                items[item] = first_item

    def fill_with_first_2(coll):
        length = len(coll)

        if length == 0:
            return

        first = coll[0]

        for i in range(0, length):
            coll[i] = first

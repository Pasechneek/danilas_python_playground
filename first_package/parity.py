def is_even(number: int) -> True | False:
    """Check if number is even"""""
    return number % 2

def get_same_parity(numbers: list | None) -> list:
    """Get all even numbers from the given collection"""""
    result = []

    if not numbers:
        return []

    first: int = numbers[0]
    length = len(numbers)

    first_number_parity = is_even(first)
    counter = 0

    if length > 1:
        while counter < length:
            current = numbers[counter]
            current_parity = is_even(current)
            check = first_number_parity == current_parity
            if check:
                result.append(current)
            counter += 1
    return result

def get_same_parity_2(coll):
    """Get all even numbers from the given collection"""
    if not coll:
        return []
    result = []
    remainder = coll[0] % 2

    for item in coll:
        if item % 2 == remainder:
            result.append(item)
    return result

def maximize_a_using_b(a_number: str, b_number: str) -> str:
    digits_a = list(a_number)
    digits_b = sorted(b_number, reverse=True)
    index = 0
    for i in range(len(digits_a)):
        if index < len(digits_b) and digits_a[i] < digits_b[index]:
            digits_a[i] = digits_b[index]
            index += 1
    return "".join(digits_a)

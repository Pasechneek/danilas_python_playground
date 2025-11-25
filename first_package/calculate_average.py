def calculate_average(temperatures: list) -> float:
    if len(temperatures) == 0:
        return None
    else:
        agreg_sum: float = 0
        counter: int = 0
        for n in temperatures:
            agreg_sum += n
            counter += 1
    return agreg_sum / counter

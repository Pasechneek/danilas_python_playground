def air_humidifier(input_str):
    lines = input_str.strip().split("\n")
    counter = int(lines[0])
    water = 0
    prev_time = 0
    for i in range(1, counter + 1):
        time, values = map(int, lines[i].split())
        delta_t = time - prev_time
        water = max(0, water - delta_t)
        water += values
        prev_time = time
    return str(water)

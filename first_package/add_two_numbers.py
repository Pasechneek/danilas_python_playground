import sys


def add(a, b):
    return a + b


if __name__ == "__main__":
    print("has arguments")

    # Формируем список из аргументов командной строки
    input_list = sys.argv[1:]
    print("Входные данные:", input_list)
    print("Тип входных данных:", type(input_list))

    # Вызываем функцию и выводим результат
    result = add(1, 2)
    print("Результат:", result)

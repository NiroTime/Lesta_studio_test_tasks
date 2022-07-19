def is_even(value: int) -> bool:
    """
    Функция определения чётности числа при помощи последнего бита в двоичной
    системе счисления.
    """
    return value & 1 == 0


if __name__ == '__main__':
    print(is_even(int(input())))

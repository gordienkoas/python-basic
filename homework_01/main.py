"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in numbers]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


#def is_prime(n):
#    d = 2
#    while d * d <= n and n % d != 0:
#        d += 1
#    return d * d > n

def is_prime(n):
    k = 0
    for i in range(2, n // 2 + 1):
        if (n % i == 0):
            k = k + 1
    if (k <= 0 and n > 1):
        return True
    else:
        return False
def filter_numbers(numbers_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if filter_type == ODD:
        return [number for number in numbers_list if number % 2 != 0]
    elif filter_type == EVEN:
        return [number for number in numbers_list if number % 2 == 0]
    elif filter_type == PRIME:
        return [number for number in numbers_list if is_prime(number) == True]
    else:
        return "ValueError"
import numpy as np
from game_v2 import score_game


def game_core_v3(number: int = 1) -> int:
    """
    Функция получает на вход загаданное число, диапазон поиска числа от 1 до 100.
    Требуется каждый раз брать число, которое делит пополам диапазон поиска, 
    если загадано не это число, то, в зависимости от того больше это число 
    или меньше, сужать диапазон поиска. В конце, если между числами остался 
    лишь один вариант, попытка не считается, так как ответ становится очевидным.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0                                   # Число поыток
    predict = 0                                 # Угаданное число

    """Поскольку число в пределах от 1 до 100, требуется расширить границы 
    на 1 с каждой стороны, так как крайние числа не проверяются """

    border_min = 1 - 1                          # Граница минимума
    border_max = 100 + 1                        # Граница максимума
    centre = (border_max + border_min) // 2     # Центр диапазона поиска

    while number != predict:
        if number != centre:
            count += 1

            if number < centre:
                border_max = centre
            elif number > centre:
                border_min = centre

            centre = (border_max + border_min) // 2

        elif number == centre:
            if border_max - border_min != 2:
                count += 1
            predict = centre

    return count


print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)

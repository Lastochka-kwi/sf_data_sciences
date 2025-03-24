"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def game_core_v3(number: int=1) -> int:
    """Сначала устанавливаем любое random число, заводим две переменные, мин и макс, обновляем их
        в зависимости от того, больше оно или меньше нужного.
        После обновлнеия минимума и максимума загадываем новое число из урезанного списка вариантов
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min_num = 1 # Минимально значение поиска
    max_num = 101 # Максимальное значение поиска
    predict = np.random.randint(min_num, max_num)

    while number != predict:
        count += 1        
        if number > predict:
            min_num = predict # Корректируем минимальное значение
            predict = np.random.randint(min_num, max_num) # Обновляем ответ по новым вводным
        elif number < predict:
            max_num = predict
            predict = np.random.randint(min_num, max_num)

    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

if __name__ == "__main__":
    score_game(game_core_v3)
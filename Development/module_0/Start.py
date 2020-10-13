import numpy as np


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


def game_core_v2(number):
    """Сначала определим постоянное значение для переменной predict и будем его сравнивать с загаданным числом,
        при этом изменяя верхнюю или нижнюю границу интервала, в котором находится number"""
    count = 0
    down_light = 1
    up_line = 100
    predict = (down_light + up_line) // 2
    while number != predict:
        count += 1
        predict = (low + high) // 2  # Новое значение переменной после каждой итерации
        if number > predict:
            low = predict + 1
        elif number < predict:
            high = predict - 1
    return count  # Выход из цикла, если угадали


score_game(game_core_v2)

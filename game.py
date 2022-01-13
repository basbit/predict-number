"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number:int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min_number = 1
    max_number = 100
    
    predict_number = max_number / 2
    
    while number != predict_number:
        count += 1
        if predict_number < number:
            min_number = predict_number + 1
        elif predict_number > number:
            max_number = predict_number - 1
        
        predict_number = round((min_number + max_number) / 2)
    
    print (f"Число угадано! Это число = {number}, за {count} попыток")
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для вопроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


if __name__ == "__main__":
     # RUN
    score_game(random_predict)

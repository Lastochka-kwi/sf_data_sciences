import numpy as np

number = np.random.randint(1, 101)
count = 0

while True:
    count += 1
    predicet_number = int(input('Угадай число от 1 до 100: '))
    if predicet_number < number:
        print('Число должно быть больше')
    elif predicet_number > number:
        print('Число должно быть меньше')
    else:
        print(f'Вы угадали, это число: {number}, количество попыток: {count}')
        break
# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

from random import randint

# функция проверки ввода
def f_input(number, res):
    while True:
        if number == 'А1' or number == 'А2' or number == 'А3' or number == 'С1' or number == 'С2' or number == 'С3' or number == 'Б1' or number == 'Б2' or number == 'Б3' or number == 'И1' or number == 'И2' or number == 'И3' or number == 'В1' or number == 'В2' or number == 'В3':
            number = input('Переключите на английскую раскладку:  ').upper()
        elif number in res:
            number = input(
                'Такое значение уже было. Введите новое значение поля:  '). upper()
        elif number == 'A1' or number == 'A2' or number == 'A3' or number == 'B1' or number == 'B2' or number == 'B3' or number == 'C1' or number == 'C2' or number == 'C3':
            break
        else:
            number = input('Вы должны ввести значение поля ').upper()
    return number

# функция проверки ввода бота
def f_input_bot(number, res):
    while True:
        if number in res:
            time_number = randint(1, 9)
            number = dict_bot.setdefault(time_number)
            print(f'11{number}')
        else:
            break
    return number

# функция вывода поля на экран
def print_games(dict_games):
    print()
    print('     1     2     3')
    print()
    print('A   ', my_dict['A1'], ' | ', my_dict['A2'], ' | ', my_dict['A3'])
    print('    ----------------')
    print('B   ', my_dict['B1'], ' | ', my_dict['B2'], ' | ', my_dict['B3'])
    print('    ----------------')
    print('C   ', my_dict['C1'], ' | ', my_dict['C2'], ' | ', my_dict['C3'])
    print()

my_dict = {'A1': '*', 'A2': '*', 'A3': '*',
           'B1': '*', 'B2': '*', 'B3': '*',
           'C1': '*', 'C2': '*', 'C3': '*'}

dict_bot = {1: 'A1', 2: 'A2', 3: 'A3',
            4: 'B1', 5: 'B2', 6: 'B3',
            7: 'C1', 8: 'C2', 9: 'C3'}

# имена игроков
print('Сыграем в игру крестики-нолики?')
player1 = input('Как тебя зовут? ')
player1 = player1[0].upper()+player1[1:]
print('А меня зовут Ирэн. Приятно познакомиться\nТвои - крестики Х, мои-нолики 0')
player2 = 'Ирэн'

print_games(my_dict)

# список для проверки повторяющихся значений
res = []

# определяем кто ходит первый
first = randint(1, 2)
if first == 1:
    number = (input(f'Первым ходишь ты, {player1}. Введи значение поля '))
    number = f_input(number.upper(), res)
    res.append(number.upper())
    my_dict[number] = 'X'

else:
    time_number = randint(1, 9)
    number = dict_bot.setdefault(time_number)
    print(f'Первым хожу я. Значение поля будет равным {number} ')
    res.append(number)
    my_dict[number] = '0'

print_games(my_dict)

for i in range(8):
    first += 1
    if first % 2 == 0:
        player = player2
        time_number = randint(1, 9)
        number = dict_bot.setdefault(time_number)
        number = f_input_bot(number, res)
        print(f'Мой ход: {number} ')
        res.append(number)
        my_dict[number] = '0'
        print_games(my_dict)
    else:
        player = player1
        number = (input(f'{player1}, Ваш ход: '))
        number = f_input(number.upper(), res)
        res.append(number.upper())
        my_dict[number] = 'X'
        print_games(my_dict)
    if (my_dict['A1'] == 'X' and my_dict['A2'] == 'X' and my_dict['A3'] == 'X') or (my_dict['A1'] == '0' and my_dict['A2'] == '0' and my_dict['A3'] == '0') or\
        (my_dict['B1'] == 'X' and my_dict['B2'] == 'X' and my_dict['B3'] == 'X') or (my_dict['B1'] == '0' and my_dict['B2'] == '0' and my_dict['B3'] == '0') or\
        (my_dict['C1'] == 'X' and my_dict['C2'] == 'X' and my_dict['C3'] == 'X') or (my_dict['C1'] == '0' and my_dict['C2'] == '0' and my_dict['C3'] == '0') or\
        (my_dict['A1'] == 'X' and my_dict['B1'] == 'X' and my_dict['C1'] == 'X') or (my_dict['A1'] == '0' and my_dict['B1'] == '0' and my_dict['C1'] == '0') or\
        (my_dict['A2'] == 'X' and my_dict['B2'] == 'X' and my_dict['C2'] == 'X') or (my_dict['A2'] == '0' and my_dict['B2'] == '0' and my_dict['C2'] == '0') or\
        (my_dict['A3'] == 'X' and my_dict['B3'] == 'X' and my_dict['C3'] == 'X') or (my_dict['A3'] == '0' and my_dict['B3'] == '0' and my_dict['C3'] == '0') or\
        (my_dict['A1'] == 'X' and my_dict['B2'] == 'X' and my_dict['C3'] == 'X') or (my_dict['A1'] == '0' and my_dict['B2'] == '0' and my_dict['C3'] == '0') or\
            (my_dict['C1'] == 'X' and my_dict['B2'] == 'X' and my_dict['A3'] == 'X') or (my_dict['C1'] == '0' and my_dict['B2'] == '0' and my_dict['A3'] == '0'):
        if player == player1:
            print(f'Твоя победа, {player}! Поздравляю!')
            break
        else:
            print('Игру выиграл я! Ура!!!')
            break
    else:
        if i == 7:
            print('Поле заполнено. Стоп игра. Победителей нет.')
        else:
            continue
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import randint

# функция правил русского языка


def number_sweet(my_list, n):
    if n == 0:
        my_list = 'Игры не будет, на столе конфет нет'
    elif n == 1 or 0 < ((n/10)-(int(n/10))) < 0.2:
        my_list.append(f' {n} конфета. ')
    elif 2 < n < 5 or 0.1 < ((n/10)-(int(n/10))) < 0.5 and n > 20:
        my_list.append(f'{n} конфеты. ')
    else:
        my_list.append(f'{n} конфет. ')
    print(*my_list, end='')

# функция проверки 28 конфет
def f_28(number, n):
    while True:
        if not number.isdigit():
            number = input('Вы должны ввести число. Сколько конфет возьмете?')
        else:
            number = int(number)
            if number > n:
                number = (input(
                    f'Вы не можете взять конфет больше, чем их лежит на столе.Сколько конфет возьмете?'))
            elif number > 28:
                number = (
                    input(f'Вы не можете взять больше 28 конфет.Сколько конфет возьмете? '))
            else:
                break
    return number
    

#имена игроков
print('Сыграем в игру:\nНа столе лежит заданное количество конфет. Каждый игрок ходит по очереди.\nЗа один ход можно забрать не более чем 28 конфет. Того, кто ходит первым, определит случай.\nТот, кто забирает со стола последнюю конфету, выигрывает партию и забирает себе все конфеты.\nИтак,')
player1 = input('Представьтесь, пожалуйста: ')
player1=player1[0].upper()+player1[1:]
print()

#определяем количество конфет
n=randint(50,100)

my_sweet=['На столе лежит']
number_sweet(my_sweet,n)
print()

#определяем кто ходит первый
first=randint(1,2)
if first==1:
    number= (input(f'Первым ходите Вы, {player1}.Сколько конфет возьмете?  '))
    number=f_28(number,n)
else:
    number=randint(1,28)
    print(f'Первым хожу я. Я беру {number} конфет')

while n>0:
    n=n-number
    my_sweet2=['На столе осталось']
    my_sweet1=['Я беру']
    if n<28:
        number_sweet(my_sweet2,n)
        print()
        if first%2!=0:                    
            print ('Я забираю их всех, и на столе остается ноль конфет. \nУра! Победил я!')
        else:
            print(f'{player1}, Вы забираете их всех, и на столе остается ноль конфет. \nПоздравляю, Вы победили!')
        break
    else:
         first+=1        
         if first%2==0:
            number_sweet(my_sweet2,n)
            number= randint(1,28)
            number_sweet(my_sweet1,number)
            print()
  #          print(f'Я беру {number} конфет. ')
         else:
            number_sweet(my_sweet2,n)
            number= (input(f'{player1}, Ваш ход: '))
            number=f_28(number,n)
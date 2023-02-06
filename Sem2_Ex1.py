# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
'''
#первоначальный код
s = input ('Введите число: ')
sum=0
for i in range(len(s)):
    if s[i]=='.':
        continue
    else:
        sum=sum+int(s[i])
print(f'Сумма цифр числа {s} равна', sum)
'''

# проверка ввода данных
def f_input(number):
    while True:
        try:
            float(number)
            break
        except ValueError:
            number = input('Введите ЧИСЛОВОЕ значение:')
    return number


s = s_first = f_input(input('Введите число: '))
s = s.replace('-', '').replace('0.', '')

sum = 0
for i in range(len(s)):
    sum = sum+int(s[i])
print(f'Сумма цифр числа {s_first} равна', sum)
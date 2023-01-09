# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

number = int(input('Введите число для составления ряда Фибоначчи: '))

print('1 способ')
# конечное число Фибоначчи
fib_number = 0
number1 = 0
number2 = 1
for i in range(number):
    fib_number = number1+number2
    number2 = number1
    number1 = fib_number

# заполняем отрицательными числами негафибоначчи
new_fib_list = [fib_number, number2]
for i in range(number-1):
    fib_number = (number1-number2)
    number1 = number2
    number2 = fib_number
    new_fib_list.append(fib_number)
    if number % 2 == 0:
        if i % 2 == 0:
            new_fib_list[i] = -new_fib_list[i]
        else:
            continue
    else:
        if i % 2 != 0:
            new_fib_list[i] = -new_fib_list[i]
        else:
            continue
print(fib_number)

# добавляем прямой ряд Фибоначчи
for i in range(number, number*2-1):
    fib_number = number1+number2
    number2 = number1
    number1 = fib_number
    new_fib_list.append(fib_number)
print(f'для k = {number} список будет выглядеть так: {new_fib_list}')
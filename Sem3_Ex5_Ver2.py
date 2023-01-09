# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

print('2 способ')
number = int(input('Введите число для составления ряда Фибоначчи: '))

print_number = number

# прямой ряд Фибоначчи
my_fib_list = [0, 1]
for i in range(number-1):
    my_fib_list.append((my_fib_list[i]+my_fib_list[i+1]))

# отзеркалили с минусом
i = 0
count = number
for i in range(number//2):
    if number % 2 == 0:
        if i % 2 == 0:
            b = my_fib_list[count]
            my_fib_list[count] = (-my_fib_list[i])
            my_fib_list[i] = -b
            count -= 1
        else:
            b = my_fib_list[count]
            my_fib_list[count] = (my_fib_list[i])
            my_fib_list[i] = b
            count -= 1
    else:
        if i % 2 != 0:
            b = my_fib_list[count]
            my_fib_list[count] = (-my_fib_list[i])
            my_fib_list[i] = -b
            count -= 1
        else:
            b = my_fib_list[count]
            my_fib_list[count] = (my_fib_list[i])
            my_fib_list[i] = b
            count -= 1
print(my_fib_list)

# добавили к списку прямой ряд Фибоначчи
for i in range(number-1, number*2-1):
    my_fib_list.append((my_fib_list[i]+my_fib_list[i+1]))
print(f'для k = {number} список будет выглядеть так: {my_fib_list}')

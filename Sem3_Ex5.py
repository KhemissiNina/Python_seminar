# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

number = int(input('Введите число для составления ряда Фибоначчи: '))

def Fibonacci(k):
    if k in [1, 2]:
        return 1
    elif k in [0]:
        return 0
    else:
        return Fibonacci(k-1)+Fibonacci(k-2)

my_list = []
for i in range(-number, number+1):
    if i < 0:
        my_list.append(int((-1)**(i+1)*Fibonacci(-i)))
    else:
        my_list.append(Fibonacci(i))
print(f'для k = {number} список будет выглядеть так: {my_list}')

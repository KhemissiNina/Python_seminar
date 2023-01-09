# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

number = int(input('Введите десятичное число: '))
number_print = number

my_list = []
while (number > 1):
    ostatok = number - number//2*2
    number = number//2
    my_list.append(ostatok)
my_list.append(number)

result = 0
for i in range(len(my_list)):
    if my_list[i] == 1:
        result += 10**i
    else:
        continue

print(f'{number_print} -> {result}')
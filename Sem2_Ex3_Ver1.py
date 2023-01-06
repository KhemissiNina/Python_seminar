#Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int

from random import randint

N=int(input('Введите количество элементов списка: '))
start=int(input('Введите диапозон значения чисел от: '))
finish=int(input('                                до: '))
my_list = []

for i in range(N):
    my_list.append(randint(start, finish))
print ('Первоначальный массив:', end=' ')
for i in my_list:
    print(i, end=' ')
print ('')

for i in range(N):
    time_index=randint(0,N-1)
    b=my_list[i]
    my_list[i]=my_list[time_index]
    my_list[time_index]=b

print ('Перемешанный массив:  ', end=' ')
for i in my_list:
    print(i, end=' ')
#Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
#Пример:
#Для n=4 -> [2, 2.25, 2.37, 2.44]
#Сумма 9.06

n = int(input('Введите число для задания последовательности:'))
my_list=[]
sum=0
for i in range (n):
	k=((1 + 1/(i+1))**(i+1))
	if k==int(k):
	    my_list.append(int(k))
	else:
	    my_list.append(round(k,2))
	sum=sum+my_list[i]
print(f'Для числа {n} последовательность: ', my_list)
print(f'Сумма =', sum)
import random

# функция создания словаря
def dict(number):
    dict = {}
    for key in range(number, -1, -1):
        dict[key] = random.randint(-100, 100)
#    dict[2] = 0
#    dict[4]=-1
    return dict

# функция создания многочлена из словаря
def solution(length_dict, my_dict):
    my_str = ''
    for key, value in my_dict.items():
        if key < length_dict+1:
            if value != 0:
                if key == 0:
                    my_str = my_str + '+' + str(value)
                elif key == 1:
                    my_str = my_str + '+' + str(value)+'*x'
                else:
                    my_str = my_str + '+' + (str(value)+'*x' + '^' + str(key))
            else:
                continue
    my_str = my_str.replace('+-', '- ').replace(' ', '').replace('-1*', '-')

    if my_str.startswith('+'):
        my_str = my_str[1:]

    my_str = my_str + '=0'
    return my_str

number = int(input('Введите высшую степень первого многочлена: '))
number1 = int(input('Введите высшую степень второго многочлена: '))

my_dict = (dict(number))
my_dict1 = (dict(number1))

polynomial = (solution(number, my_dict))
polynomial1 = (solution(number1, my_dict1))

print(f'Первый многочлен: {polynomial}')
print(f'Второй многочлен: {polynomial1}')

f = open('sem4\polynomial.txt', 'w')
f.write(polynomial)
f.close()

f1 = open('sem4\polynomial1.txt', 'w')
f1.write(polynomial1)
f1.close()

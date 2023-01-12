def poly(p):
    p = p.replace('=', '^').replace('-', '+-').replace('*x+','^1+').replace('*x', '').replace('^', '+').split('+')
    if (p[0]) == '':
        del p[0]
    return p


def dict(p):
    dict = {int(p[i+1]): int(p[i]) for i in range(0, len(p), 2)}
    return dict

def summa_dict(dictionary1, dictionary2):
    for key in dictionary1.keys():
        if key in dictionary2.keys():
            if len(dictionary1) > len(dictionary2):
                dictionary1[key] = dictionary1[key] + dictionary2[key]
                summa_dict = dictionary1
            else:
                dictionary2[key] = dictionary2[key] + dictionary1[key]
                summa_dict = dictionary2
    return summa_dict

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

with open('sem4\polynomial1.txt') as polynomial1:
    p2 = polynomial1.readline()

with open('sem4\polynomial.txt') as polynomial:
    p1 = polynomial.readline()

print('Даны многочлены')
print(p1)
print(p2)

polynomial1 = poly(p1)
polynomial2 = poly(p2)

dict1 = dict(polynomial1)
dict2 = dict(polynomial2)

summa = summa_dict(dict1, dict2)

len = len(summa)
summa_polynomial = solution(len, summa)
print('Сумма многочленов равна:')
print(summa_polynomial)

f = open('sem4\summa_polynomial.txt', 'w')
f.write(summa_polynomial)
f.close()

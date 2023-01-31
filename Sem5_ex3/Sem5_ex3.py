# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

# функция архивирования
def arhiv(my_list):
    count = 1
    finish_list = []
    for i in range(len(my_list)-1):
        if my_list[i] == my_list[i+1]:
            count += 1
        else:
            finish_list.append(count)
            finish_list.append(my_list[i])
            count = 1
    finish_list.append(count)
    finish_list.append(my_list[i+1])

    finish_list = [str(i) for i in finish_list]

    finish_code = ''.join(finish_list)
    return finish_code

# функция разархивирования
def an_arhiv(my_list):
    finish_code = []
    finish_list = []
    number_list = []

 # если число больше 10
    for i in range(len(my_list)):
        if my_list[i].isdigit():
            number_list.append(my_list[i])
        else:
            finish_list.append(number_list)
            finish_list.append(my_list[i])
            number_list = []

    for i in range(0, len(finish_list), 2):
        finish_list[i] = ''.join(finish_list[i])

    for i in range(len(finish_list)):
        if finish_list[i].isdigit():
            finish_list[i] = int(finish_list[i])
        else:
            continue

    for i in range(0, len(finish_list), 2):
        j = 0
        while j < (finish_list[i]):
            finish_code.append(finish_list[i+1])
            j += 1
    finish_code = ''.join(finish_code)
    return finish_code


# запись в 1 файл исходника
code = input('Введите последовательность: ')
f = open('Sem5_Ex3\Code1.txt', 'w')
f.write(code)
f.close()

my_list_code = list(code)

code2 = (an_arhiv(my_list_code)
         if my_list_code[0].isdigit() else arhiv(my_list_code))

print(f'{code} -> {code2}')

# запись в 2 файл результата
f = open('Sem5_Ex3\Code2.txt', 'w')
f.write(code2)
f.close()
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input('Введите номер четверти (от 1 до 4): '))
if number <= 0 or number > 4:
    print('Вы ввели неверное  значение')
else:
    if number == 1:
        print('Координаты 1-ой четверти: Х от 0 до плюс бесконечности; Y от 0 до плюс бесконечности')
    else:
        if number == 2:
            print(
                'Координаты 2-ой четверти: Х от 0 до минус бесконечности; Y от 0 до плюс бесконечности')
        else:
            if number == 3:
                print(
                    'Координаты 3-ей четверти: Х от 0 до минус бесконечности; Y от 0 до минус бесконечности')
            else:
                print(
                    'Координаты 4-ой четверти: Х от 0 до плюс бесконечности; Y от 0 до минус бесконечности')
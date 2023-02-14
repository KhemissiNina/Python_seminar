
def input_class():
    name_class=input('Выберите класс ').upper()
    while True:
            try:        
                if int(name_class[:-1])>11:
                    name_class = input('Максимальный класс в школе 11. Повторите ввод класса').upper()
                if name_class[-1] in ('F',',','D','U','L','T','A'):
                    name_class = input('Переключите на русскую раскладку и введите класс  ').upper()
                elif name_class[-1] in ('А','Б','В','Г','Д','Е'):
                    break  
                else:
                    name_class = input('Такого класса не существует. Введите класс заново ').upper()
            except ValueError:
                    name_class = input('Неверное значение. Введите класс заново ').upper()         
    return name_class

def input_subject():
    subject=input('\nВыберите предмет\nМожно ввести первую букву ').lower()
    while True:
        if subject.startswith('ф'):
            subject='физика'
            break
        elif subject.startswith('р'):
            subject='русский язык'
            break
        elif subject.startswith('м'):
            subject='математика'
            break
        elif subject.startswith('х'):
            subject='химия'
            break
        elif subject.startswith('п'):
            subject='природоведение'
            break
        else:
            subject = input('Такого предмета в этом классе нет, введите заново ').lower()                                  
     
    return subject

def who_answer(list_student: list):
    pupile=input('\nВведите номер ученика, который будет отвечать ')
    while True:
        try:
            if pupile=='exit':
                break
            elif int(pupile)<(len(list_student)+1):
                break

            else:
                pupile = input('Такого ученика нет. Повторите ввод ')   
        except ValueError:
            pupile = input('Неверное значение. Введите  заново ')  
    return pupile    
   # return int(input('\nВведите номер ученика, который будет отвечать '))

def what_mark():
    mark=input('На какую отметку ответил ученик? ')        
    while True:
        try:
            if 0<int(mark)<6:
                break
            else:
                mark = input('Оценки в пределах от 1 до 5. Повторите ввод ')
        except ValueError:
            mark = input('Неверное значение. Введите  заново ')  
    return mark

def list_of_child(journal: dict, subject: str):
    print()
    print(subject[0].upper()+subject[1:])
    for i, child in enumerate(journal, 1):             #проходим в списке учеников по ключам-ФИО и нумеруем их, начиная с 1
        print(f'{i}. {child:20} {journal.get(child)}') #child это ключ, третьи{} это в списке обратиться пл ключу и проучить его данные

def list_of_subject(list_subject: list):
    print('\nВ классе ведутся следующие предметы: ')
    print('\n'.join(list_subject))

def print_student(student:str):
    print(f'Отвечает {student}')

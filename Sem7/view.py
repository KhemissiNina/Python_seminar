import controller
#функция выбора пользователя
def main_menu():
    command=['Показать все контакты',
            'Открыть файл',
            'Сохранить файл',
            'Новый контакт',
            'Изменить контакт',
            'Удалить контакт',
            'Найти контакт',
            'Выйти из программы']
    print('\nЧем могу помочь?')
    for i in range (len(command)):
        print (f'{i+1}. {command[i]}')
    user_input=int(input())
    return user_input

def show_contacts(phone_book: list): #функция печати книги
    if len(phone_book)>0:
        for item in phone_book:
            print (f'{item[0]} {item[1]} ({item[2]})')
    else:
        print("Телефонная книга пуста или не загружена")

def load_success(): #функция вывода инфы, что книга запущена
    print('Телефонная книга загружена успешно')

def save_success(): 
    print('Телефонная книга успешно сохранена')

def new_contact_success(): 
    print('Новый контакт успешно загружен')

def change_contact_success(rechange_contact: str, phone_book: list):
    if controller.rechange_contact in phone_book :
        print('Контакт успешно изменен')
    else:
        print('Контакт не найден')

def new_contact():
    name=input('Введите имя и фамилию контакта: ')
    phone=input('Введите номер телефона: ')
    comment=input('Введите комментарий: ')
    return name, phone, comment

def found_contact():
    search=input('Введите искомое значение ')
    return search

def delete_contact():
    delete=input('Какой контакт удалить?')
    return delete

def change_input():
    change=input('Какой контакт хотите изменить?')
    print('Введите новые данные контакта')
    return change
phone_book=[]
path='Sem7\phone_book.txt'

def get_phone_book(): #фугкция выдачи книги 
     global phone_book
     return phone_book

def update_phone_book(contact: list):
    global phone_book
    phone_book.append(contact)
    

def open_phone_book(): #функция зарузки книги из файла
    global phone_book
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data=file.readlines()
        for line in data:
            phone_book.append(line.strip().split(';'))
        
def save_phone_book(): #функция сохранения книги в файл
    global phone_book
    global path
    data=[]
    for line in phone_book:
        data.append(';'.join(line))
    with open(path, 'w', encoding='UTF-8') as file:
        data=file.write('\n'.join(data))

def searh_contact(searh: str):
    global phone_book
    searh_results=[]
    for line in phone_book:
        for field in line:
            if searh in field:
                searh_results.append(line)
                break
    return searh_results

def delete_contact(delete: str):
    global phone_book
    for line in phone_book:
        for field in line:
            if delete in field:
                phone_book.remove(line)
    return phone_book

def change_contact(old_name: str, new_name: str):
    global phone_book

    for line in phone_book:
        for field in line:
            if old_name in field:
                phone_book.remove(line)
                phone_book.append(new_name)
            else:
                break
    return phone_book
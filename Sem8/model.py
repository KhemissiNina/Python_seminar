
journal = {}  # список учеников с отметками
list_of_subject = []
list_of_student=[]
new_file=''
file=''
subject = ''  # наименование предмета введеного польхователем
path = ''  # путь


# функция формирования дороги до требуемого файла - добавить проверку на дурака и первод русских букв в английские
def set_class(class_path: str):
    global path
    class_path = class_path.replace('А', 'A').replace('Б', 'B').replace('В', 'V').replace('Г', 'G').replace('Д', 'D')
    # формирование дороги до файла головная папка/+введенный пользователем класс+ расширение .txt
    path = 'Sem8/Classes/' + class_path + '.txt'


def set_subject(our_subject: str):  # функция определения требумого предмета
    global subject
    subject = our_subject


def open_file():                                                  #функция доставания нужной строки предмета
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()                                                                      # чтение файла построково
    for sub in file:                                                 # цикл прохождение по строкам из файла, поиск требуемого предмета
        if sub.split(';')[0] == subject:
                                                                                                # сравниваем левую часть от разреза по; сравниваем с веденным пользователем запросом
                                                                                            # цикл прохождения по разделенной строке справа, которую делим на 2 части по : sub.split... - это по сути сфрпмированный список, просто не присвоен никакой перменной.
            for study in sub.split(';')[1].strip().split(', '):                                 # идем по безымянному временно  сформированному списку и левую часть делаем ключом, а правую значением, формируя список по разделителю пробел
                journal[study.split(':')[0]] = study.split(':')[1].split()

def list_student():
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()                                                                      
    for sub in file:                                                 
        if sub.split(';')[0] == subject:
            for study in sub.split(';')[1].strip().split(', '):       
                list_of_student.append(study.split(':')[0])                  

def list_subject():
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        list_of_subject.append(sub.split(';')[0])


def student_mark(student: str, mark: int):
    marks = journal.get(student)  # получаем список оценок ответившкго ученика
    marks.append(mark)  # в спсисок добавляем оценку
    # в словаре-строке журнала по предмету по ключу ФИО мы перезаписываем значения
    journal[student] = marks


def file_save():
    new_file = []
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:                            # цикл прохождение по строкам из файла, поиск неработавшего предмета
        if sub.split(';')[0] != subject:        # добавляем нработающие предметы в целом неизменнном виде
            new_file.append(sub.strip())
    new_predmet = []                              # список
    for student, marks in journal.new_predmet():  # проходимся и по ключу и по значению
        new_predmet.append(student + ':' + ' '.join(list(map(str, marks))))  # добавляем ключ-ФИО  : и через пробел переводя в строку список оценок
    new_predmet = subject + ';' + ', '.join(new_predmet)                        # добавляем предмет   ;   и выше свофрмированный спсиок через ,пробел
    new_file.append(new_predmet)  # присоединяем выщесозданную конструкцию
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(new_file))

def ask_to_save():
    new_file = []
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:  
        if sub.split(';')[0] != subject:      
            new_file.append(sub.strip())
    new_predmet = []                         
    for student, marks in journal.new_predmet(): 
        new_predmet.append(student + ':' + ' '.join(list(map(str, marks))))  
    new_predmet = subject + ';' + ', '.join(new_predmet)                       
    new_file.append(new_predmet)




def get_journal():  # функция для передачи в работу списка учеников с отметками
    return journal

def get_subject():
    return subject

def get_list_subject():
    return list_of_subject

def get_list_student():
    return list_of_student

def get_new_file():
    return new_file

def get_file():
    return file
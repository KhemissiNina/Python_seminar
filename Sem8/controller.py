import view
import model

def start():
   # model.input_class(view.input_class)
    model.set_class(view.input_class())
    model.list_subject()
    view.list_of_subject(model.get_list_subject())
    model.set_subject(view.input_subject())
    model.open_file()
    while True:
        view.list_of_child(model.get_journal(),model.get_subject())
        model.list_student()
        list_student=model.get_list_student()
        student=view.who_answer(list_student)
        if student=='exit':
            break
        student=list_student[int(student)-1]
        view.print_student(student)
        mark=int(view.what_mark())
        model.student_mark(student, mark)
    #view.ask_for_save(model.get_file(),model.get_new_file())
    model.file_save()






    
    
    
   
    
    
    
 
    
    model.set_class(view.input_class())         #передаем из V в M информацию о выбранном классе
    model.set_subject(view.input_subject())     #передаем из V в M информацию о выьранном предмете
    model.open_file()                           #запускаем в М функцию запуска парксинга строки с нужным предметом
    while True:
        journal=model.get_journal()         #получаем из M список учеников с отметками
        view.list_of_child(journal)         #запускаем из V функцию вывода на экран списка передавая из M его
        student=view.who_answer()               #V запрашиваем кто отвечает
        if student=='exit':
            break
        mark=int(view.who_answer())             #в переменную записваем ответ из V
        model.student_mark(student, mark)
    model.save_fail()
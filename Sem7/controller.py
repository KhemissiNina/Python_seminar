import view
import model

def start():
    user_choice=0
    while user_choice!=8:
        user_choice=view.main_menu()

        match user_choice:
            case 1:
                phone_book=model.get_phone_book()
                view.show_contacts(phone_book)
            case 2:
                model.open_phone_book()
                view.load_success()
            case 3:
                model.save_phone_book()
                view.save_success()
            case 4:
                new=list(view.new_contact())
                model.update_phone_book(new)
                view.new_contact_success()
            case 5:
                change_contact=view.change_input()
                rechange_contact=view.new_contact()
                model.change_contact(change_contact,rechange_contact)
                view.change_contact_success(rechange_contact, phone_book)
            case 6:
                del_contact=view.delete_contact()
                model.delete_contact(del_contact)
            case 7:
                search=view.found_contact()
                result=model.searh_contact(search)
                view.show_contacts(result)

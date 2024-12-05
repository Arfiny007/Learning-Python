from add_contacts import add_contacts
from save_all_contacts import save_all_contacts
from veiw_all_contact import view_all_contact
from load_contacts import load_contact
from remove_contact import remove_contact
from update_contacts import update_contact
from search_contacts import search_contacts
all_contact = load_contact()

while True:
    print("------Contact contact Management System------")
    print("1. Add Contacts")
    print("2. Update Contacts")
    print("3. Remove Contacts")
    print("4. View Contacts")
    print("5. Search Contact")
    print("6. Exit")

    option = input("Select Any Option Between (1-6) :")

    if option == "1" :
       all_contact = add_contacts(all_contact)
    elif option == "2":
        all_contact = update_contact(all_contact)
    elif option == "3" :
        all_contact = remove_contact(all_contact)
    elif option == "4" :
        view_all_contact(all_contact)
    elif option == "5" :
        search_contacts(all_contact)
    elif option == "6" :
        save_all_contacts(all_contact)
        print("----Thanks for Using Contact-contact Management System----")
        break
    else :
        print("Invaild Number. Please Select Any Option Between (1 - 6) ")


    

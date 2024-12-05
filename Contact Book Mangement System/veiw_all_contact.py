
def view_all_contact(all_contact) :
    if all_contact:
        print("\nList of Contacts:")
        for contact in all_contact :
            print(f"Name : {contact['name']} || Phone Number : {contact['phone_number']} || Email : {contact['email']} || Address : {contact['address']}")
    else :
        print("No Contact Has Been Found")
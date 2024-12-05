from save_all_contacts import save_all_contacts


def add_contacts(all_contact) :
    
    while True :
        
        name = input("Enter Contact Name: ").strip()
        if not name.isalpha():
            print("Error: The contact's name must only contain letters. Please try again.")
            continue
        phone_number = input("Enter Phone Number: ").strip()
        if not phone_number.isdigit():
            print("Error: The phone number must only contain digits. Please try again.")
            continue
        
        email = input("Enter Email : ")
        address = input("Enter Address: ")
        for contact in all_contact :
            if contact["phone_number"] == phone_number:
                print("Contact with this phone number already exists!")
                return all_contact
            

        contacts ={
                "name" : name,
                "phone_number" : phone_number,
                "email" : email,
                "address" : address
            }

        all_contact.append(contacts)  
        save_all_contacts(all_contact)
        print("Contact Added Successfully!!")
        return all_contact

from save_all_contacts import save_all_contacts

def remove_contact(all_contact) :
    
    if not all_contact :
        print("No contacts Found")
        return all_contact
    
    remove= input("Enter The Number That You Want To Remove : ").strip()
    if not remove.isdigit():
        print("Error: The phone number must only contain digits. Please try again.")
        
        
    for contact in all_contact:
         if contact['phone_number'] == remove :
            all_contact.remove(contact)
            print(f"The Contact Named {contact['name']} Removed")
            save_all_contacts(all_contact)
            return all_contact
            

    print("No Contact Found With The Given Phone Number.")
    return all_contact
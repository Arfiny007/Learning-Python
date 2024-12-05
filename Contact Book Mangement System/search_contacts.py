from load_contacts import load_contact
def search_contacts(all_contact) :
    all_contact = load_contact()
    search = input("Enter The Contact Name That You Want To Search : ")
    
    result =[]
    
    for contact in all_contact :
        if contact['name'].lower() == search.lower() or contact['email'].lower() == search.lower() :
            result.append(contact)
            
    if result:
        print("Search Results :")
        for contact in result  :
            print(f"Name : {contact['name']} || Phone Number : {contact['phone_number']} || Email : {contact['email']} || Address : {contact['address']}")
    else :
        print("No Contact Found With this Name")
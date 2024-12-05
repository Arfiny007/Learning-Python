from save_all_contacts import save_all_contacts
def update_contact(all_contact):
    if not all_contact:
        print("No Contact Available To Update.")
        return all_contact

    update = input("Enter The Phone Number To Update: ")

    for contact in all_contact:
        if contact['phone_number'] == update:
            print(f"Found Contact: {contact}")
            print("Enter New Details (Leave Blank To Keep The Current Value): ")
            contact["name"] = input(f"New name (current: {contact['name']}): ") or contact["name"]
            contact["phone_number"] = input(f"New phone_number (current: {contact['phone_number']}): ") or contact["phone_number"]
            contact["email"] = input(f"New email (current: {contact['email']}): ") or contact["email"]
            contact["address"] = input(f"New address (current: {contact['address']}): ") or contact["address"]
            print("Contact Updated Successfully!")
            save_all_contacts(all_contact)
            return all_contact

    print("No contact found with the given Number.")
    return all_contact
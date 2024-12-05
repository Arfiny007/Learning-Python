import csv
def save_all_contacts(all_contact) :
    with open ("all_contact.csv",mode="w",newline="") as file:
        writer = csv.DictWriter(file,fieldnames=["name","phone_number","email","address"])
        writer.writeheader()
        writer.writerows(all_contact)
import csv
import os
def load_contact(file_path="all_contact.csv"):
    try :
        if not os.path.exists(file_path):  
            return []  
        with open ("all_contact.csv" , mode= 'r') as file:
            reader = csv.DictReader(file)
            contacts = []
            for contact in reader:
                contacts.append(contact)
            return contacts
    except FileNotFoundError:
        return []
    
    
    
   

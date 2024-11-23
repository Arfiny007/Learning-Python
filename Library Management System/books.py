from add_books import add_books
from view_all_books import view_all_books
from load_books import load_books
from update_books import update_book
from remove_books import remove_book
from save_all_books import save_all_books

all_books = load_books()

while True:
    print("----Welcome to Library Management System----")
    print("1. Add Books")
    print("2. Update Books")
    print("3. Remove Books")
    print("4. View All Books")
    print("5. Exit")

    option = int(input("Select Any Option Between 1 - 5 :"))

    if option == 1 :
        all_books = add_books(all_books)
    elif option == 2 :
        all_books = update_book(all_books)
    elif option == 3 :
        all_books = remove_book(all_books)
    elif option == 4 :
        view_all_books(all_books)

    elif option == 5 :
        save_all_books(all_books)
        print("----Thanks for Using Library Management SystemLibrary Management System----")
        break
    else :
        print("Invaild Number. Please Select Any Option Between (1 - 5) ")



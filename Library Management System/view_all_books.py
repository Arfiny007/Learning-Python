def view_all_books(all_books):
    if all_books != [] :
        for books in all_books:
            print(f"Tittle: {books['title']} | Author: {books['author']} | ISBN: {books['isbn']} | Year: {books['year']} | Price: {books['price']} | Quantity: {books['quantity']}\n")
    else:
        print("No Book found in the System")
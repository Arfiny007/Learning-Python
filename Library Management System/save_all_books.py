import csv
def save_all_books(all_books):
    with open("all_books.csv", mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "author", "isbn", "year", "price", "quantity"])
        writer.writeheader()
        writer.writerows(all_books)
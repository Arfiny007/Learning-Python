
import csv
def load_books():
    try:
        with open("all_books.csv", mode="r") as file:
            reader = csv.DictReader(file)
            return [book for book in reader]
    except FileNotFoundError:
        return []


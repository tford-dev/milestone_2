import json;

books = [];

def add_book():
    with open('books.json', 'a') as file:
        json.dump(books, file);
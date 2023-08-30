import json;

books = [];

def call_books(list_arr):
    print("Generating list of books in directory...................................................................")
    for book in books:
        print(f"\nBook Title: {book['name'].title()}\n{book['name'].title()} Author: {book['author'].title()}\n{book['name'].title()} Read?: {book['read']}\n");

def add_book(list_arr):
    filename = 'utils/books.json';
    try:
        with open(filename, 'r') as file:
            data = json.load(file);
            for book in data:
                list_arr.append(book);
        print("Generating list of books in directory...................................................................")
        for book in list_arr:
            print(f"\nBook Title: {book['name'].title()}\n{book['name'].title()} Author: {book['author'].title()}\n{book['name'].title()} Read?: {book['read']}\n"); 
    except FileNotFoundError:
        print(f"File in directory is empty, improperly formatted, or corrupted");

""" def add_book():
    with open('books.json', 'a') as file:
        json.dump(books, file);"""

add_book();
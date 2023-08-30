import json;

#Initial array/list
books = [];

#generic helper function that is currently called in add_book() and in list_books() in app.py
def call_books(list_arr):
    print("Generating list of books in directory...................................................................")
    #loops through data/books in a list 
    for book in list_arr:
        print(f"\nBook Title: {book['name'].title()}\n{book['name'].title()} Author: {book['author'].title()}\n{book['name'].title()} Read?: {book['read']}\n");

#helper function to open json file
def read_call(filepath):
    with open(filepath, 'r') as file:
        current_data = json.load(file);
    return current_data;

#helper function to overwrite json file
def write_call(filepath, list_arr):
    with open(filepath, 'w') as file:
        json.dump(list_arr, file, indent=4);
    return list_arr;


#The purpose of this function is so that data from books.json can be added to the books list
def add_book(list_arr):
    filename = 'utils/books.json';
    #try/except block for if there's no data in books.json
    try:
        #Open and read books.json
        with open(filename, 'r') as file:
            data = json.load(file);
            for book in data:
                #adds each book object/dictionary to list/array
                list_arr.append(book);
        #display data in list/array after being copied
        call_books(list_arr);
    except FileNotFoundError:
        print(f"File in directory is empty, improperly formatted, or corrupted.");

add_book(books);
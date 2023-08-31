#The whole point of this file is to add json data to a list so it's more simple to view data
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

#helper function to overwrite json file
def write_call(filepath, list_arr):
    #Reliable way to clear books list
    del books[:]
    with open(filepath, 'w') as file:
        json.dump(list_arr, file, indent=4);
    #This line is to add current json data into books list
    add_book(books);
    return list_arr;
import json;
from utils import database;

USER_CHOICE = """
Enter: 
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' or any other key to quit;
Your choice: """

def prompt_add_book():
    book_name = input("Howdy, what is the name of the book you would like to add to the database? ");
    book_author = input(f"What is the author of the book {book_name.title()}??? ");
    obj_to_push = {'name': book_name, 'author': book_author, 'read': False};
    with open('utils/books.json', 'r') as file:
        current_data = json.load(file);
    current_data.append(obj_to_push);
    with open('utils/books.json', 'w') as file:
        json.dump(current_data, file, indent=4);
    print(f"{obj_to_push} has been added to database.");

def list_books():
    with open('utils/books.json', 'r') as file:
        current_data = json.load(file);
    if(len(current_data) > 0):
        print("Generating list of books in directory...................................................................")
        for book in current_data:
            print(f"\nBook Title: {book['name'].title()}\n{book['name'].title()} Author: {book['author'].title()}\n{book['name'].title()} Read?: {book['read']}\n");
    else: 
        print("Directory is empty.");

def prompt_read_book():
    book_name_lookup = input("What is the name of the book you would like to mark as read? ");
    with open('utils/books.json', 'r') as file:
        data = json.load(file);
    book_match = False;
    for book in data:
        if book_name_lookup.lower() == book['name'].lower():
            book_match = True;
            if book['read']:
                print(f"{book['name'].title()} has already been read.");
            else:
                book['read'] = True;
                with open('utils/books.json', 'w') as file:
                    json.dump(data, file, indent=4)
                print(f"{book['name'].title()} has been marked as read.");
            break;
    if not book_match:
        print(f"{book_name_lookup.title()} is not in directory.");

""" def prompt_read_book():
    book_name_lookup = input("What is the name of the book you would like to mark as read? ");
    with open('utils/books.json', 'r') as file:
        data = json.load(file);
    book_match = False;
    for book in data:
        if ((book_name_lookup.lower() == book['name'].lower()) and book['read']):
            print(f"{book['name'].title()} has already been marked as read.");
            break
        elif ((book_name_lookup.lower() == book['name'].lower()) and not book['read']):
            book['read'] = True;
            with open('utils/books.json', 'w') as file:
                json.dump(data, file, indent=4);
            print(f"{book['name'].title()} has been marked as read.");
            break;
        else:
            print(f"{book_name_lookup} is not in directory"); 
            break; """

def prompt_delete_book():
    book_name_lookup = input("What is the name of the book you would like to delete? ");
    with open('utils/books.json', 'r') as file:
        data = json.load(file);
    updated_data = [];
    book_found = False;
    for book in data:
        if (book['name'].lower() == book_name_lookup.lower()):
            book_found = True
            print(f"{book['name'].title()} has been deleted from the directory.");
        else:
            updated_data.append(book);
    if book_found:
        with open('utils/books.json', 'w') as file:
            json.dump(updated_data, file, indent=4);
    else:
        print(f"{book_name_lookup} is not in directory"); 


def menu():
    while True:
        user_input = input(USER_CHOICE);
        if user_input.lower() == 'a':
            prompt_add_book();
        elif user_input.lower() == 'l':
            list_books();
        elif user_input.lower() == 'r':
            prompt_read_book();
        elif user_input.lower() == 'd':
            prompt_delete_book();
        elif user_input.lower() == 'q':
            print("Process terminated.");
            break;
        else:
            print("Invalid choice.\nPlease choose a valid option.");

menu();
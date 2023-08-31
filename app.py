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

#function to make sure there is an array in books.json if there is no data in the file
def create_book_table():
    try:
        database.read_call('utils/books.json');
    except json.JSONDecodeError:
        with open('utils/books.json', 'w') as file:
            json.dump([], file);

#function to add book to books.json
def prompt_add_book():
    #while loop so it is possible for users to quit process
    while True:
        book_name = input("Howdy, what is the name of the book you would like to add to the database? ");
        if book_name.lower() == 'q':
            break;
        book_author = input(f"What is the author of the book {book_name.title()}??? ");
        if book_author.lower() == 'q':
            break;
        #template for object to be stored in books.json
        obj_to_push = {'name': book_name, 'author': book_author, 'read': False};
        #open json file
        current_data = database.read_call('utils/books.json')
        #copy objects as dictionaries into current_data
        current_data.append(obj_to_push);
        database.write_call('utils/books.json', current_data);
        print(f"{obj_to_push} has been added to .json database.");

#function to list books in books.json
def list_books():
    #open json file
    current_data = database.read_call('utils/books.json');
    #if there is data in current data, the function 'call_books()' from utils/database.py is called to list dictionaries in current_data
    if(len(current_data) > 0):
        database.call_books(current_data);
    else: 
        print("Directory is empty.");

#function to to turn the 'read' value in books.json to true
def prompt_read_book():
    #while loop so it is possible for users to quit process
    while True:
        book_name_lookup = input("What is the name of the book you would like to mark as read? ");
        if book_name_lookup.lower() == 'q':
            break;
        #open json file and copy objects as dictionaries into current_data
        current_data = database.read_call('utils/books.json');
        #initial boolean for this function
        book_match = False;

        for book in current_data:
            #if book name from user input matches the book name
            if book_name_lookup.lower() == book['name'].lower():
                #sets boolean for if there's a match
                book_match = True;
                #If the book that matches is already read, then the following message will be sent to the user
                if book['read']:
                    print(f"{book['name'].title()} has already been read.");
                else:
                    #sets boolean for if there's a match
                    book['read'] = True;
                    #overwrite data in books.json with updated data from current_data
                    database.write_call('utils/books.json', current_data);
                    print(f"{book['name'].title()} has been marked as read.");
                break;
        if not book_match:
            print(f"{book_name_lookup.title()} is not in directory.");

#function to delete a book from books.json
def prompt_delete_book():
    #while loop so it is possible for users to quit process
    while True:
        book_name_lookup = input("What is the name of the book you would like to delete? ");
        if book_name_lookup.lower() == 'q':
            break;
        #open json file
        data = database.read_call('utils/books.json');
        #initial array/list
        updated_data = [];
        #initial boolean
        book_found = False;
        #loops through copied dictionaries/objects in data list
        for book in data:
            #if book name from user input matches the book name
            if (book['name'].lower() == book_name_lookup.lower()):
                #sets boolean for if there's a match
                book_found = True
                print(f"{book['name'].title()} has been deleted from the directory.");
            else:
                #If book in loop does not match user input, add it to updated_data list before books.json is overwritten
                updated_data.append(book);
        #If book is found, overwrite data in books.json
        if book_found:
            database.write_call('utils/books.json', updated_data);
        else:
            print(f"{book_name_lookup.title()} is not in directory"); 

#Function to call other functions in file and set console session
def menu():
    create_book_table();
    #While loop so that menu() can be ran indefinetly and USER_CHOICE prompt can be displayed after a function is called.
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
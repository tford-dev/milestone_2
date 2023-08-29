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
    book_author = input(f"What is the author of the book {book_name}??? ");
    obj_to_push = {'name': book_name, 'author': book_author, 'read': False}
    database.books.append(obj_to_push);
    print(f"{obj_to_push} has been added to database.");

def list_books():
    if(len(database.book) > 0):
        for book in database.books:
            print(f"Book Title: {book.name.title()}\n{book.name.title()} Author: {book.author.title()}\n{book.name.title()} read?:");
    else: 
        print("Directory is empty.");

def prompt_read_book():
    book_name_lookup = input("What is the name of the book you would like to mark as read? ");
    temporary_obj = None;
    for book in database.books:
        if book['name'].lower() == book_name_lookup.lower():
            database.books.remove(book);
            temporary_obj = book;
            break;
    if temporary_obj == None:
        print("Book not found in directory. I'm so sorry. ");
    elif temporary_obj['read'] == True:
        print(f"{temporary_obj['name'].title()} has already been read.");
    else:
        temporary_obj['read'] = True
        database.books.append(temporary_obj);
        print(f"{temporary_obj} has been updated and added to database.");
        print(f"The book {temporary_obj['name'].title()} is now set to read.");

def prompt_delete_book():
    book_name_lookup = input("What is the name of the book you would like to mark as read?");
    for book in database.books:
        if book['name'].lower() == book_name_lookup.lower():
            database.books.remove(book);
            print(f"{book['name'].title()} has been deleted. ")
            break;
    

def menu():
    user_input = input(USER_CHOICE);
    while user_input != 'q':
        if user_input.lower() == 'a':
            prompt_add_book();
        elif user_input.lower() == 'l':
            list_books();
        elif user_input.lower() == 'r':
            prompt_add_book();
        elif user_input.lower() == 'd':
            prompt_delete_book();
        else:
            break;
    print("Process terminated.");

menu();
import sqlite3;

USER_CHOICE = """
Enter: 
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' or any other key to quit;
Your choice: """

def create_book_table_sql():
    connection = sqlite3.connect('data.db');
    cursor = connection.cursor();
    cursor.execute('CREATE TABLE IF NOT EXISTS books(name TEXT primary key, author TEXT, read BOOLEAN)');
    connection.commit()
    connection.close();

def prompt_add_book():
    while True:
        try:
            book_name = input("Howdy, what is the name of the book you would like to add to the database? ");
            if book_name.lower() == 'q':
                break;
            book_author = input(f"What is the author of the book {book_name.title()}??? ");
            if book_author.lower() == 'q':
                break;
            #Sql portion
            # ",0); DROP TABLE books; ... not good
            connection = sqlite3.connect('data.db');
            cursor = connection.cursor();
            #You must put quotation marks around values so sql does'nt think it's a table
            #Do not do direct query formatting to prevent injection attacks
            cursor.execute("INSERT INTO books VALUES(?, ?, 0)", (book_name, book_author));
            print(f"Object successfully pushed to data.db: {book_name} by {book_author}");
            connection.commit()
            connection.close();
        except sqlite3.IntegrityError:
            print("Book already in directory, please enter a unique book.")

def list_books():
    #sql portion
    connection = sqlite3.connect('data.db');
    cursor = connection.cursor();
    cursor.execute('SELECT * FROM books');
    #turns initial tuple in a dictionary
    books = []
    for row in cursor.fetchall():
        book = {'name': row[0], 'author': row[1], 'read': row[2]}
        books.append(book);
    connection.close();
    print(books);

def prompt_read_book():
    while True:
        book_name_lookup = input("What is the name of the book you would like to mark as read? ");
        if book_name_lookup.lower() == 'q':
            break;
        connection = sqlite3.connect('data.db');
        cursor = connection.cursor();
        try:
            #Query to look up book in table by name with book_name_lookup
            cursor.execute("SELECT read FROM books WHERE name=?", (book_name_lookup,));
            #Selects one row based on the what is SELECTed('read' key was selected)
            row = cursor.fetchone();
            #If there's no row at all....
            if row is None:
                print(f"Book '{book_name_lookup.title()}' not found in the database.");
            #IF the row that was fetched is true..... 1 is true in sql
            elif (row[0] == 1):
                print(f"{book_name_lookup.title()} has already been read.");
            #Sets 'read' key to true in table if 'read' == 0 initially(falsey)
            else:
                cursor.execute("UPDATE books SET read=1 WHERE name=?", (book_name_lookup,));
                connection.commit();
                print(f"Book '{book_name_lookup.title()}' has been marked as read.");
        except sqlite3.Error:
            print("Error occured when updating database.");
        finally:
            connection.close();

def prompt_delete_book():
    while True:
        book_name_lookup = input("What is the name of the book you would like to mark as read? ");
        if book_name_lookup.lower() == 'q':
            break;
        connection = sqlite3.connect('data.db');
        cursor = connection.cursor();
        try:
            cursor.execute('DELETE FROM books WHERE name=?', (book_name_lookup,));
            if cursor.rowcount > 0:
                connection.commit();
                print(f"Book {book_name_lookup.title()} has been deleted from database.");
            else: 
                print(f"{book_name_lookup.title()} is not found in table. Please enter a different query.");
        except sqlite3.Error:
            print("Error occured when updating database.");
        finally:
            connection.close();

#Function to call other functions in file and set console session
def menu():
    create_book_table_sql();
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
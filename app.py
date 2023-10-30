import random
import datetime
import re


"""
==================
This section contain the classes that
==================

"""


#defining the book class
class Book:
    def __init__(self, title, author, year, publisher, num_copies, publication_date):
            self.book_id = random.randint(1, 1000)
            self.title = title
            self.author = author
            self.year = year
            self.publisher = publisher
            self.total_copies = num_copies
            self.available_copies = num_copies
            self.publication_date = publication_date

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_total_copies(self):
        return self.total_copies

    def get_available_copies(self):
        return self.available_copies

    def get_publication_date(self):
        return self.publication_date

    def borrow_book(self, num_copies=1):
        if self.available_copies >= num_copies:
            self.available_copies -= num_copies
            return True
        else:
            return False
        
    def return_book(self, num_copies=1):
        if self.available_copies + num_copies <= self.total_copies:
            self.available_copies += num_copies
            return True
        else:
            return False

    def modify_book(self):
        #this method modifies an exisiting book details
            print("Modify Book Details:")
            self.title = input(f"Title ({self.title}): ") 
            self.author = input(f"Author ({self.author}): ") 
            self.year = input(f"Publication Year ({self.year}): ")
            self.publisher = input(f"Publisher ({self.publisher}): ") 
            while True:
                num_copies = input(f"Number of Copies ({self.total_copies}): ") 
                if num_copies.isdigit():
                    num_copies = int(num_copies)
                    if num_copies > 0:
                        self.total_copies = num_copies
                        self.available_copies = num_copies
                        break
                    else:
                        print(" Please provide a positive number of copies.")
                else:
                    print("Please Please provide a valid integer for the number of copies.")
            self.publication_date = input(f"Publication Date ({self.publication_date}): ") or self.publication_date


#defining the BookList class

class BookList:
    # ... (BookList class methods)
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def search_book(self, search_field, search_value):
        matching_books = []
        for book in self.books.values():
            if search_value.lower() in getattr(book, search_field).lower():
                matching_books.append(book)
        return matching_books

    def remove_book(self, title):
        to_remove = None
        for book in self.books.values():
            if book.title.lower() in book.get_title().lower():
                to_remove = book
                break
        if to_remove:
            del self.books[to_remove.book_id]
            print(f"{book.title} as been removed from the Library")

    def get_total_books(self):
        return len(self.books)
    
    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        else:
            return False

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        else:
            return False


class User:
    # User class code 
    def __init__(self, username, firstname, surname, house_number, street_name, postcode, email, date_of_birth):
        self.username = username.lower()
        self.firstname = firstname
        self.surname = surname
        self.house_number = house_number
        self.street_name = street_name
        self.postcode = postcode
        self.email = email
        self.date_of_birth = date_of_birth

    def get_username(self):
        return self.username

    def get_firstname(self):
        return self.firstname

    def get_surname(self):
        return self.surname

    def modify_user(self):
        print("Modify User Details:")
        self.firstname = input(f"First Name ({self.firstname}): ") 
        self.surname = input(f"Surname ({self.surname}): ") 

        while True:
            email = input(f"Email ({self.email}): ") 
            if validate_email(email):
                email = email
                break
            else:
                print("Invalid email format. Please provide a valid email ")

        while True:
            date_of_birth = input(f"D.O.B ({self.date_of_birth}): ") 
            if validate_date_of_birth(date_of_birth):
                date_of_birth = date_of_birth
                break
            else:
                print("Invalid date format. Please provide a valid date of birth (YYYY-MM-DD).")

 #UserList class code defining     
class UserList:
   
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.username] = user

    def remove_user(self, firstname):
        matching_users = [user for user in self.users.values() if user.firstname == firstname]
        if len(matching_users) > 1:
            print("Multiple users with the same first name. Provide more information to remove.")
        elif len(matching_users) == 1:
            del self.users[matching_users[0].username]
        else:
            print("User not found.")

    def get_total_users(self):
        return len(self.users)

    def get_user_details(self, username):
        return self.users.get(username, None)


   # Loans class code defining

class Loans:

    def __init__(self):
            self.loan_books = {} 
           

    def borrow_book(self, user, book):
        if book.get_available_copies() > 0:
            book.available_copies -= 1
            self.loan_books[(user.get_username(), book.book_id)] = datetime.datetime.now()
            print(f"{user.get_username()} borrowed {book.title}.")
            return True
        else:
            return False

    def return_book(self, user, book):
        if (user.get_username(), book.book_id) in self.loan_books:
            book.available_copies += 1
            del self.loan_books[(user.get_username(), book.book_id)]
            print(f"{user.get_username()} returned {book.get_title()}.")
            return True
        else:
            print("Book not found in the user's borrowed list.")
            return False
        
    def get_borrowed_books(self, user):
        print("Overdue Books:")
        for loan in self.loan_books:
            print(user.username)
            user = user_list.get_user_by_username(loan['user'].get_username())
            book = book_list.get_book_by_id(loan['book'].book_id)
            print(f"User: {user.get_username()}, First Name: {user.get_firstname()}")
            print(f"Overdue Book: {book.get_title()}, Due Date: {loan['due_date']}")

    def count_borrowed_books(self, user):
        count = sum(1 for key in self.loan_books.keys() if key[0] == user.get_username())
        return count

    def get_overdue_books(self, user_list):
        current_time = datetime.datetime.now()
        for key, borrow_date in self.loan_books.items():
            username, book_id = key
            user = user_list.get_user_details(username)
            book = book_list.books[book_id]
            due_date = borrow_date + datetime.timedelta(days=14)
            if current_time > due_date:
                print(f"Overdue: {book.get_title()} borrowed by {user.get_firstname()} {user.get_surname()}")


    def print_overdue_books(self, user_list, book_list):
        current_date = "2023-10-27"  # Replace with the actual current date

        print("Overdue Books:")
        for loan in self.loaned_books:
            user = user_list.get_user_by_username(loan['user'].get_username())
            book = book_list.get_book_by_id(loan['book'].book_id)

            if loan['due_date'] < current_date:
                print(f"User: {user.get_username()}, First Name: {user.get_firstname()}")
                print(f"Overdue Book: {book.get_title()}, Due Date: {loan['due_date']}")


#application menu display function 

def application_menu(logged_in_user):
    if logged_in_user:
        print("\nLibrary Menu (Logged In as {}):".format(logged_in_user.get_username()))
        print("1. Search for Books")
        print("2. Add a Book")
        print("3. Return a Borrowed Book")
        print("4. Modify User Details")
        print("5. Modify Book Details")
        print("6. Remove a Book")
        print("7. Borrowed Books")
        print("8. Log Out")
        print("9. Exit")
    else:
        print("\nLibrary Menu (Not Logged In):")
        print("1. Create Account")
        print("2. Log In")
        print("3. Exit")






"""
==================

This section contains functions that run specific tailored aspects of this application feeding of the classes params.

==================


"""

#a function to validate email
def validate_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$', email)

#a function to help validate if input d.o.b is a d.o.b
def validate_date_of_birth(date_of_birth):
    try:
        datetime.datetime.strptime(date_of_birth, "%Y-%m-%d")
        return True
    except ValueError:
        return False

#creating an account function
def create_account(user_list):

    username = input("Please provide a username: ")
    firstname = input("Please provide  your first name: ")
    surname = input("Please provide  your surname: ")
    house_number = input("Please provide  your house number: ")
    street_name = input("Whats your street name: ")
    postcode = input("Please provide  your postcode: ")

    while True:
        email = input("Please provide  your email address: ")
        if validate_email(email):
            email = email
            break
        else:
         print("Invalid email format. Please provide a valid email ") 

    while True:
        date_of_birth = input("Please provide your date of birth (YYYY-MM-DD): ")
        if validate_date_of_birth(date_of_birth):
            date_of_birth = date_of_birth
            break
        else:
            print("Invalid date format. Please provide a valid date of birth (YYYY-MM-DD).")


#if all validation and input is provided we create the user using the User object which is intialized off the User class
    add_new_user = User(username, firstname, surname, house_number, street_name, postcode, email, date_of_birth)
    user_list.add_user(add_new_user)
    print("Account has been created !")

#a function to log in  a user it checks if user is in the  list storing the user object list
def log_in_account(user_list):
    username = input("Please provide your username: ").lower()

    if username in user_list.users:
        return user_list.users[username]
    else:
        print("\n ** Authentication Failed, Please create new account or log in")
        return None
    
# a function to borrow a book.
def borrow_book(user_list, book_list, loan_books, user):
    if user:
        book_title = input("Enter the title of the book you want to borrow: ")
        matching_books = book_list.search_book("title", book_title)
        if matching_books:
            for i, book in enumerate(matching_books):
                print(f"{i + 1}. {book.get_title()} by {book.get_author()}")
                while True:
                    choice = int(input("Please enter the listed index number of the book you want to borrow: ")) - 1
                    if 0 <= choice < len(matching_books):
                        loan_books.borrow_book(user, matching_books[choice])
                        break
                    else:
                        
                        print("Wrong choice, please try again")
        else:
                print(f"No books found with title '{book_title}'.")
    else:
        print("User not found. Please create an account first.")

    
#a function to modify book details
def modify_book_details(book_list):
    print("Modify Book Details:")
    title = input("Please provide  the title of the book you want to modify: ")
    matching_books = book_list.search_book("title", title)

    if matching_books:
        book = matching_books[0]
        book.modify_book()
    else:
        print(f"Book with title '{title}' not found.")


#a function to search for books
def search_books(book_list, user, loaned_books):
    print("Search for Books:")
    search_field = input("Search by (title, author, publisher, publication date): ").strip().lower()
    search_value = input(f"Enter the {search_field} to search for: ").strip()

    matching_books = book_list.search_book(search_field, search_value)

    if matching_books:
        print("Matching Books:")
        for i, book in enumerate(matching_books, start=1):
            print(f"{i}. Title: {book.get_title()}")
        
        choice = input("Do you want to borrow a book from this list? (yes/no): ").strip().lower()

        if choice == "yes":
            book_choice = int(input("Enter the number of the book you want to borrow: "))
            if 1 <= book_choice <= len(matching_books):
                selected_book = matching_books[book_choice - 1]

                # Ask the user how many copies they want to borrow
                while True:
                    try:
                        num_copies = int(input("Enter the number of copies you want to borrow: "))
                        if 1 <= num_copies <= selected_book.get_available_copies():
                            break
                        else:
                            print(f"Invalid input. Please enter a valid number of copies. You can only borrow between 1 - { selected_book.get_available_copies() } copies")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                
                # Borrow the selected book
                if selected_book.borrow_book(num_copies):
                    print(f"You have successfully borrowed {num_copies} copies of '{selected_book.get_title()}'.")
                    loaned_books.borrow_book(user, selected_book)
                else:
                    print("No available copies to borrow.")
            else:
                print("Invalid choice. Please enter a valid book number.")
        elif choice == "no":
            print("You chose not to borrow a book.")
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
    else:
        print(f"No books found with {search_field}: '{search_value}'")

    input("Press Enter to continue...")


# a function to add a book
def add_book(book_list):
    print("Add a Book to the Library:")
    title = input("Title: ")
    author = input("Author: ")
    year = input("Publication Year: ")
    publisher = input("Publisher: ")
    while True:
        num_copies = input("Number of Copies: ")
        if num_copies.isdigit() and int(num_copies) > 0:
            num_copies = int(num_copies)
            break
        else:
            print("Please provide a valid positive integer for the number of copies.")

    while True:
           publication_date = input("Publication Date (YYYY-MM-DD) : ")
           if validate_date_of_birth(publication_date):
            publication_date = publication_date
            break
           else:
            print("Invalid date format. Please provide a publication date (YYYY-MM-DD).")

    

    new_book = Book(title, author, year, publisher, num_copies, publication_date)
    book_list.add_book(new_book)
    print(f"{title} by {author} added to the library.")


# a functin to return a book
def return_borrowed_book(user_list, book_list, loan_books, user):
    print("Return a Borrowed Book:")
    title = input("Enter the title of the book you want to return: ")
    matching_books = book_list.search_book("title", title)

    if matching_books:
        book = matching_books[0]
        loan_books.return_book(user, book)
    else:
        print(f"Book with title '{title}' not found in your borrowed books.")


def remove_book(book_list):
    print("Remove a Book:")
    title = input("Enter the title of the book you want to remove: ")
    matching_books = book_list.search_book("title", title)

    if matching_books:
        book = matching_books[0]
        book_list.remove_book(book)
    else:
        print(f"Book with title '{title}' not found.")


def show_borrowed_books(loaned_books, user):
    print("Borrowed Books:")
    borrowed_books = loaned_books.get_borrowed_books(user)

    if not borrowed_books:
        print("You haven't borrowed any books.")
    else:
        for i, book in enumerate(borrowed_books, start=1):
            print(f"{i}. {book['book'].get_title()}")

    input("Press Enter to continue...")


            
"""

==================

 The Logic flow running the application.

==================

"""



if __name__ == "__main__": #making sure am running the main program script
   

    book_list = BookList() #intializing the book class 
    user_list = UserList() #userlist 
    loan_books = Loans() #to interact and loan, return the books.
    logged_in_user = None #a variable to store if a user is logged in or not. 

    # Created demo books the library
    book1 = Book(title="Banger", author="O.A Fem", num_copies=5, year= 2022, publisher="Macmillian Books", publication_date="1966-03-13")
    book2 = Book(title="Switch", author="Taylor Gomez", num_copies=3, year= 2021, publisher="Argo Books", publication_date="1991-08-01")
    book_list.add_book(book1)
    book_list.add_book(book2)

    # Demo users to the system
    user1 = User(username="Olawale", firstname="Olawale", surname="Olamide", house_number="5c", street_name="Settle St", 
                 postcode="LA142TL", email="olawale@example.com", date_of_birth="1994-03-11")
    user2 = User(username="Love", firstname="Love", surname="Akinola", house_number="3f", street_name="Brig St", 
                 postcode="LA142RB", email="love@example.com", date_of_birth="1999-01-01")
    user_list.add_user(user1)
    user_list.add_user(user2)



    while True:
        application_menu(logged_in_user)
        

        if not logged_in_user:
            choice = input("** Please select an option between <1 - 3> : ")

            if choice == "1":
                logged_in_user = create_account(user_list)
            elif choice == "2":
                logged_in_user = log_in_account(user_list)
            elif choice == "3":
                print("See you later!")
                break
            else:
                print("Not acceptable option picked. Please select a valid option.")
        else:
            choice = input("** Please select an option between <1 - 9> : ")

            if choice == "1":
                search_books(book_list, logged_in_user, loan_books)
            elif choice == "2":
                add_book(book_list)
            elif choice == "3":
                return_borrowed_book(user_list, book_list, loan_books, logged_in_user)
            elif choice == "4":
                logged_in_user.modify_user()
            elif choice == "5":
                modify_book_details(book_list)
            elif choice == "6":
                remove_book(book_list)
            elif choice == "7":
                show_borrowed_books(loan_books, user_list)
            elif choice == "8":
                logged_in_user = None
            elif choice == "9":
                print("Thanks for using our service!")
                break
            else:
                print("Please select a valid option.")

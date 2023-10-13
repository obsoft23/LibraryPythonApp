import random
import datetime

class Book:
    def __init__(self, title="", author="", year="", publisher="", num_copies=0, publication_date=None):
        self.book_id = random.randint(1000, 9999)
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.num_copies = num_copies
        self.available_copies = num_copies
        self.publication_date = publication_date

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_year(self, year):
        self.year = year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def set_num_copies(self, num_copies):
        if num_copies >= 0:
            self.num_copies = num_copies
            self.available_copies = num_copies

    def set_publication_date(self, publication_date):
        try:
            datetime.datetime.strptime(publication_date, "%Y-%m-%d")
            self.publication_date = publication_date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_num_copies(self):
        return self.num_copies

    def get_available_copies(self):
        return self.available_copies

    def get_publication_date(self):
        return self.publication_date

class BookList:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def remove_book(self, title):
        for book_id, book in list(self.books.items()):
            if book.get_title() == title:
                del self.books[book_id]
                return True
        return False

    def search_book(self, attribute, value):
        matching_books = []
        for book in self.books.values():
            if getattr(book, attribute, None) == value:
                matching_books.append(book)
        return matching_books

    def total_books(self):
        return len(self.books)

class User:
    def __init__(self, username, firstname, surname, house_number, street_name, postcode, email, date_of_birth):
        self.username = username
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

    def get_house_number(self):
        return self.house_number

    def get_street_name(self):
        return self.street_name

    def get_postcode(self):
        return self.postcode

    def get_email(self):
        return self.email

    def get_date_of_birth(self):
        return self.date_of_birth

    def edit_firstname(self, new_firstname):
        self.firstname = new_firstname

    def edit_surname(self, new_surname):
        self.surname = new_surname

    def edit_email(self, new_email):
        self.email = new_email

    def edit_date_of_birth(self, new_date_of_birth):
        self.date_of_birth = new_date_of_birth

class UserList:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.get_username()] = user

    def remove_user(self, firstname):
        matching_users = [username for username, user in self.users.items() if user.get_firstname() == firstname]
        if len(matching_users) == 1:
            del self.users[matching_users[0]]
            return True
        elif len(matching_users) > 1:
            print("Multiple users found with the same first name. Please specify the username.")
        return False

    def count_users(self):
        return len(self.users)

    def get_user_details(self, username):
        return self.users.get(username)

class Loans:
    def __init__(self):
        self.loans = []

    def borrow_book(self, user, book):
        if book.get_available_copies() > 0:
            book.available_copies -= 1
            self.loans.append((user, book))
            return True
        else:
            return False

    def return_book(self, user, book):
        if (user, book) in self.loans:
            book.available_copies += 1
            self.loans.remove((user, book))
            return True
        else:
            return False

    def count_borrowed_books(self, user):
        return len([loan for loan in self.loans if loan[0] == user])

    def get_overdue_books(self):
        today = datetime.date.today()
        overdue_books = []
        for user, book in self.loans:
            if today > datetime.datetime.strptime(book.get_publication_date(), "%Y-%m-%d").date():
                overdue_books.append((user.get_username(), user.get_firstname(), book.get_title()))
        return overdue_books

def display_menu():
    print("\nLibrary Menu:")
    print("1. Create Account")
    print("2. Search for Books")
    print("3. Add a Book")
    print("4. Borrow a Book")
    print("5. Exit")

def create_account(user_list):
    username = input("Enter a username: ")
    firstname = input("Enter your first name: ")
    surname = input("Enter your surname: ")
    house_number = input("Enter your house number: ")
    street_name = input("Enter your street name: ")
    postcode = input("Enter your postcode: ")
    email = input("Enter your email address: ")
    date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")

    new_user = User(username, firstname, surname, house_number, street_name, postcode, email, date_of_birth)
    user_list.add_user(new_user)
    print("Account created successfully!")

def search_books(book_list, user, loans):
    search_criteria = input("Enter search criteria (title/author/publisher/publication date): ")
    search_value = input("Enter search value: ")

    matching_books = book_list.search_book(search_criteria, search_value)
    if matching_books:
        print("\nMatching Books:")
        for i, book in enumerate(matching_books):
            print(f"{i + 1}. {book.get_title()} by {book.get_author()}")
        
        loan_choice = input("Do you want to borrow a book (yes/no)? ").lower()
        if loan_choice == "yes":
            book_choice = int(input("Enter the number of the book you want to borrow: ")) - 1
            if 0 <= book_choice < len(matching_books):
                borrow_book(user, matching_books[book_choice], loans)
            else:
                print("Invalid choice.")
    else:
        print("\nNo matching books found.")

def add_book(book_list):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = input("Enter book publication year: ")
    publisher = input("Enter book publisher: ")
    num_copies = int(input("Enter number of copies: "))
    publication_date = input("Enter publication date (YYYY-MM-DD): ")

    new_book = Book(title, author, year, publisher, num_copies, publication_date)
    book_list.add_book(new_book)
    print("Book added successfully!")

def borrow_book(user, book, loans):
    if loans.borrow_book(user, book):
        print(f"You have successfully borrowed '{book.get_title()}'.")
    else:
        print(f"Sorry, '{book.get_title()}' is not available for borrowing.")

def main():
    book_list = BookList()
    user_list = UserList()
    loans = Loans()
    logged_in_user = None

    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            create_account(user_list)
        elif choice == "2":
            if logged_in_user:
                search_books(book_list, logged_in_user, loans)
            else:
                print("Please create an account or log in first.")
        elif choice == "3":
            add_book(book_list)
        elif choice == "4":
            if logged_in_user:
                username = logged_in_user.get_username()
                book_title = input("Enter the title of the book you want to borrow: ")
                matching_books = book_list.search_book("title", book_title)
                if matching_books:
                    print("\nMatching Books:")
                    for i, book in enumerate(matching_books):
                        print(f"{i + 1}. {book.get_title()} by {book.get_author()}")
                    
                    loan_choice = input("Do you want to borrow a book (yes/no)? ").lower()
                    if loan_choice == "yes":
                        book_choice = int(input("Enter the number of the book you want to borrow: ")) - 1
                        if 0 <= book_choice < len(matching_books):
                            borrow_book(logged_in_user, matching_books[book_choice], loans)
                        else:
                            print("Invalid choice.")
                else:
                    print(f"No books found with title '{book_title}'.")
            else:
                print("Please create an account or log in first.")
        elif choice == "5":
            print("Exiting the library. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4/5).")

if __name__ == "__main__":
    main()

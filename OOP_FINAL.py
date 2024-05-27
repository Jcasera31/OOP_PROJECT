import random
from abc import ABC, abstractmethod

class Book(ABC): #base class for books 
    def __init__(self, title, author, publication_year, genre):
        self.__title = title
        self.__author = author
        self.__publication_year = publication_year
        self.__genre = genre
        self.__available = True

    @abstractmethod
    def borrow(self): #abstract menthod for borrow
        if self.__available:
            self.__available = False
            return True
        else:
            print("This book is not available.")
            return False

    @abstractmethod
    def return_book(self): #abstract menthod for return
        self.__available = True

    def get_title(self):#method for get a book
        return self.__title

    def is_available(self):#method if the books is available
        return self.__available

class FictionBook(Book):#representing fiction books and inherets from Book class
    def __init__(self, title, author, publication_year, genre):# Constructor method
        super().__init__(title, author, publication_year, genre)# Calling parent class constructor

    def borrow(self):# Method to borrow a fiction book
        return super().borrow()

    def return_book(self):# Method to return a fiction book
        super().return_book()

class NonFictionBook(Book):#representing non-fiction books and inherets from Book class
    def __init__(self, title, author, publication_year, genre):# Constructor method
        super().__init__(title, author, publication_year, genre)# Calling parent class constructor

    def borrow(self):# Method to borrow a non-fiction book
        return super().borrow()

    def return_book(self):# Method to return a non-fiction book
        super().return_book()

class LibraryMember: #class for library member
    def __init__(self, name, member_id):
        self.__name = name
        self.__member_id = member_id
        self.__borrowed_books = []

    def borrow(self, book):# Method to borrow a book by a member
        if book.borrow():
            self.__borrowed_books.append(book)
            print(f"{self.__name} has borrowed '{book.get_title()}'")
        else:
            print(f"Sorry, '{book.get_title()}' is not available.")

    def return_book(self, book_title):#method to return a book by a member
        for book in self.__borrowed_books:
            if book.get_title().lower() == book_title.lower():
                book.return_book()
                self.__borrowed_books.remove(book)
                print(f"{self.__name} has successfully returned '{book.get_title()}'.")
                return
        print(f"Sorry, '{self.__name}' has not borrowed '{book_title}' or it is not a valid book title.")

class Library:
    def __init__(self):
        self.__books = []#list of books in library

    def add_book(self, book):#method for adding books in a library
        self.__books.append(book)

    def display_books(self):
        for book in self.__books:#method if the book is available or not
            if book.is_available():
                print(f"Title: {book.get_title()}, Available: YES")
            else:
                print(f"Title: {book.get_title()}, Available: NO")

    def get_book_by_title(self, title):#get method for borrwing or returning books
        for book in self.__books:
            if book.get_title().lower() == title.lower() and book.is_available():
                return book
        return None

library = Library()#creating library object

fiction_book = FictionBook("Harry Potter", "J.K. Rowling", 1997, "Fantasy")
fiction_book1 = FictionBook("The Chronicles of Narnia", "C.S. Lewis,", 1950, "Fantasy")
fiction_book2 = FictionBook("Percy Jackson & the Olympians", "Rick Riordan", 2005, "Fantasy")
nonfiction_book = NonFictionBook("Sapiens", "Yuval Noah Harari", 2011, "History")
nonfiction_book1 = NonFictionBook("Harry Potter and History", " Nancy R. Reagin", 2011, "History")
nonfiction_book2 = NonFictionBook("J.K. Rowling: A Biography", "Sean Smith", 2002, "Biography")

library.add_book(fiction_book)#adding the fiction book for library
library.add_book(fiction_book1)
library.add_book(fiction_book2)
library.add_book(nonfiction_book)#addinig the non-fiction book for library
library.add_book(nonfiction_book1)
library.add_book(nonfiction_book2)

user_name = input("Enter your Name: ")#getting user's name
ID_no = "A" + str(random.randint(100, 999))#creating a user's ID

new_user = LibraryMember(user_name, ID_no)# Creating a LibraryMember object

print(f"Hello {user_name}! \nYour member ID is {ID_no}")# Printing user's name and member ID

print("List of available Books")#printing list of all books in the library
library.display_books()

while True:#loop for user iteration
    action = input("Enter '1' to borrow a book, '2' to return a book, or '3' to exit: ")#prompt for user action
    
    if action == "1":#if user wants to borrow book
        select_book_title = input("Enter the title of the book you want to borrow: ")
        selected_book = library.get_book_by_title(select_book_title)
        
        if selected_book:
            new_user.borrow(selected_book)#borrowing the book
        else:
            print("The book you selected is not available or does not exist.")
    
    elif action == "2":
        if new_user._LibraryMember__borrowed_books:  # Accessing private attribute
            return_books_title = input("Enter the title of the book you want to return: ")
            new_user.return_book(return_books_title)  # Modified to pass book title
        else:
            print("You have not borrowed any books.")
    
    elif action == "3":# if the user wants to exit
        print("Exiting...")
        break
    
    else:
        print("Invalid input! Please try again.")

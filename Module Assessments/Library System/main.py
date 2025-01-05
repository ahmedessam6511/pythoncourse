class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"The book '{self.title}' by {self.author} has been checked out.")
        else:
            print(f"Sorry, the book '{self.title}' by {self.author} is already checked out.")

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"The book '{self.title}' by {self.author} has been returned.")
        else:
            print(f"The book '{self.title}' by {self.author} was not checked out.")

    def __str__(self):
        status = "Available" if not self.is_checked_out else "Checked Out"
        return f"'{self.title}' by {self.author} - {status}"


class LibraryCatalogue:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"The book '{book.title}' by {book.author} has been added to the catalogue.")

    def list_books(self):
        if not self.books:
            print("The catalogue is empty.")
        else:
            for book in self.books:
                print(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title):
        book = self.find_book(title)
        if book:
            book.check_out()
        else:
            print(f"The book '{title}' is not in the catalogue.")

    def return_book(self, title):
        book = self.find_book(title)
        if book:
            book.return_book()
        else:
            print(f"The book '{title}' is not in the catalogue.")


library = LibraryCatalogue()

library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

print("\nListing all books in the catalogue:")
library.list_books()

print("\nChecking out '1984':")
library.check_out_book("1984")

print("\nTrying to check out '1984' again:")
library.check_out_book("1984")

print("\nReturning '1984':")
library.return_book("1984")

print("\nListing all books after returning '1984':")
library.list_books()
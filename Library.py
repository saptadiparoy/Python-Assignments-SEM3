#Creating class for Book

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Yes" if self.available else "No"
        print(f"Title    :   {self.title}")
        print(f"Author    :   {self.author}")
        print(f"Available    :   {status}")

#Creating class for Patron
class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed = []

    def display(self):
        print(f"Name    :   {self.name}")
        if self.borrowed:
            print("Borrowed Books:")
            for book in self.borrowed:
                print(f" - {book.title} by {book.author}")

        else:
            print("No borrowed books.")


#actual library
class Library(Book, Patron):  #inherits from book and patron
    def  __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' by {author} added to the library.")

    def register_patron(self, name):
        patron = Patron(name)
        self.patrons.append(patron)
        print(f"Patron '{name}' registered in the library.")

    def borrow_book(self, patron_name, book_title):
        patron = next((p for p in self.patrons if p.name == patron_name), None)
        book = next((b for b in self.books if b.title == book_title), None)

        if patron and book:
            if book.available:
                book.available = False
                patron.borrowed.append(book)
                print(f"Patron '{patron_name}' borrowed the book '{book_title}'.")
            else:
                print(f"Book '{book_title}' is not available for borrowing.")
        else:
            if not patron:
                print(f"Patron '{patron_name}' is not registered in the library.")
            if not book:
                print(f"Book '{book_title}' is not found in the library.")

    def return_book(self, patron_name, book_title):
        patron = next((p for p in self.patrons if p.name == patron_name), None)

        if patron:
            for book in patron.borrowed:
                if book.title == book_title:
                    book.available = True
                    patron.borrowed.remove(book)
                    print(f"Patron '{patron_name}' returned the book '{book_title}'.")

        else:
            print(f"Book not borrowed by patron.")

    def display_books(self):
        print("Books in the Library:")
        for book in self.books:
            book.display()
            print()

    def display_patrons(self):
        print("Registered Patrons:")
        for patron in self.patrons:
            patron.display()
            print()


if  __name__ == "__main__":
    library = Library()

    # Adding books to the library
    library.add_book("smth", "someone")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("1984", "George Orwell")

    # Registering patrons
    library.register_patron("xyz")
    library.register_patron("abc")

    # Displaying books and patrons
    library.display_books()
    library.display_patrons()

    # Borrowing and returning books
    library.borrow_book("xyz", "1984")
    library.borrow_book("abc", "smth")
    library.return_book("xyz", "1984")

    # Displaying updated books and patrons
    library.display_books()
    library.display_patrons()

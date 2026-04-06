# Class Book is a template for books
class Book:
    count = 0

   # Constructor to instantiate the values of attributes of the book object
    def __init__(self, book_title , book_author , book_price):
        self.title = book_title
        self.author = book_author
        self.price = book_price
        self.is_borrowed = False
        Book.count += 1

   # A dunder method which prints details of book with just simple statement : print(book1)
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return (f"Book          : {self.title}\n"
                f"Author        : {self.author}\n"
                f"Price         : ${self.price}\n"
                f"Borrow Status : {status}")

   # Borrow Functionality for a book
    def borrow(self):
        if self.is_borrowed:
            print(f"❌ Sorry, '{self.title}' is already borrowed!")
        else:
            self.is_borrowed = True
            print(f"✅ '{self.title}' borrowed successfully!")

    # Return Functionality for a book
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"✅ '{self.title}' has been returned successfully.")
        else:
            print(f"❌ '{self.title}' was not borrowed in the first place.")


# Creation of objects , The only books I ever read 😅
book1 = Book("Atomic Habits" , "James Clear" , 29.9)
book2 = Book("Think & Grow Rich " , "Napoleon Hill" , 39.9)


# Use of methods
print(book1)
book1.borrow()
book1.return_book()
print(book1)



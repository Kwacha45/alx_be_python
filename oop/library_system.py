class Book:

  def __init__(self, title, author):

    self.title = title
    self.author = author

class EBook(Book):

  def __init__(self, title, author, file_size):

    super().__init__(title, author)  # Call base class constructor
    self.file_size = file_size

class PrintBook(Book):

  def __init__(self, title, author, page_count):

    super().__init__(title, author)  # Call base class constructor
    self.page_count = page_count

class Library:
  def __init__(self):
    self.books = []

  def add_book(self, book):
    if isinstance(book, Book):  # Check if book object inherits from Book
      self.books.append(book)
    else:
      print("Invalid book type. Only Book, EBook, or PrintBook instances allowed.")

  def list_books(self):
    if not self.books:
      print("No books in the library.")
      return

    for book in self.books:
      print(f"- {book.title} by {book.author}")
      if isinstance(book, EBook):
        print(f"  File size: {book.file_size} MB")
      elif isinstance(book, PrintBook):
        print(f"  Page count: {book.page_count}")
      print()  # Add a new line between book details
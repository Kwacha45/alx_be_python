class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  def __str__(self):
    return f"{self.title} by {self.author}"

class EBook(Book):
  def __init__(self, title, author, file_size_kb):
    super().__init__(title, author)  # Call base class constructor
    self.file_size_kb = file_size_kb

  def __str__(self):
    return f"{super().__str__()} (EBook, {self.file_size_kb} KB)"

class PrintBook(Book):
  def __init__(self, title, author, page_count):
    super().__init__(title, author)  # Call base class constructor
    self.page_count = page_count

  def __str__(self):
    return f"{super().__str__()} (PrintBook, {self.page_count} pages)"

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
      print(book)  # Use __str__ method for book details
      print()  # Add a new line between book details
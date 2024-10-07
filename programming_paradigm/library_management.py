class Book:
  """
  Represents a book with title, author, and availability status.
  """
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self._is_checked_out = False  # Private attribute for availability

  def check_out(self):
    """Marks the book as checked out (unavailable)."""
    self._is_checked_out = True

  def return_book(self):
    """Marks the book as returned (available)."""
    self._is_checked_out = False

  def is_available(self):
    """Returns True if the book is available, False otherwise."""
    return not self._is_checked_out

class Library:
  """
  Represents a library with a collection of books.
  """
  def __init__(self):
    self._books = []  # Private list to store Book instances

  def add_book(self, book):
    """Adds a new book to the library collection."""
    self._books.append(book)

  def check_out_book(self, title):
    """Attempts to check out a book by title, marking it unavailable."""
    for book in self._books:
      if book.title == title and book.is_available():
        book.check_out()
        print(f"Successfully checked out '{title}'.")
        return
    print(f"Sorry, '{title}' is not available for checkout.")

  def return_book(self, title):
    """Attempts to return a book by title, marking it available."""
    for book in self._books:
      if book.title == title:
        book.return_book()
        print(f"Successfully returned '{title}'.")
        return
    print(f"Sorry, '{title}' is not currently checked out.")

  def list_available_books(self):
    """Prints a list of titles for all available books."""
    print("Available books:")
    for book in self._books:
      if book.is_available():
        print(f"- {book.title} by {book.author}")

# Keep this block for testing purposes
if __name__ == "__main__":
  main()
class Book:
  def __init__(self, title, author, year):
    self.title = title
    self.author = author
    self.year = year

  def __del__(self):
    print(f"Deleting '{self.title}'")

  def __str__(self):
    return f"{self.title} by {self.author}, published in {self.year}"

  def __repr__(self):
    return f"Book('{self.title}', '{self.author}', {self.year})"

# Example usage (optional)
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)
print(book1)  # Output: The Hitchhiker's Guide to the Galaxy by Douglas Adams, published in 1979

# Simulate deletion (won't actually be called explicitly in most cases)
del book1  # Output: Deleting 'The Hitchhiker's Guide to the Galaxy'
class Library:
  def __init__(self, name):
    self.name = name
    self.books = []

  def add_book(self, book):
    self.books.append(book)

  def list_books(self):
    for i, book in enumerate(self.books, start=1):
      print(f"Book {i}: {book.title}, by: {book.author}")

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

class Audiobook:
  def __init__(self, title, author, lector):
    self.title = title
    self.author = author
    self.lector = lector

library = Library("Wrocławska Biblioteka")

books = [
  Book("Wieża jaskółki", "Andrzej Sapkowski"),
  Book("Pan Lodowego Ogrodu, tom 1", "Jarosław Grzędowicz"),
  Book("Wieża jaskółki", "Andrzej Sapkowski"),
  Book("Pan Lodowego Ogrodu, tom 1", "Jarosław Grzędowicz"),
  Audiobook("Nawyki warte miliony", "Brian Tracy", "Krystyna Czubówna")
]

for book in books:
  library.add_book(book)

library.list_books()
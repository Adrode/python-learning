class Book:
  total_books = 0

  def __init__(self, title, author):
    self.title = title
    self.author = author
    Book.total_books += 1

  def show_info(self):
    return f"Title: {self.title}, by {self.author}"

  @classmethod
  def from_string(cls, book_info):
    title, author = book_info.split(" - ")
    return cls(title, author)
  
  @classmethod
  def number_of_books(cls):
    return f"Total number of books: {cls.total_books}"

book1 = Book.from_string("Ostatnie Życzenie - Andrzej Sapkowski")
book2 = Book.from_string("Pan Lodowego Ogrodu - Jarosław Grzędowicz")
book3 = Book("Miecz Przeznaczenia", "Andrzej Sapkowski")

print(Book.number_of_books())
print(book1.show_info())
print(book2.show_info())
print(book3.show_info())

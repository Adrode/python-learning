class Author:
  def __init__(self, name):
    self.name = name

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

class Library:
  def __init__(self):
    self.books = []

  def add_book(self, book):
    self.books.append(book)

  def list_books(self):
    for book in self.books:
      print(f"Title: {book.title}, by {book.author.name}")

author1 = Author("Andrzej Sapkowski")
author2 = Author("Jarosław Grzędowicz")

book1 = Book("Ostatnie Życzenie", author1)
book2 = Book("Pani Jeziora", author1)
book3 = Book("Pan Lodowego Ogrodu, tom 3", author2)

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.list_books()
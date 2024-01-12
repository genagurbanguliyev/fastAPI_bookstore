from fastapi import FastAPI

from helpers.set_book_id import set_id
from propTypes.book.i_book import IBook

from propTypes.book.class_book import Book

app = FastAPI()

bookstore = [
  Book(id='1', title='Python in a Nutshell', author='gena', description='Python in a Nutshell', rating=5),
  Book(id='2', title='Python Cookbook', author='gena', description='Python Cookbook', rating=4),
  Book(id='3', title='Python Cookbook', author='gem', description='Python Cookbook', rating=3),
  Book(id='4', title='Python Cookbook', author='gem', description='Python Cookbook', rating=2),
  Book(id='5', title='Python Cookbook', author='oraz', description='Python Cookbook', rating=1),
]


@app.get('/books')
async def get_books():
    return bookstore


@app.post('/create-book')
async def create_book(book: IBook):
    new_book = Book(**book.model_dump())
    bookstore.append(set_id(book=new_book, last_id=len(bookstore)))


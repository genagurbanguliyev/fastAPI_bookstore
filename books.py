from fastapi import FastAPI, Path, Query, HTTPException
from starlette import status

from helpers.set_book_id import set_id
from propTypes.book.i_book import IBook

from propTypes.book.class_book import Book

app = FastAPI()

bookstore = [
  Book(id=1, title='Python in a Nutshell', author='gena', description='Python in a Nutshell', rating=5, published_date=2024),
  Book(id=2, title='Python Cookbook', author='gena', description='Python Cookbook', rating=4, published_date=2024),
  Book(id=3, title='Python Cookbook', author='gem', description='Python Cookbook', rating=3, published_date=2024),
  Book(id=4, title='Python Cookbook', author='gem', description='Python Cookbook', rating=2, published_date=2024),
  Book(id=5, title='Python Cookbook', author='oraz', description='Python Cookbook', rating=1, published_date=2024),
]


@app.get('/books', status_code=status.HTTP_200_OK)
async def get_books():
    return bookstore


@app.get('/books/{book_id}', status_code=status.HTTP_200_OK)
async def get_book_by_id(book_id: int = Path(gt=0)):
    for book in bookstore:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")


@app.get('/books/', status_code=status.HTTP_200_OK)
async def get_book_by_rate(book_rating: int = Query(gt=0, lt=6)):
    return [book for book in bookstore if book.rating == book_rating]


@app.post('/create-book', status_code=status.HTTP_201_CREATED)
async def create_book(book_request: IBook):
    # print(book_request.model_dump())
    new_book = Book(**book_request.model_dump())
    bookstore.append(set_id(book=new_book, last_id=len(bookstore)))


@app.put('/update-book', status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book_request: IBook):
    changed = False
    for i in range(len(bookstore)):
        if bookstore[i].id == book_request.id:
            bookstore[i] = book_request
            changed = True
            break
    if not changed:
        raise HTTPException(status_code=404, detail="Item not found")


@app.delete('/books/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    changed = False
    for i in range(len(bookstore)):
        if bookstore[i].id == book_id:
            bookstore.pop(i)
            changed = True
            break
    if not changed:
        raise HTTPException(status_code=404, detail="Item not found")

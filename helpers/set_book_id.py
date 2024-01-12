from propTypes.book.class_book import Book


def set_id(book: Book, last_id: int) -> Book:
    book.id = last_id + 1
    return book

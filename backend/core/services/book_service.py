from typing import Dict, List

from core.decorators import api_interface
from core.exceptions import Conflict, NotFound
from db.book_models import Book
from db.db_actions import save_to_db
from logger import get_logger


class BookService:

    def __init__(self):
        self.logger = get_logger()

    @api_interface
    def add_book(self, title: str, author_id: int, category_id: int, book_type_id: int) -> int:
        self.logger.info(f'About to add book: {title=}')
        book = Book(title=title, author_id=author_id, category_id=category_id, book_type_id=book_type_id)
        try:
            save_to_db(book)
        except Conflict:
            raise Conflict(f'{book=} already exists')

        self.logger.info(f'{book=} added! ID={book.id}')
        return book.id

    @api_interface
    def get_book(self, book_id: int) -> Dict:
        self.logger.info(f'About to get book {book_id=}')
        book = Book.query.get(book_id)

        if not book:
            raise NotFound('Book was not found')

        return book.json

    @api_interface
    def get_books(self) -> List[Dict]:
        self.logger.info(f'About to get all books')
        books = Book.query.all()

        return [book.json for book in books]

    @api_interface
    def update_book(self, book_id: int, updated_book: Dict) -> Dict:
        self.logger.info(f'About to update {book_id=}')
        book = Book.query.get(book_id)

        if title := updated_book.get('title'):
            book.title = title
        if category_id := updated_book.get('category_id'):
            book.category_id = category_id
        if author_id := updated_book.get('author_id'):
            book.author_id = author_id
        if book_type := updated_book.get('book_type'):
            book.book_type = book_type

        save_to_db(book)

        return book.json


book_svc = BookService()

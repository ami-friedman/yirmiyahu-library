from typing import Dict, List

from core.decorators import api_interface
from core.exceptions import Conflict, NotFound
from db.book_models import Book
from db.db_actions import save_to_db
from logger import get_logger


class BookService:

    def __init__(self):
        self.logger = get_logger()
        
    def add_book(self, title: str, author_id: int, genre_id: int, book_type_id: int) -> int:
        self.logger.info(f'About to add book: {title=}')
        book = Book(title=title, author_id=author_id, genre_id=genre_id, book_type_id=book_type_id)
        try:
            save_to_db(book)
        except Conflict:
            raise Conflict(f'{book=} already exists')

        self.logger.info(f'{book=} added! ID={book.id}')
        return book.id

    def get_book(self, book_id: int) -> Dict:
        self.logger.info(f'About to get book {book_id=}')
        book = Book.query.get(book_id)

        if not book:
            raise NotFound('Book was not found')

        return book.json

    def get_books(self) -> List[Dict]:
        self.logger.info(f'About to get all books')
        books = Book.query.all()

        return [book.json for book in books]

    def update_book(self, book_id: int, updated_book: Dict) -> Dict:
        self.logger.info(f'About to update {book_id=}')
        book = Book.query.get(book_id)

        if title := updated_book.get('title'):
            book.title = title
        if genre_id := updated_book.get('genre_id'):
            book.genre_id = genre_id
        if author_id := updated_book.get('author_id'):
            book.author_id = author_id
        if book_type := updated_book.get('book_type'):
            book.book_type = book_type

        save_to_db(book)

        return book.json

    def is_book_on_loan(self, book_id: int) -> bool:
        book = Book.query.get(book_id)
        self.logger.info(f'Check if {book=} is on loan')

        if book.loans:
            loan = next((loan for loan in book.loans if loan.return_date is None), None)
            self.logger.info(f'{book=} is on {loan=}')
            return bool(loan)

        return False


book_svc = BookService()

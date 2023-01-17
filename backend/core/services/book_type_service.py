from typing import Dict, List

from core.decorators import api_interface
from core.exceptions import Conflict, NotFound
from db.book_models import BookType
from db.db_actions import save_to_db
from logger import get_logger


class BookTypeService:

    def __init__(self):
        self.logger = get_logger()

    def add_book_type(self, name: str, loan_duration: int) -> int:
        self.logger.info(f'About to add book_type: {name=} {loan_duration=}')
        book_type = BookType(name=name, loan_duration=loan_duration)
        try:
            save_to_db(book_type)
        except Conflict:
            raise Conflict(f'{book_type} already exists')

        self.logger.info(f'{book_type=} added! ID={book_type.id}')
        return book_type.id

    def get_book_type(self, book_type_id: int) -> Dict:
        self.logger.info(f'About to get book_type {book_type_id=}')
        book_type = BookType.query.get(book_type_id)

        if not book_type:
            raise NotFound('BookType was not found')

        return book_type.json

    def get_book_types(self) -> List[Dict]:
        self.logger.info(f'About to get all book_types')
        book_types = BookType.query.all()

        return [book_type.json for book_type in book_types]

    def update_book_type(self, book_type_id: int, updated_book_type: Dict) -> Dict:
        self.logger.info(f'About to update {book_type_id=}')
        book_type = BookType.query.get(book_type_id)

        if name := updated_book_type.get('name'):
            book_type.name = name
        if loan_duration := updated_book_type.get('loan_duration'):
            book_type.loan_duration = loan_duration

        save_to_db(book_type)

        return book_type.json


book_type_svc = BookTypeService()

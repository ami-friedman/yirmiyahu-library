import time
from typing import Dict, Tuple

from core.decorators import api_interface
from core.exceptions import Conflict, NotFound, NotAllowed
from core.utils import human_readable_ts
from db.book_models import Book
from db.db_actions import save_to_db
from db.loan_models import Loan
from logger import get_logger


class LoanService:

    def __init__(self):
        self.logger = get_logger()

    def add_loan(self, book_id: int, sub_id: int) -> int:
        from core.services.book_service import book_svc

        self.logger.info(f'Requested to create a loan: {book_id=} {sub_id=}')

        if book_svc.is_book_on_loan(book_id):
            raise Conflict('book is currently on loan')

        loan = Loan(book_id=book_id, sub_id=sub_id)
        loan.loan_date, loan.due_date = self._calculate_loan_and_due_date(book_id)

        try:
            save_to_db(loan)
        except Conflict:
            raise Conflict(f'{loan} already exists')

        self.logger.info(f'{loan=} added! ID={loan.id}')
        return loan.id

    def get_loan(self, loan_id: int) -> Dict:
        self.logger.info(f'About to get loan {loan_id=}')
        loan = Loan.query.get(loan_id)

        if not loan:
            raise NotFound('Loan was not found')

        return loan.json

    def extend_loan(self, loan_id: int):
        loan = Loan.query.get(loan_id)
        self.logger.info(f'Requested to extend {loan=}')

        if loan.book.book_type.extension_duration == 0:
            msg = f'Book {loan.book} from {loan} cannot be extended! extension_duration is 0'
            self.logger.error(msg)
            raise NotAllowed(msg)

        if not loan.original_due_date:
            loan.original_due_date = loan.due_date
        loan.due_date += loan.book.book_type.extension_duration

        save_to_db(loan)

    def _calculate_loan_and_due_date(self, book_id: int) -> Tuple[int, int]:
        book = Book.query.get(book_id)
        self.logger.info(f'Calculating due date for {book=}')

        loan_duration = book.book_type.loan_duration
        now = int(time.time())

        due_date = now + loan_duration

        self.logger.info(f'Due date for {book=} is {human_readable_ts(due_date)}')
        return now, due_date


loan_svc = LoanService()

import os
from typing import Dict

from sqlalchemy import ForeignKey

from db.db_config import db
from logger import get_logger

logger = get_logger()


class Loan(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    loan_date = db.Column(db.Integer, nullable=False)
    due_date = db.Column(db.Integer, nullable=False)
    original_due_date = db.Column(db.Integer, nullable=True)
    return_date = db.Column(db.Integer)
    book_id = db.Column(db.Integer, ForeignKey('book.id', use_alter=True), nullable=False)
    sub_id = db.Column(db.Integer, ForeignKey('subscriber.id'), nullable=False)
    num_extensions = db.Column(db.Integer, default=0)

    @property
    def json(self) -> Dict:
        return {
            'id': self.id,
            'loan_date': self.loan_date,
            'due_date': self.due_date,
            'original_due_date': self.original_due_date,
            'book_id': self.book_id,
            'return_date': self.return_date,
            'sub_id': self.sub_id,
            'allow_extend': self._allow_extend,
        }

    @property
    def _allow_extend(self) -> bool:
        if self.num_extensions >= os.environ.get('NUM_EXTENSIONS'):
            return False

        return True

    def __repr__(self) -> str:
        return f'<Loan {self.id}>: Subscriber ID {self.sub_id}'


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reserve_date = db.Column(db.Integer, nullable=False)
    reserve_expiry_date = db.Column(db.Integer, nullable=False)
    book_id = db.Column(db.Integer, ForeignKey('book.id', use_alter=True), nullable=False)
    sub_id = db.Column(db.Integer, ForeignKey('subscriber.id'), nullable=False)

    @property
    def json(self) -> Dict:
        return {
            'id': self.id,
            'reserve_date': self.reserve_date,
            'reserve_expiry_date': self.reserve_expiry_date,
            'book_id': self.book_id,
            'sub_id': self.sub_id,
        }

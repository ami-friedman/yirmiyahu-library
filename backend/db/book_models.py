from typing import Dict

from sqlalchemy import ForeignKey

from db.db_config import db
from logger import get_logger

logger = get_logger()


class Author(db.Model):
    __table_args__ = (
        db.UniqueConstraint('first_name', 'last_name', name='unique_author'),
    )
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    books = db.relationship('Book', backref=db.backref('author', lazy=True))

    @property
    def json(self) -> Dict:
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'id': self.id,
            'books': self.books
        }

    def __repr__(self):
        return f'<Author {self.first_name} {self.last_name}>'


class Genre(db.Model):
    __table_args__ = (
        db.UniqueConstraint('name', name='unique_genre'),
    )
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    books = db.relationship('Book', backref=db.backref('genre', lazy=True))

    @property
    def json(self) -> Dict:
        return {
            'id': self.id,
            'name': self.name,
        }


class BookType(db.Model):
    __table_args__ = (
        db.UniqueConstraint('name', 'loan_duration', name='unique_type'),
    )
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    loan_duration = db.Column(db.Integer, nullable=False)
    extension_duration = db.Column(db.Integer, nullable=False)
    books = db.relationship('Book', backref=db.backref('book_type', lazy=True))

    @property
    def json(self) -> Dict:
        return {
            'id': self.id,
            'name': self.name,
            'loan_duration': self.loan_duration,
            'extension_duration': self.extension_duration,
        }


class Book(db.Model):
    __table_args__ = (
        db.UniqueConstraint('title', 'author_id', name='unique_type'),
    )
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, ForeignKey('author.id'), nullable=False)
    genre_id = db.Column(db.Integer, ForeignKey('genre.id'), nullable=False)
    book_type_id = db.Column(db.Integer, ForeignKey('book_type.id'), nullable=False)
    loans = db.relationship('Loan', backref=db.backref('book', lazy=True))
    reservations = db.relationship('Reservation', backref=db.backref('book', lazy=True))

    def __repr__(self):
        return f'<Book {self.title}>'

    @property
    def json(self) -> Dict:
        return {
            'id': self.id,
            'title': self.title,
            'author_id': self.author_id,
            'author': self.author.json,
            'genre': self.genre.json if self.genre else None,
            'book_type': self.book_type.json if self.book_type else None,
        }

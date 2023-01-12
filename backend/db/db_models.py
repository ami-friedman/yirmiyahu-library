import os
from typing import Dict

import sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy_utils import database_exists, create_database

from core.enums import Role
from core.exceptions import Conflict
from logger import get_logger

flask_app = Flask(__name__)

if os.environ.get('DEV_RUN'):
    DATABASE_URI = os.environ.get('DEV_DB_URI')
else:
    DATABASE_URI = os.environ.get('PROD_DB_URI')

if not DATABASE_URI:
    raise Exception('DB_URI environment variable is required for running this app')

flask_app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
flask_app.config['SQLALCHEMY_POOL_RECYCLE'] = 60


db = SQLAlchemy(flask_app)
logger = get_logger()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    role = db.Column(db.Enum(Role, values_callable=lambda role_enum: [r.value for r in role_enum]), nullable=False)

    @property
    def json(self) -> Dict:
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role.value,
        }


class Author(db.Model):
    __table_args__ = (
        db.UniqueConstraint('first_name', 'last_name', name='unique_author'),
    )
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    # books = db.relationship('Book', backref=db.backref('author', lazy=True), cascade="all,delete")

    def to_dict(self) -> Dict:
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'id': self.id,
            # 'books': self.books
        }

    def __repr__(self):
        return f'<Author {self.first_name} {self.last_name}>'


def db_commit():
    try:
        db.session.commit()
    except sqlalchemy.exc.IntegrityError as _:
        logger.error('Some/all records already exists')
        raise Conflict
    except Exception as exc:
        logger.error(f'something went wrong during adding of record: {exc}')
        db.session.rollback()
        raise


def save_to_db(record: db.Model):
    db.session.add(record)
    db_commit()


if __name__ == '__main__':
    if not database_exists(DATABASE_URI):
        create_database(DATABASE_URI)
    db.create_all()

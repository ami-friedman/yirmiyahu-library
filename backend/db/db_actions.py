import sqlalchemy
from sqlalchemy_utils import database_exists, create_database

from core.exceptions import Conflict
from db.db_config import db, DATABASE_URI, flask_app
from logger import get_logger

# These imports are required for create_all()
from db.book_models import Author, Category, Book, BookType
from db.user_models import User

logger = get_logger()


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


def delete_from_db(query_res):
    query_res.delete()
    db_commit()


if __name__ == '__main__':
    db.init_app(flask_app)
    if not database_exists(DATABASE_URI):
        create_database(DATABASE_URI)
    db.create_all()

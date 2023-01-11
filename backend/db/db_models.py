import os
from typing import Dict

import sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

from core.enums import Role
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


def db_commit():
    try:
        db.session.commit()
    except sqlalchemy.exc.IntegrityError as _:
        logger.error('Some/all records already exists')
        raise
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

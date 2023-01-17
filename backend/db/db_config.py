import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
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
flask_app.config['SECRET_KEY'] = 'secret-key-goes-here'


db = SQLAlchemy(flask_app)
logger = get_logger()

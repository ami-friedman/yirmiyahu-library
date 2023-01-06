from typing import Dict

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

flask_app = Flask(__name__)

db = SQLAlchemy(flask_app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)

    @property
    def json(self) -> Dict:
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
        }
from typing import Dict

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from core.enums import Role

flask_app = Flask(__name__)

db = SQLAlchemy(flask_app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    last_valid_token = db.Column(db.String(80), nullable=False)
    role = db.Column(db.Enum(Role, values_callable=lambda role_enum: [r.value for r in role_enum]), nullable=False)

    @property
    def json(self) -> Dict:
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role.value,
        }

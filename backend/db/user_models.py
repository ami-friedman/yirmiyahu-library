from typing import Dict

from core.enums import Role
from db.db_config import db


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

import os
from typing import Dict

from google.auth.transport import requests
from google.oauth2 import id_token

from core.decorators import api_interface
from core.enums import Role
from db.db_models import User, save_to_db
from core.exceptions import Unauthorized
from logger import get_logger

logger = get_logger()


class UserService:

    def __init__(self):
        self.client_id = os.getenv('GOOGLE_CLIENT_ID')
        if not self.client_id:
            raise Exception('GOOGLE_CLIENT_ID not set! Cannot authenticate with app')
        self.admins = os.getenv('ADMINS').split(',')

    @api_interface
    def login(self, token: str) -> Dict:
        try:
            user_info = id_token.verify_oauth2_token(token, requests.Request(), self.client_id)
            return self.register_or_validate_user(user_info)
        except ValueError:
            msg = f'Bad user {token=}'
            logger.error(msg)
            raise Unauthorized(msg)

    def register_or_validate_user(self, user_info: Dict) -> Dict:
        email = user_info.get('email')
        user = User.query.filter_by(email=email).first()
        if not user:
            role = self.determine_role(email)
            user = User(name=user_info.get('name'),
                        email=email,
                        role=role)
            save_to_db(user)
        return user.json

    def determine_role(self, email: str) -> Role:
        if email in self.admins:
            return Role.ADMIN

        return Role.SUBSCRIBER


user_svc = UserService()

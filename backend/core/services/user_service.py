import os
from typing import Dict

from flask_login import login_user
from google.auth.transport import requests
from google.oauth2 import id_token

from core.decorators import api_interface
from core.enums import Role
from core.exceptions import Unauthorized
from db.db_actions import save_to_db
from db.user_models import User
from logger import get_logger
from login_manager import login_manager

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
            # user_info = id_token.verify_oauth2_token(token, requests.Request(), self.client_id)
            user_info = {'name': 'Amichai Friedman', 'email': 'amishosh@gmail.com'}
            user = self.register_or_validate_user(user_info)
            login_user(user)
            return user.json
        except ValueError:
            msg = f'Bad user {token=}'
            logger.error(msg)
            raise Unauthorized(msg)

    def register_or_validate_user(self, user_info: Dict) -> User:
        email = user_info.get('email')
        user = User.query.filter_by(email=email).first()
        if not user:
            role = self.determine_role(email)
            user = User(name=user_info.get('name'),
                        email=email,
                        role=role)
            save_to_db(user)

        return user

    def determine_role(self, email: str) -> Role:
        if email in self.admins:
            return Role.ADMIN

        return Role.SUBSCRIBER

    @staticmethod
    @login_manager.unauthorized_handler
    @api_interface
    def unauthorized():
        raise Unauthorized

    @staticmethod
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


user_svc = UserService()

from flask import request
from flask_restx import Namespace, Resource, fields

from core.enums import Role
from db.db_models import User
from responses import OK

user_api = Namespace('user', description='User management')

user_login_model = user_api.model(
    name='User login',
    model={
        'token': fields.String(required=True, description="User's token from gmail")})


class UserLogin(Resource):
    @user_api.expect(user_login_model, validate=True)
    def post(self):
        token = request.json.get('token')

        user = User(id=1, name='Amichai Friedman', email='amishosh@gmail.com', last_valid_token='@dsdklj122', role=Role.ADMIN)

        res = OK(data=user.json)

        return res.get_as_json(), res.status_code


user_api.add_resource(UserLogin, '/login')


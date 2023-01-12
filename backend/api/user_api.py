from flask import request
from flask_restx import Namespace, Resource, fields

from core.services.user_service import user_svc


user_api = Namespace('users', description='User management')

user_login_model = user_api.model(
    name='User login',
    model={
        'token': fields.String(required=True, description="User's token from gmail")})


class UserLogin(Resource):
    @user_api.expect(user_login_model, validate=True)
    def post(self):
        token = request.json.get('token')

        res = user_svc.login(token)

        return res.get_as_json(), res.status_code


user_api.add_resource(UserLogin, '/login')


from flask import request
from flask_restx import Namespace, Resource, fields

from core.services.author_service import author_svc
from core.services.user_service import user_svc


author_api = Namespace('authors', description='Author management')

add_author_model = author_api.model(
    name='Add Author',
    model={
        'first_name': fields.String(required=True, description="Author's first name"),
        'last_name': fields.String(required=True, description="Author's last name"),
    })


class Author(Resource):
    @author_api.expect(add_author_model, validate=True)
    def post(self):
        first_name = request.json.get('first_name')
        last_name = request.json.get('last_name')

        res = author_svc.add_author(first_name, last_name)

        return res.get_as_json(), res.status_code


author_api.add_resource(Author, '')


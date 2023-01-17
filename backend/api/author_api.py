from flask import request
from flask_login import login_required
from flask_restx import Namespace, Resource, fields

from core.decorators import api_interface
from core.services.author_service import author_svc


author_api = Namespace('authors', description='Author management')

add_author_model = author_api.model(
    name='Add Author',
    model={
        'first_name': fields.String(required=True, description="Author's first name"),
        'last_name': fields.String(required=True, description="Author's last name"),
    })

update_author_model = author_api.model(
    name='Update Author',
    model={
        'updated_author': fields.Raw(required=True, description="Updated Author's info"),
    })

author_id_doc = {'author_id': 'Author ID'}


class Authors(Resource):
    @author_api.expect(add_author_model, validate=True)
    @login_required
    @api_interface
    def post(self):
        first_name = request.json.get('first_name')
        last_name = request.json.get('last_name')

        return author_svc.add_author(first_name, last_name)

    @login_required
    @api_interface
    def get(self):
        return author_svc.get_authors()


class Author(Resource):
    @author_api.doc(author_id_doc)
    @login_required
    @api_interface
    def get(self, author_id: int):
        return author_svc.get_author(author_id)

    @author_api.doc(author_id_doc)
    @author_api.expect(update_author_model, validate=True)
    @login_required
    @api_interface
    def put(self, author_id: int):
        updated_author = request.json.get('updated_author')
        return author_svc.update_author(author_id, updated_author)


author_api.add_resource(Authors, '')
author_api.add_resource(Author, '/<int:author_id>')


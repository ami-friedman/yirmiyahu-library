from flask import request
from flask_login import login_required
from flask_restx import Namespace, Resource, fields

from core.decorators import api_interface
from core.services.book_type_service import book_type_svc


book_type_api = Namespace('book_types', description='BookType management')

add_book_type_model = book_type_api.model(
    name='Add BookType',
    model={
        'name': fields.String(required=True, description="BookType's name"),
        'loan_duration': fields.Integer(required=True, description="BookType's loan duration in seconds"),
    })

update_book_type_model = book_type_api.model(
    name='Update BookType',
    model={
        'updated_book_type': fields.Raw(required=True, description="Updated BookType's info"),
    })

book_type_id_doc = {'book_type_id': 'BookType ID'}


class BookTypes(Resource):
    @book_type_api.expect(add_book_type_model, validate=True)
    @login_required
    @api_interface
    def post(self):
        name = request.json.get('name')
        loan_duration = request.json.get('loan_duration')

        return book_type_svc.add_book_type(name, loan_duration)

    @login_required
    @api_interface
    def get(self):
        return book_type_svc.get_book_types()


class BookType(Resource):
    @book_type_api.doc(book_type_id_doc)
    @login_required
    @api_interface
    def get(self, book_type_id: int):
        return book_type_svc.get_book_type(book_type_id)

    @book_type_api.doc(book_type_id_doc)
    @book_type_api.expect(update_book_type_model, validate=True)
    @login_required
    @api_interface
    def put(self, book_type_id: int):
        updated_book_type = request.json.get('updated_book_type')
        return book_type_svc.update_book_type(book_type_id, updated_book_type)


book_type_api.add_resource(BookTypes, '')
book_type_api.add_resource(BookType, '/<int:book_type_id>')


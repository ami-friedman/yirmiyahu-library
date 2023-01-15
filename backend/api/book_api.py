from flask import request
from flask_restx import Namespace, Resource, fields

from core.services.book_service import book_svc


book_api = Namespace('books', description='Book management')

add_book_model = book_api.model(
    name='Add Book',
    model={
        'title': fields.String(required=True, description="Book's title"),
        'author_id': fields.Integer(required=True, description="ID of the book author"),
        'category_id': fields.Integer(required=True, description="ID of the book category"),
        'book_type_id': fields.Integer(required=True, description="ID of the book book_type"),
    })

update_book_model = book_api.model(
    name='Update Book',
    model={
        'updated_book': fields.Raw(required=True, description="Updated Book's info"),
    })

book_id_doc = {'book_id': 'Book ID'}


class Books(Resource):
    @book_api.expect(add_book_model, validate=True)
    def post(self):
        author_id = request.json.get('author_id')
        category_id = request.json.get('category_id')
        book_type_id = request.json.get('book_type_id')

        res = book_svc.add_book(author_id, category_id, book_type_id)

        return res.get_as_json(), res.status_code

    def get(self):
        res = book_svc.get_books()

        return res.get_as_json(), res.status_code


class Book(Resource):
    @book_api.doc(book_id_doc)
    def get(self, book_id: int):
        res = book_svc.get_book(book_id)

        return res.get_as_json(), res.status_code

    @book_api.doc(book_id_doc)
    @book_api.expect(update_book_model, validate=True)
    def put(self, book_id: int):
        updated_book = request.json.get('updated_book')
        res = book_svc.update_book(book_id, updated_book)

        return res.get_as_json(), res.status_code


book_api.add_resource(Books, '')
book_api.add_resource(Book, '/<int:book_id>')


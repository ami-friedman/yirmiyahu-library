from flask import request
from flask_login import login_required
from flask_restx import Namespace, Resource, fields

from core.decorators import api_interface
from core.services.book_service import book_svc


book_api = Namespace('books', description='Book management')

add_book_model = book_api.model(
    name='Add Book',
    model={
        'title': fields.String(required=True, description="Book's title"),
        'author_id': fields.Integer(required=True, description="ID of the book author"),
        'genre_id': fields.Integer(required=True, description="ID of the book genre"),
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
    @login_required
    @api_interface
    def post(self):
        author_id = request.json.get('author_id')
        genre_id = request.json.get('genre_id')
        book_type_id = request.json.get('book_type_id')

        return book_svc.add_book(author_id, genre_id, book_type_id)

    @api_interface
    def get(self):
        return book_svc.get_books()


class Book(Resource):
    @book_api.doc(book_id_doc)
    @login_required
    @api_interface
    def get(self, book_id: int):
        return book_svc.get_book(book_id)

    @book_api.doc(book_id_doc)
    @book_api.expect(update_book_model, validate=True)
    @login_required
    @api_interface
    def put(self, book_id: int):
        updated_book = request.json.get('updated_book')
        return book_svc.update_book(book_id, updated_book)


book_api.add_resource(Books, '')
book_api.add_resource(Book, '/<int:book_id>')


from flask import request
from flask_login import login_required
from flask_restx import Namespace, Resource, fields

from core.decorators import api_interface
from core.services.genre_service import genre_svc


genre_api = Namespace('genres', description='Genre management')

add_genre_model = genre_api.model(
    name='Add Genre',
    model={
        'name': fields.String(required=True, description="Genre's name"),
    })

update_genre_model = genre_api.model(
    name='Update Genre',
    model={
        'updated_genre': fields.Raw(required=True, description="Updated Genre's info"),
    })

genre_id_doc = {'genre_id': 'Genre ID'}


class Categories(Resource):
    @genre_api.expect(add_genre_model, validate=True)
    @login_required
    @api_interface
    def post(self):
        name = request.json.get('name')

        return genre_svc.add_genre(name)

    @login_required
    @api_interface
    def get(self):
        return genre_svc.get_genres()


class Genre(Resource):
    @genre_api.doc(genre_id_doc)
    @login_required
    @api_interface
    def get(self, genre_id: int):
        return genre_svc.get_genre(genre_id)

    @genre_api.doc(genre_id_doc)
    @genre_api.expect(update_genre_model, validate=True)
    @login_required
    @api_interface
    def put(self, genre_id: int):
        updated_genre = request.json.get('updated_genre')
        return genre_svc.update_genre(genre_id, updated_genre)


genre_api.add_resource(Categories, '')
genre_api.add_resource(Genre, '/<int:genre_id>')


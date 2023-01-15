from flask import request
from flask_restx import Namespace, Resource, fields

from core.services.category_service import category_svc


category_api = Namespace('categories', description='Category management')

add_category_model = category_api.model(
    name='Add Category',
    model={
        'name': fields.String(required=True, description="Category's name"),
    })

update_category_model = category_api.model(
    name='Update Category',
    model={
        'updated_category': fields.Raw(required=True, description="Updated Category's info"),
    })

category_id_doc = {'category_id': 'Category ID'}


class Categories(Resource):
    @category_api.expect(add_category_model, validate=True)
    def post(self):
        name = request.json.get('name')

        res = category_svc.add_category(name)

        return res.get_as_json(), res.status_code

    def get(self):
        res = category_svc.get_categories()

        return res.get_as_json(), res.status_code


class Category(Resource):
    @category_api.doc(category_id_doc)
    def get(self, category_id: int):
        res = category_svc.get_category(category_id)

        return res.get_as_json(), res.status_code

    @category_api.doc(category_id_doc)
    @category_api.expect(update_category_model, validate=True)
    def put(self, category_id: int):
        updated_category = request.json.get('updated_category')
        res = category_svc.update_category(category_id, updated_category)

        return res.get_as_json(), res.status_code


category_api.add_resource(Categories, '')
category_api.add_resource(Category, '/<int:category_id>')


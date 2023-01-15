from flask import request
from flask_login import login_required
from flask_restx import Namespace, Resource, fields

from core.decorators import api_interface
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
    @login_required
    @api_interface
    def post(self):
        name = request.json.get('name')

        return category_svc.add_category(name)

    @login_required
    @api_interface
    def get(self):
        return category_svc.get_categories()


class Category(Resource):
    @category_api.doc(category_id_doc)
    @login_required
    @api_interface
    def get(self, category_id: int):
        return category_svc.get_category(category_id)

    @category_api.doc(category_id_doc)
    @category_api.expect(update_category_model, validate=True)
    @login_required
    @api_interface
    def put(self, category_id: int):
        updated_category = request.json.get('updated_category')
        return category_svc.update_category(category_id, updated_category)


category_api.add_resource(Categories, '')
category_api.add_resource(Category, '/<int:category_id>')


from flask import request
from flask_restx import Namespace, Resource, fields

from core.services.loan_service import loan_svc


loan_api = Namespace('loans', description='Loan management')

add_loan_model = loan_api.model(
    name='Add Loan',
    model={
        'book_id': fields.Integer(required=True, description='ID of the book to lend'),
        'sub_id': fields.Integer(required=True, description='ID of the subscriber borrowing'),
    })

loan_id_doc = {'loan_id': 'Loan ID'}


class Loans(Resource):
    @loan_api.expect(add_loan_model, validate=True)
    def post(self):
        book_id = request.json.get('book_id')
        sub_id = request.json.get('sub_id')

        res = loan_svc.add_loan(book_id, sub_id)

        return res.get_as_json(), res.status_code


class Loan(Resource):
    @loan_api.doc(loan_id_doc)
    def get(self, loan_id: int):
        res = loan_svc.get_loan(loan_id)

        return res.get_as_json(), res.status_code

    @loan_api.doc(loan_id_doc)
    def put(self, loan_id: int):
        res = loan_svc.extend_loan(loan_id)

        return res.get_as_json(), res.status_code


loan_api.add_resource(Loans, '')
loan_api.add_resource(Loan, '/<int:loan_id>')


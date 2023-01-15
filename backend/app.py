import logging
import os

import requests
from flask import Blueprint
from flask_restx import Api
from flask_cors import CORS

from urllib3.exceptions import InsecureRequestWarning
from waitress import serve

from api.author_api import author_api
from api.book_api import book_api
from api.book_type_api import book_type_api
from api.category_api import category_api
from api.loan_api import loan_api
from api.user_api import user_api
from db.db_config import flask_app, db
from logger import get_logger


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
CORS(flask_app, resources={r'/*': {'origins': '*'}})

blueprint = Blueprint('api', __name__, url_prefix='/api')

app = Api(app=blueprint,
          version='1.0',
          title='yirmiyahu-library',
          description='Yirmiyahu Library Application')

app.add_namespace(user_api)
app.add_namespace(author_api)
app.add_namespace(book_api)
app.add_namespace(category_api)
app.add_namespace(book_type_api)
app.add_namespace(loan_api)

logging.basicConfig(level=logging.NOTSET,
                    format='%(asctime)s : %(levelname)-6s : %(filename)s:%(lineno)s:%(funcName)-30s :: %(message)s')
flask_app.register_blueprint(blueprint)
flask_app.logger = get_logger()

if __name__ == '__main__':
    db.init_app(flask_app)
    if os.environ.get('LOCAL_RUN'):
        flask_app.run(debug=True, port=5000, host='127.0.0.1')
    else:
        serve(flask_app, port=5000, threads=20)

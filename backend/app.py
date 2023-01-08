import logging
import os

import requests
from flask import Blueprint
from flask_restx import Api
from flask_cors import CORS

from urllib3.exceptions import InsecureRequestWarning
from waitress import serve

from api.user.user_api import user_api
from db.db_models import flask_app
from logger import get_logger


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
CORS(flask_app, resources={r'/*': {'origins': '*'}})

blueprint = Blueprint('api', __name__, url_prefix='/api')

app = Api(app=blueprint,
          version='1.0',
          title='yirmiyahu-library',
          description='Yirmiyahu Library Application')

app.add_namespace(user_api)

logging.basicConfig(level=logging.NOTSET,
                    format='%(asctime)s : %(levelname)-6s : %(filename)s:%(lineno)s:%(funcName)-30s :: %(message)s')
flask_app.register_blueprint(blueprint)
flask_app.logger = get_logger()

if __name__ == '__main__':
    if os.environ.get('LOCAL_RUN'):
        flask_app.run(debug=True, port=5000, host='127.0.0.1')
    else:
        serve(flask_app, port=5000, threads=20)

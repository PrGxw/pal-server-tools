from flask import Flask
from flask_cors import CORS
import logging

from src.common.controller_error import ControllerError
from .controllers.controller_utils import ResponseCodes, create_response
from .common.controller_error_handler import base_exception_handler
import os

LOGDIR = os.environ.get("LOG_DIR") or "."
LOGFILENAME= "controller.log"
ENV = "development"
LOGLEVEL = logging.INFO if (ENV == "production") else logging.DEBUG
logging.basicConfig(filename=f"{LOGDIR}/{LOGFILENAME}", encoding='utf-8', level=LOGLEVEL)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
cors = CORS(app)
logging.info("Flask app initialized")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:example@mysql:3306/palworld_server?charset=utf8mb4'

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
from flask_migrate import Migrate
migrate = Migrate(app, db)
from flask_marshmallow import Marshmallow
ma = Marshmallow(app)


app.register_error_handler(Exception, base_exception_handler)
# app.register_error_handler(ControllerError, base_exception_handler)

# the following line is strategically placed here to avoid circular deps.
# controllers' dep tree will depend on db variable. hence the controller imports should
# happen after db var is instantiated
from .controllers.users_controller import pb_users_controller
app.register_blueprint(pb_users_controller)
from .controllers.app_controller import pb_app_controller
app.register_blueprint(pb_app_controller)


# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
# need to import the models here to allow for almbic to detect changes in model files
# import of models needs to be placed after the initialization of db. as models will import db
# variable. if placed before db initialization, will cause dep error.
from .models import *

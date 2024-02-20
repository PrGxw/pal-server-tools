from flask import Blueprint, request, render_template
from ..models import User
from .. import db
from .controller_utils import *

pb_app_controller = Blueprint('app_controller', __name__, url_prefix='/')


@pb_app_controller.get("/login")
def login():
    return render_template("login.html")

from flask import Blueprint, request, render_template
from ..models import User
from .. import db
from .controller_utils import *
from ..common.rcon_manager import broadcast
pb_rcon_controller = Blueprint('rcon_controller', __name__, url_prefix='/rcon')

@pb_rcon_controller.post("/broadcast")
def broadcast():
    broadcast("hello_world")

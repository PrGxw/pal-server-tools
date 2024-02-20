from flask import Blueprint, request, render_template
from ..models import User
from .. import db
from .controller_utils import *

pb_users_controller = Blueprint('users_controller', __name__, url_prefix='/users')

@pb_users_controller.post("/")
def create():
    try:
        body = request.json
        username, password = body["username"], body["password"]
        if (not username or not password): raise Exception("Username or password not present")

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        return {"id": user.id}
    except Exception as err:
        return create_failure_response("USER_CREATE_FAILURE", {"errmsg": str(err)})

@pb_users_controller.post("/auth")
def authenticate():
    try:
        body = request.json
        username, password = body["username"], body["password"]

        user = db.session.execute(db.select(User).filter_by(
            username=username, password=password
        )).scalar_one()

        if (not user): raise Exception(f"Unable to find user for {username}")

        return {"id": user.id, "token": user.authtoken()}
    except Exception as err:
        return create_failure_response("USER_LOGIN_FAILURE", {"errmsg": "Sorry, we're unable to authenticate the user."})

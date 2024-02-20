from .. import db
from .base_model import BaseModel
from ..common import consts

class User(BaseModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128))
    password = db.Column(db.String(128))
    email = db.Column(db.String(128))

    # # relationships
    # topics = db.relationship('Topic', backref='user', lazy=True)
    # topics = db.relationship('Post', backref='user', lazy=True)

    def authtoken(self):
        return consts.TEMPORARY_AUTH_TOKEN

from .. import db
from sqlalchemy_easy_softdelete.mixin import generate_soft_delete_mixin_class
from datetime import datetime

class SoftDeleteMixin(generate_soft_delete_mixin_class()):
    deleted_at: datetime

class BaseModel(db.Model, SoftDeleteMixin):
    # https://stackoverflow.com/questions/22976445/how-do-i-declare-a-base-model-class-in-flask-sqlalchemy
    __abstract__ = True

    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.current_timestamp(),
        server_onupdate=db.func.current_timestamp()
    )
    created_at = db.Column(
        db.DateTime,
        server_default=db.func.current_timestamp(),
        server_onupdate=db.func.current_timestamp()
    )

    def as_dict(self):
       return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

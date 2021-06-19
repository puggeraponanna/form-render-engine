from .database import db
from sqlalchemy.dialects.postgresql import JSON

class JSONFormMaster(db.Model):
    __tablename__ = 'json_form_master'

    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.String())
    file_contents = db.Column(JSON)
    created_on = db.Column(db.DateTime())
    modified_on = db.Column(db.DateTime())

    def __init__(self, module_id, file_contents, created_on, modified_on):
        self.module_id = module_id
        self.file_contents = file_contents
        self.created_on = created_on
        self.modified_on = modified_on

    def __repr__(self):
        return '<id {}>'.format(self.id)
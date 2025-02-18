from database import db
from datetime import date

class Notice(db.Model):
    __table__ = db.Table('notice',db.metadata,autoload_with=db.engine)
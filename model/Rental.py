from database import db
from datetime import datetime

class Rental(db.Model):
    __table__ = db.Table('rental',db.metadata,autoload_with=db.engine) 
from database import db
from datetime import time

class Staff(db.Model):
    __table__ = db.Table('staff',db.metadata,autoload_with=db.engine)
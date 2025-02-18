from database import db

class Payment(db.Model):
    __table__ = db.Table('payment',db.metadata,autoload_with=db.engine)
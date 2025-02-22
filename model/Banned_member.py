from database import db 
from datetime import date

# class Banned_member(db.Model):
#     __table__ = db.Table('banned_member', db.metadata, autoload_with=db.engine)

class Banned_member(db.Model):
    __tablename__ = "banned_members"
    ban_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), primary_key=True)
    reason = db.Column(db.Text, nullable=False)
    ban_date = db.Column(db.Date, nullable=False)
    customer = db.relationship('Customer', backref=db.backref('banned_members', lazy=True))

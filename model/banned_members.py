from database import db 
from datetime import date

class Banned_Members(db.Model):
    __tablename__ = 'banned_members'
    Ban_Id = db.Column(db.Integer, autoincrement = True)
    Customer_Id = db.Column(db.Integer)
    Reason = db.Column(db.Text, nullable = False)
    Ban_Date = db.Column(db.Date, default = date.today)
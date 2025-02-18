from database import db 
from datetime import date

class Banned_members(db.Model):
    __table__ = db.Table('banned_members', db.metadata, autoload_with=db.engine)

# class Banned_Members(db.Model):
#     __tablename__ = 'banned_members'
#     Ban_Id = db.Column(db.Integer, autoincrement = True)
#     Customer_Id = db.Column(db.Integer, db.ForeignKey('customer.Customer_Id'), nullable=False)
#     Reason = db.Column(db.Text, nullable = False)
#     Ban_Date = db.Column(db.Date, default = date.today)
    
#     __table_args__ = (
#         db.PrimaryKeyConstraint('Ban_Id', 'Customer_Id'),
#     )
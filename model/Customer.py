from database import db
from datetime import date  

class Customer(db.Model):
    __tablename__ = "customer"
    Customer_Id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    Customer_Name = db.Column(db.String(255), nullable = False)
    Email = db.Column(db.String(255), nullable = False, unique = True)
    Password = db.Column(db.String(255), nullable = False)
    Phone_Number = db.Column(db.String(20), nullable = False)
    Street_Address = db.Column(db.String(255), nullable = False)
    City = db.Column(db.String(100), nullable = False)
    State = db.Column(db.String(100), nullable = False)
    Zip_Code = db.Column(db.String(20), nullable = False)
    Staff_Id = db.Column(db.Integer, nullable = False)
    Created_Date = db.Column(db.Date, default=date.today)
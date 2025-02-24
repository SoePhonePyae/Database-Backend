from database import db
from datetime import time
from sqlalchemy import Enum

class Staff(db.Model):
    __tablename__ = "staff"
    staff_id = db.Column(db.Integer, primary_key=True)
    staff_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    salary = db.Column(db.Numeric(10, 2), nullable=False)
    street_address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.String(20), nullable=False)
    
    # FIX: Added a name to the ENUM type
    type = db.Column(Enum('Part_Time', 'Full_Time', 'Internship', name="staff_type"), nullable=False)
    
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id'), nullable=False)
    last_action = db.Column(db.TIMESTAMP)
    admin = db.relationship('Admin', backref=db.backref('staffs', lazy=True))

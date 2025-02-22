from database import db
from datetime import date

class Notice(db.Model):
    __tablename__ = "notice"
    notice_id = db.Column(db.Integer, primary_key=True)
    reason = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date, nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id'), nullable=False)
    admin = db.relationship('Admin', backref=db.backref('notices', lazy=True))

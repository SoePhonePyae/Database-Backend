from database import db
from datetime import datetime

class Game_Report(db.Model):
    __tablename__ = "game_reports"
    report_id = db.Column(db.Integer, primary_key=True)
    rental_id = db.Column(db.Integer, db.ForeignKey('rental.rental_id'), nullable=False)
    reason = db.Column(db.Text, nullable=False)
    report_date = db.Column(db.Date, nullable=False)
    detail = db.Column(db.Text, nullable=False)
    attachment = db.Column(db.String(255))
    rental = db.relationship('Rental', backref=db.backref('game_reports', lazy=True))
from database import db
from datetime import datetime

class Rental(db.Model):
    __tablename__ = "rental"
    rental_id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.game_id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    status = db.Column(db.Enum('Pending', 'Renting', 'Returned'), nullable=False)
    rent_date = db.Column(db.Date, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer)
    game = db.relationship('Game', backref=db.backref('rentals', lazy=True))
    customer = db.relationship('Customer', backref=db.backref('rentals', lazy=True))

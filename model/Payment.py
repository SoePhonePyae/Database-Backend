from database import db

class Payment(db.Model):
    __tablename__ = "payment"
    payment_id = db.Column(db.Integer, primary_key=True)
    rental_id = db.Column(db.Integer, db.ForeignKey('rental.rental_id'), primary_key=True)
    proof = db.Column(db.String(255), nullable=False)
    method = db.Column(db.String(50), nullable=False)
    rental = db.relationship('Rental', backref=db.backref('payments', lazy=True))

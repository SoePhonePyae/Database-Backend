from database import db 

# class Game(db.Model):
#     __table__ = db.Table('game', db.metadata, autoload_with=db.engine)
    
class Game(db.Model):
    __tablename__ = "game"
    
    game_id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    platform = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.String(20), nullable=False)
    stock_number = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable = False)
    image_link = db.Column(db.String(255), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.admin_id"), nullable=False)
    last_action = db.Column(db.TIMESTAMP, nullable=True)
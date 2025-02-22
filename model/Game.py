from database import db 

# class Game(db.Model):
#     __table__ = db.Table('game', db.metadata, autoload_with=db.engine)
    
class Game(db.Model):
    __tablename__ = "game"
    game_id = db.Column(db.Integer, primary_key = True)
    admin_name = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(255), nullable = False, unique = True)
    password = db.Column(db.String(255), nullable = False)
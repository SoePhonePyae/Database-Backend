from database import db 

class Game(db.Model):
    __table__ = db.Table('game', db.metadata, autoload_with=db.engine)
    
# class Game(db.Model):
#     __tablename__ = "game"
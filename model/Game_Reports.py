from database import db
from datetime import datetime

class Game_Reports(db.Model):
    __table__ = db.Table('game_reports',db.metadata,autoload_with=db.engine)
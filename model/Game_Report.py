from database import db
from datetime import datetime

class Game_Report(db.Model):
    __table__ = db.Table('game_report',db.metadata,autoload_with=db.engine)
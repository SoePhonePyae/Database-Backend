from database import db

class Admin(db.Model):
    __table__ = db.Table('admin', db.metadata, autoload_with=db.engine)
    
# class Admin(db.Model):
#     __tablename__ = "admin"
#     Admin_Id = db.Column(db.Integer, primary_key = True)
#     Admin_Name = db.Column(db.String(255), nullable = False)
#     Email = db.Column(db.String(255), nullable = False, unique = True)
#     Password = db.Column(db.String(255), nullable = False)
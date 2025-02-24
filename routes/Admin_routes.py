from flask import jsonify
from app import app, db
from model import Admin

@app.route("/admin", methods=["GET"])
def get_admin():
    admin = Admin.query.all()
    return jsonify([{"admin_id" : a.admin_id,
                     "admin_name" : a.admin_name,
                     "email" : a.email,
                     "password" : a.password} for a in admin])
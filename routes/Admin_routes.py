from flask import Flask, request,jsonify
from app import app, db
from model import Admin

@app.route("/admin", methods=["GET"])
def get_admin():
    admin = Admin.query.all()
    return jsonify([{"admin_id" : a.admin_id,
                     "admin_name" : a.admin_name,
                     "email" : a.email,
                     "password" : a.password} for a in admin])

@app.route('/admin/<int:admin_id>', methods=['GET'])
def get_admin_by_id(admin_id):
    admin = Admin.query.get(admin_id)
    if not admin:
        return jsonify({"error": "Admin not found"}), 404
    
    return jsonify({
        "admin_id": admin.admin_id,
        "admin_name": admin.admin_name,
        "email": admin.email,
        "password": admin.password
    })


@app.route('/admin/<string:email>', methods=['GET'])
def auth_admin(email):
    admin = Admin.query.filter_by(email=email).first()
    if not admin:
        return jsonify({"password": "null"}), 404
    else:
        return jsonify({"password": admin.password}), 200
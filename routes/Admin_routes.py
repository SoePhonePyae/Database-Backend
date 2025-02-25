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
    

@app.route('/login/admin', methods=['POST'])
def auth_admin():
    data = request.get_json()
    required_fields = ['email', 'password']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    admin = Admin.query.filter_by(email=data['email']).first()
    if not admin:
        return jsonify({"error": "admin not found"}), 404
    if admin.password != data['password']:
        return jsonify({"error": "Incorrect password"}), 400
    return jsonify({
        "admin_id" : admin.admin_id,
        "admin_name" : admin.admin_name,
        "email" : admin.email
    })
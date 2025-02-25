from flask import jsonify, request
from app import app, db
from model import Staff
from datetime import datetime

@app.route("/staff", methods=['GET'])
def get_staff():
    staff = Staff.query.all()
    return jsonify([{"staff_id" : s.staff_id,
                     "staff_name" : s.staff_name,
                     "email" : s.email,
                     "password" : s.password,
                     "phone_number" : s.phone_number,
                     "salary" : s.salary,
                     "street_address" : s.street_address,
                     "city" : s.city,
                     "state" : s.state,
                     "zip_code" : s.zip_code,
                     "type" : s.type,
                     "admin_id" : s.admin_id,
                     "last_action" : s.last_action} for s in staff])


@app.route("/staff", methods=['POST'])
def create_staff():
    data = request.get_json()
    required_fields = ['staff_name', 'email', 'password', 'phone_number', 'salary', 
                       'street_address', 'city', 'state', 'zip_code', 'type', 'admin_id']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    
    new_staff = Staff(
        staff_name = data["staff_name"],
        email = data["email"],
        password = data['password'],
        phone_number = data['phone_number'],
        salary = data['salary'],
        street_address = data['street_address'],
        city = data['city'],
        state = data['state'],
        zip_code = data['zip_code'],
        type = data['type'],
        admin_id = data['admin_id'],
        last_action = "Added"
    )

    db.session.add(new_staff)
    db.session.commit()
    return jsonify({"message": "Staff added"})
        

@app.route('/staff/<int:report_id>', methods=['GET'])
def get_specific_staff(report_id):
    s = Staff.query.get(report_id)
    if not s:
        return jsonify({"error": "Staff not found"}), 404
    
    return jsonify({
        "staff_id" : s.staff_id,
        "staff_name" : s.staff_name,
        "email" : s.email,
        "password" : s.password,
        "phone_number" : s.phone_number,
        "salary" : s.salary,
        "street_address" : s.street_address,
        "city" : s.city,
        "state" : s.state,
        "zip_code" : s.zip_code,
        "type" : s.type,
        "admin_id" : s.admin_id,
        "last_action" : s.last_action
    })


@app.route('/staff/<int:staff_id>', methods=['PUT'])
def update_staff(staff_id):
    data = request.get_json()
    staff = Staff.query.get(staff_id)
    print("DATA")
    print(data)
    if not staff:
        return jsonify({"error": "staff not found"}), 404

    staff.staff_name = data.get("staff_name", staff.staff_name)
    staff.email = data.get("email", staff.email)
    staff.password = data.get("password", staff.password)
    staff.phone_number = data.get("phone_number", staff.phone_number)
    staff.street_address = data.get("street_address", staff.street_address)
    staff.city = data.get("city", staff.city)
    staff.state = data.get("state", staff.state)
    staff.zip_code = data.get("zip_code", staff.zip_code)
    staff.type = data.get("type", staff.type)
    staff.admin_id = data.get("admin_id", staff.admin_id)
    staff.last_action = "Updated"
    
    db.session.commit()
    return jsonify({"message": "staff updated successfully"})


@app.route('/login/staff', methods=['POST'])
def auth_staff():
    data = request.get_json()
    required_fields = ['email', 'password']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    staff = Staff.query.filter_by(email=data['email']).first()
    if not staff:
        return jsonify({"error": "Staff not found"}), 404
    if staff.password != data['password']:
        return jsonify({"error": "Incorrect password"}), 400
    return jsonify({
        "staff_id": staff.staff_id,
        "staff_name": staff.staff_name,
        "email": staff.email,
        "phone_number": staff.phone_number,
        "salary": staff.salary,
        "street_address": staff.street_address,
        "city": staff.city,
        "state": staff.state,
        "zip_code": staff.zip_code,
        "type": staff.type,
        "admin_id": staff.admin_id
    })
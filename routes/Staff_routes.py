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
def create_game():
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
        street_addess = data['street_address'],
        city = data['city'],
        state = data['state'],
        zip_code = data['zip_code'],
        type = data['type'],
        admin_id = data['admin_id'],
        last_action = datetime.today().strftime('%Y-%m-%d')
    )

    db.session.add(new_staff)
    db.session.commit()
    return jsonify({"message": "Game added"})
        
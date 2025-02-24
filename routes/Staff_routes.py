from flask import jsonify
from app import app, db
from model import Staff

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
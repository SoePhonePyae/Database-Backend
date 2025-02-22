from flask import jsonify
from app import app,db
from model import Customer

@app.route('/customer', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([{"customer_id" : c.customer_id,
                     "customer_name" : c.customer_name,
                     "email" : c.email,
                     "password" : c.password,
                     "phone_number" : c.phone_number,
                     "street_address" : c.street_address,
                     "city" : c.city,
                     "state" : c.state,
                     "zip_code" : c.zip_code,
                     "staff_id" : c.staff_id,
                     "created_date" : c.created_date} 
                     for c in customers])
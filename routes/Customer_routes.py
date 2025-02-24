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

@app.route('/customer/<string:email>/<string:password>', methods=['GET'])
def check_customer_password(email, password):
    """
    A simple endpoint that looks up a customer by email,
    compares the plain-text password, and returns a JSON response.
    """
    # Look up the customer by email
    customer = Customer.query.filter_by(email=email).first()
    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    # Compare the plain-text password (again, not recommended for production)
    if customer.password == password:
        return jsonify({
            "message": "Login successful",
            "customer_id": customer.customer_id,
            "customer_name": customer.customer_name,
            "email": customer.email
        }), 200
    else:
        return jsonify({"error": "Incorrect password"}), 401
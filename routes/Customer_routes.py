from flask import jsonify, request
from app import app,db
from model import Customer
from datetime import datetime

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
    

@app.route('/customer', methods=['POST'])
def create_customer():
    data = request.get_json()
    required_fields = ['customer_name', 'email', 'password', 'phone_number', 
                       'street_address', 'city', 'state', 'zip_code', 'staff_id']
    
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    
    new_customer = Customer(
        customer_name = data['customer_name'],
        email = data['email'],
        password = data['password'],
        phone_number = data['phone_number'],
        street_address = data['street_address'],
        city = data['city'],
        state = data['state'],
        zip_code = data['zip_code'],
        staff_id = data['staff_id'],
        created_date = datetime.now()
    )

    db.session.add(new_customer)
    db.session.commit()

    return jsonify({"message": "New customer added successfully"})


@app.route('/customer/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.get_json()
    customer = Customer.query.get(customer_id)

    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    customer.customer_name = data.get("customer_name", customer.customer_name)
    customer.email = data.get("email", customer.email)
    customer.password = data.get("password", customer.password)
    customer.phone_number = data.get("phone_number", customer.phone_number)
    customer.street_address = data.get("street_address", customer.street_address)
    customer.city = data.get("city", customer.city)
    customer.state = data.get("state", customer.state)
    customer.zip_code = data.get("zip_code", customer.zip_code)
    customer.staff_id = data.get("staff_id", customer.staff_id)
    
    db.session.commit()
    return jsonify({"message": "customer updated successfully"})
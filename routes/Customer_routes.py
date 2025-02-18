from flask import jsonify
from app import app,db
from model import Customer

@app.route('/customer', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([{"customer_id" : c.Customer_Id,
                     "customer_name" : c.Customer_Name,
                     "email" : c.Email,
                     "password" : c.Password,
                     "phone_number" : c.Phone_Number,
                     "street_address" : c.Street_Address,
                     "city" : c.City,
                     "state" : c.State,
                     "zip_code" : c.Zip_Code,
                     "staff_id" : c.Staff_Id,
                     "created_date" : c.Created_Date} 
                     for c in customers])
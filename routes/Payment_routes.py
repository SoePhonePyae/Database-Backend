from flask import Flask,request,jsonify
from app import app,db
from model import Payment

@app.route('/payment', methods = ['GET'])
def get_payments():
    payments = Payment.query.all()
    return jsonify([{
        "payment_id": p.payment_id,
        "rental_id": p.rental_id,
        "proof": p.proof,
        "method": p.method,
    }] for p in payments)

@app.route('/payment/<int:payment_id>', method = ['GET'])
def get_payment(payment_id):
    p = Payment.query.get(payment_id)

    if not p:
        return({"error": "Payment not found"}), 404
    
    return jsonify({
        "payment_id": p.payment_id,
        "rental_id": p.rental_id,
        "proof": p.proof,
        "method": p.method,
    })

@app.route('/payment', method = ['POST'])
def create_payment():
    data = request.get_json()
    required_fields = ["rental_id","proof", "method"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    new_payment = Payment(  
        payment_id = data["payment_id"],
        rental_id = data["rental_id"],
        proof = data["proof"],
        method = data["method"]
    )
    db.session.add(new_payment)
    db.session.commit()
    return jsonify({"message": "payment added"})

@app.route('/payment/<int:payment_id>', method = ['PUT'])
def update_payment(payment_id):
    p = Payment.query.get(payment_id)
    data = request.get_json()

    if not p:
        return jsonify({"error": "payment not found"})
    
    p.rental_id = data.get("rental_id",p.rental_id)
    p.proof = data.get("proof",p.proof)
    p.method = data.get("method",p.method)

    db.session.commit()
    return ({"message": "payment updated successfully"})

@app.route('/payment/<int:payment_id>',method = ['DELETE'])
def delete_payment(payment_id):
    p = Payment.query.get(payment_id)

    if not p:
        return jsonify({"error": "payment not found"})
    
    db.session.delete(p)
    db.session.commit()

    return jsonify({"message": "payment deleted successfully"})
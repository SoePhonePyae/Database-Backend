from flask import Flask, request, jsonify
from app import app, db
from model import Payment

@app.route('/payment', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    return jsonify([{
        "payment_id": p.payment_id,
        "rental_id": p.rental_id,
        "proof": p.proof,
        "method": p.method,
    } for p in payments])

@app.route('/payment/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    p = Payment.query.get(payment_id)

    if not p:
        return jsonify({"error": "Payment not found"}), 404
    
    return jsonify({
        "payment_id": p.payment_id,
        "rental_id": p.rental_id,
        "proof": p.proof,
        "method": p.method,
    })

@app.route('/payment', methods=['POST'])
def create_payment():
    data = request.get_json()
    required_fields = ["rental_id", "proof", "method"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    new_payment = Payment(
        payment_id=data["payment_id"],
        rental_id=data["rental_id"],
        proof=data["proof"],
        method=data["method"]
    )
    db.session.add(new_payment)
    db.session.commit()
    return jsonify({"message": "Payment added"})

@app.route('/payment/<int:payment_id>', methods=['PUT'])
def update_payment(payment_id):
    p = Payment.query.get(payment_id)
    data = request.get_json()

    if not p:
        return jsonify({"error": "Payment not found"}), 404
    
    p.rental_id = data.get("rental_id", p.rental_id)
    p.proof = data.get("proof", p.proof)
    p.method = data.get("method", p.method)

    db.session.commit()
    return jsonify({"message": "Payment updated successfully"})

@app.route('/payment/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    p = Payment.query.get(payment_id)

    if not p:
        return jsonify({"error": "Payment not found"}), 404
    
    db.session.delete(p)
    db.session.commit()

    return jsonify({"message": "Payment deleted successfully"})
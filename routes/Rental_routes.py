from flask import Flask, request, jsonify
from app import app,db
from model import Rental
from datetime import date

@app.routes('/rental', methods = ['GET'])
def get_rentals():
    rentals = Rental.query.all()
    return jsonify([{
        "rental_id": r.rental_id,
        "game_id": r.game_id,
        "customer_id": r.customer_id,
        "status": r.status,
        "rent_date": r.rent_date,
        "due_date": r.due_date,
        "duration": r.duration
    }]for r in rentals)

@app.routes('/rental/<int:rental_id>', methods = ['GET'])
def get_rental(rental_id):
    r = Rental.query.get(rental_id)

    if not r:
        return jsonify({"error": "Rental not found"}) , 404
    
    return jsonify([{
        "rental_id": r.rental_id,
        "game_id": r.game_id,
        "customer_id": r.customer_id,
        "status": r.status,
        "rent_date": r.rent_date,
        "due_date": r.due_date,
        "duration": r.duration
    }])

@app.route('/rental', methods = ['POST'])
def create_rental():
    data = request.get_json()
    required_fields = ["game_id", "customer_id","status","rent_date","due_date"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    
    new_rental = Rental(
        game_id = data['game_id'],
        customer_id = data['customer_id'],
        status = data['status'],
        rent_date = data['rent_date'],
        due_date = data['due_date'],
    )

    db.session.add()
    db.session.commit()
    return jsonify({"message": "rental successfully added"})

@app.route('rental/<int:rental_id>', methods = ['PUT'])
def update_rental(rental_id):
    data = request.get_json()
    r = Rental.query.get(rental_id)
    if not r:
        return jsonify({"error": "Rental not found"})
    
    r.game_id = data.get('game_id',r.game_id)
    r.customer_id = data.get('customer_id',r.customer_id )
    r.status = data.get('status',r.status)
    r.rent_date = data('rent_date',r.rent_date)
    r.due_date = data('due_date',r.due_date)
    r.duration = data('duration',r.duration)

    db.sessoin.commit()
    return jsonify({"message": "rental updated successfully"})

@app.route('/rental/,<int:rental_id>', methods = ['DELETE'])
def delete_rental(rental_id):
    r = Rental.query.get(rental_id)
    if not r:
        return jsonify({"error": "rental not found"}), 404
    
    db.session.delete(r)
    db.session.commit()
    return jsonify("message": "rental deleted successfully")
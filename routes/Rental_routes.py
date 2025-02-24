from flask import Flask, request, jsonify
from app import app, db
from model import Rental, Game, Customer
from datetime import datetime

@app.route('/rental', methods=['GET'])
def get_rentals():
    rentals = Rental.query.join(Game, Game.game_id == Rental.game_id).join(
        Customer, Customer.customer_id == Rental.customer_id).all()
    return jsonify([{
        "rental_id": r.rental_id,
        "game_id": r.game_id,
        "game_name": r.game.game_name,
        "customer_id": r.customer_id,
        "customer_name": r.customer.customer_name,
        "status": r.status,
        "rent_date": r.rent_date,
        "due_date": r.due_date,
        "duration": r.duration
    } for r in rentals])

@app.route('/rental/<int:rental_id>', methods=['GET'])
def get_rental(rental_id):
    r = Rental.query.get(rental_id)
    if not r:
        return jsonify({"error": "Rental not found"}), 404
    
    return jsonify({
        "rental_id": r.rental_id,
        "game_id": r.game_id,
        "customer_id": r.customer_id,
        "status": r.status,
        "rent_date": r.rent_date,
        "due_date": r.due_date,
        "duration": r.duration
    })

#To use in currently status
@app.route('/rental/renting/<int:customer_id>', methods=['GET'])
def get_renting_rentals_by_customerid(customer_id):
    rentals = Rental.query.filter_by(customer_id=customer_id, status='Renting').all()
    if not rentals:
        return jsonify({"error": "No renting rentals found"}), 404
    
    return jsonify([
        {
            "rental_id": r.rental_id,
            "game_id": r.game_id,
            "customer_id": r.customer_id,
            "status": r.status,
            "rent_date": r.rent_date,
            "due_date": r.due_date,
            "duration": r.duration,
            "game_link": r.game.image_link  # added game image link from relationship
        }
        for r in rentals
    ])


#To use in history
@app.route('/rental/returned/<int:customer_id>', methods=['GET'])
def get_returned_rentals_by_customerid(customer_id):
    rentals = Rental.query.filter_by(customer_id=customer_id, status='Returned').all()
    if not rentals:
        return jsonify({"error": "No returned rentals found"}), 404
    
    return jsonify([
        {
            "rental_id": r.rental_id,
            "game_id": r.game_id,
            "customer_id": r.customer_id,
            "status": r.status,
            "rent_date": r.rent_date,
            "due_date": r.due_date,
            "duration": r.duration
        }
        for r in rentals
    ])


@app.route('/rental', methods=['POST'])
def create_rental():
    data = request.get_json()
    required_fields = ["game_id", "customer_id", "status", "rent_date", "due_date"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    
    new_rental = Rental(
        game_id=data['game_id'],
        customer_id=data['customer_id'],
        status=data['status'],
        rent_date = datetime.strptime(data["rent_date"], "%d-%m-%Y").date(),
        due_date = datetime.strptime(data["due_date"], "%d-%m-%Y").date()
    )

    db.session.add(new_rental)
    db.session.commit()
    return jsonify({"message": "Rental successfully added",
                    "rental_id": new_rental.rental_id  # <-- must return this
})

@app.route('/rental/<int:rental_id>', methods=['PUT'])
def update_rental(rental_id):
    data = request.get_json()
    r = Rental.query.get(rental_id)
    if not r:
        return jsonify({"error": "Rental not found"}), 404
    
    r.status = data.get('status', r.status)

    db.session.commit()
    return jsonify({"message": "Rental updated successfully"})

@app.route('/rental/<int:rental_id>', methods=['DELETE'])
def delete_rental(rental_id):
    r = Rental.query.get(rental_id)
    if not r:
        return jsonify({"error": "Rental not found"}), 404
    
    db.session.delete(r)
    db.session.commit()
    return jsonify({"message": "Rental deleted successfully"})

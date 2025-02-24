from flask import Flask, request,jsonify
from app import app, db
from model import Banned_member

@app.route("/ban", methods=['GET'])
def get_banned():
    banned_member = Banned_member.query.all()
    return jsonify([{"ban_id" : bm.ban_id,
                     "customer_id" : bm.customer_id,
                     "reason" : bm.reason,
                     "ban_date" : bm.ban_date} for bm in banned_member])

# Create a new banned member entry
@app.route("/ban", methods=['POST'])
def create_ban():
    data = request.get_json()
    required_fields = ["customer_id", "reason"]

    # Validate required fields
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    new_ban = Banned_member(
        customer_id=data["customer_id"],
        reason=data["reason"],
        ban_date=data.get("ban_date")  # Can be provided or default to NULL
    )

    db.session.add(new_ban)
    db.session.commit()

    return jsonify({"message": "Member banned successfully", "ban_id": new_ban.ban_id}), 201
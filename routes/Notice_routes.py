from flask import Flask, request,jsonify
from app import app, db
from model import Notice

@app.route("/notice", methods=["GET"])
def get_notice():
    notice = Notice.query.all()
    return jsonify([{"notice_id" : n.notice_id,
                     "reason" : n.reason,
                     "date" : n.date,
                     "admin_id" : n.admin_id} for n in notice])

# Get a single notice by ID
@app.route('/notice/<int:notice_id>', methods=['GET'])
def get_notice_by_id(notice_id):
    notice = Notice.query.get(notice_id)
    if not notice:
        return jsonify({"error": "Notice not found"}), 404
    
    return jsonify({
        "notice_id": notice.notice_id,
        "reason": notice.reason,
        "date": notice.date.strftime('%Y-%m-%d'),
        "admin_id": notice.admin_id
    })

# Create a new notice
@app.route('/notice', methods=['POST'])
def create_notice():
    data = request.get_json()
    required_fields = ["reason", "admin_id"]
    
    # Check if required fields are present
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    
    new_notice = Notice(
        reason=data["reason"],
        date=data.get("date"),  # If not provided, will be NULL
        admin_id=data["admin_id"]
    )
    
    db.session.add(new_notice)
    db.session.commit()
    
    return jsonify({"message": "Notice created successfully"})

# Update an existing notice
@app.route('/notice/<int:notice_id>', methods=['PUT'])
def update_notice(notice_id):
    data = request.get_json()
    notice = Notice.query.get(notice_id)

    if not notice:
        return jsonify({"error": "Notice not found"}), 404

    # Update fields if provided in request
    notice.reason = data.get("reason", notice.reason)
    notice.date = data.get("date", notice.date)
    notice.admin_id = data.get("admin_id", notice.admin_id)

    db.session.commit()
    return jsonify({"message": "Notice updated successfully"})

# Delete a notice
@app.route('/notice/<int:notice_id>', methods=['DELETE'])
def delete_notice(notice_id):
    notice = Notice.query.get(notice_id)
    if not notice:
        return jsonify({"error": "Notice not found"}), 404

    db.session.delete(notice)
    db.session.commit()
    
    return jsonify({"message": "Notice deleted successfully"})
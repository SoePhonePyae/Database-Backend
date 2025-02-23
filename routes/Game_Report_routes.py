from flask import Flask, request, jsonify
from app import app, db
from model import Game_Report, Customer
from datetime import date

@app.route('/game_report', methods=['GET'])
def get_game_reports():
    game_reports = Game_Report.query.all()
    return jsonify([{
        "report_id": gr.report_id,
        "rental_id": gr.rental_id,
        "reason": gr.reason,
        "report_date": gr.report_date.strftime('%Y-%m-%d'),
        "detail": gr.detail,
        "attachment": gr.attachment
    } for gr in game_reports])

@app.route('/game_report/<int:report_id>', methods=['GET'])
def get_game_report(report_id):
    gr = Game_Report.query.get(report_id)
    if not gr:
        return jsonify({"error": "Report not found"}), 404
    return jsonify({
        "report_id": gr.report_id,
        "rental_id": gr.rental_id,
        "reason": gr.reason,
        "report_date": gr.report_date.strftime('%Y-%m-%d'),
        "detail": gr.detail,
        "attachment": gr.attachment
    })

@app.route('/game_report', methods=['POST'])
def create_game_report():
    data = request.get_json()
    required_fields = ["rental_id", "reason", "detail"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    new_report = Game_Report(
        rental_id=data["rental_id"],
        reason=data["reason"],
        report_date=data.get("report_date", date.today()),
        detail=data["detail"],
        attachment=data.get("attachment")
    )
    db.session.add(new_report)
    db.session.commit()
    return jsonify({"message": "Game reported"})

@app.route('/game_report/<int:report_id>', methods=['PUT'])
def update_game_report(report_id):
    data = request.get_json()
    gr = Game_Report.query.get(report_id)
    if not gr:
        return jsonify({"error": "Report not found"}), 404
    gr.rental_id = data.get("rental_id", gr.rental_id)
    gr.reason = data.get("reason", gr.reason)
    gr.report_date = data.get("report_date", gr.report_date)
    gr.detail = data.get("detail", gr.detail)
    gr.attachment = data.get("attachment", gr.attachment)
    db.session.commit()
    return jsonify({"message": "Game report updated successfully"})

@app.route('/game_report/<int:report_id>', methods=['DELETE'])
def delete_game_report(report_id):
    gr = Game_Report.query.get(report_id)
    if not gr:
        return jsonify({"error": "Report not found"}), 404
    db.session.delete(gr)
    db.session.commit()
    return jsonify({"message": "Game report deleted successfully"})
from flask import Flask,request,jsonify
from app import app,db
from model import Game_Report

@app.routes('/game_report', methods = ['GET'])
def get_game_reports():
    game_reports = Game_Report.query.all()
    return jsonify([{
        "report_id": gr.Report_ID,
        "customer_id": gr.Customer_ID,
        "rental_id": gr.Rental_ID,
        "reason": gr.Reason,
        "report_date": gr.Report_Date.strftime('%Y-%m-%d'),
        "detail": gr.Detail,
        "attachment": gr.Attachment
    } for gr in game_reports])


@app.route('/game_report/<int:report_id>', methods = ['GET'])
def get_game_report(report_id):
    gr = Game_Report.query.get(report_id)

    if not gr:
        return jsonify({"error" : "Report not found"}), 404
    
    return jsonify({
        "report_id": gr.Report_ID,
        "customer_id": gr.Customer_ID,
        "rental_id": gr.Rental_ID,
        "reason": gr.Reason,
        "report_date": gr.Report_Date.strftime('%Y-%m-%d'),
        "detail": gr.Detail,
        "attachment": gr.Attachment
    })


@app.route('/game_report', methods=['POST'])
def create_game_report():
    data = request.get_json()
    new_report = Game_Report(
        Customer_ID = data["customer_id"],
        Rental_ID = data["rental_id"],
        Reason=data["reason"],
        Report_Date=data["report-date"],
        Detail=data["detail"],
        Attachment=data.get("attachment")
    )
    db.session.add(new_report)
    db.session.commit()
    return jsonify({"message"})


@app.route('/game_report/<int:report_id>', methods = ['PUT'])
def update_game_report(report_id):
    data = request.get_json()
    gr = Game_Report.query.get(report_id)
    if not gr:
        return jsonify({"error": "Report not found"}), 404
    
    gr.Customer_ID = data.get("customer_id", gr.Customer_ID)
    gr.Rental_ID = data.get("rental_id", gr.Rental_ID)
    gr.Reason = data.get("reason", gr.Reason)
    gr.Detail = data.get("detail", gr.Detail)
    gr.Attachment = data.get("attachment", gr.Attacchment)

    db.session.commit()
    return jsonify({"message": "Game report updated successfully"})


@app.route('/game_report/<int:report_id>', methods = ['DELETE'])
def delete_game_report(report_id):
    gr = Game_Report.query.get(report_id)
    if not gr:
        return jsonify({"error": "Report not found"}),404
    
    db.session.delete(gr)
    db.session.commit()
    return jsonify({"message": "Game report deleted successfully"})
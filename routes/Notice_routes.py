from flask import jsonify
from app import app, db
from model import Notice

@app.route("/notice", methods=["GET"])
def get_notice():
    notice = Notice.query.all()
    return jsonify([{"notice_id" : n.notice_id,
                     "reason" : n.reason,
                     "date" : n.date,
                     "admin_id" : n.admin_id} for n in notice])
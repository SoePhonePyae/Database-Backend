from flask import jsonify
from app import app, db
from model import Banned_member

@app.route("/ban", methods=['GET'])
def get_banned():
    banned_member = Banned_member.query.all()
    return jsonify([{"ban_id" : bm.ban_id,
                     "customer_id" : bm.customer_id,
                     "reason" : bm.reason,
                     "ban_date" : bm.ban_date} for bm in banned_member])
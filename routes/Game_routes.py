from flask import Flask, request, jsonify
from app import app, db
from model import Game
from datetime import date

@app.route('/game', methods=['GET'])
def get_games():
    games = Game.query.all()
    return jsonify([{
        "game_id": g.game_id,
        "game_name": g.game_name,
        "release_date": g.release_date,
        "platform": g.platform,
        "genre": g.genre,
        "rating": g.rating,
        "stock_number": g.stock_number,
        "image_link": g.image_link,
        "admin_id": g.admin_id,
        "last_action": g.last_action
    } for g in games])

@app.route('/game/<int:game_id>', methods=['GET'])
def get_game(game_id):
    g = Game.query.get(game_id)
    if not g:
        return jsonify({"error": "Game not found"}), 404
    
    return jsonify({
        "game_id": g.game_id,
        "game_name": g.game_name,
        "release_date": g.release_date,
        "platform": g.platform,
        "genre": g.genre,
        "rating": g.rating,
        "stock_number": g.stock_number,
        "image_link": g.image_link,
        "admin_id": g.admin_id,
        "last_action": g.last_action
    })

@app.route('/game', methods=['POST'])
def create_game():
    data = request.get_json()
    required_fields = ['game_name', 'release_date', 'platform', 'genre', 'rating', 'stock_number', 'image_link', 'admin_id']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    
    new_game = Game(
        game_name=data["game_name"],
        release_date=data["release_date"],
        platform=data["platform"],
        genre=data["genre"],
        rating=data["rating"],
        stock_number=data["stock_number"],
        image_link=data["image_link"],
        admin_id=data["admin_id"],
        last_action="Added"
    )

    db.session.add(new_game)
    db.session.commit()
    return jsonify({"message": "Game added"})

@app.route('/game/<int:game_id>', methods=['PUT'])
def update_game(game_id):
    data = request.get_json()
    g = Game.query.get(game_id)
    if not g:
        return jsonify({"error": "Game not found"}), 404
    
    g.game_name = data.get("game_name", g.game_name)
    g.release_date = data.get("release_date", g.release_date)
    g.platform = data.get("platform", g.platform)
    g.genre = data.get("genre", g.genre)
    g.rating = data.get("rating", g.rating)
    g.stock_number = data.get("stock_number", g.stock_number)
    g.image_link = data.get("image_link", g.image_link)
    g.admin_id = data.get("admin_id", g.admin_id)
    g.last_action = "Updated"

    db.session.commit()
    return jsonify({"message": "Game updated successfully"})

@app.route('/game/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    g = Game.query.get(game_id)
    if not g:
        return jsonify({"error": "Game does not exist"}), 404

    db.session.delete(g)
    db.session.commit()
    return jsonify({"message": "Game deleted successfully"})

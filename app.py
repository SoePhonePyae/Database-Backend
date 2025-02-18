from database import *
import model
import routes

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print(app.url_map)
    app.run(debug=True)

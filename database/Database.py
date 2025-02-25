from flask_sqlalchemy import SQLAlchemy
import configparser
from flask import Flask
from flask_cors import CORS

config = configparser.ConfigParser()
config.read("config.properties")

#If there is error you need to create config.properties containing below variables
#values should be your pgsql configurations

DB_USER = config.get('DEFAULT','DB_USER')
DB_PASSWORD = config.get('DEFAULT','DB_PASSWORD')
DB_HOST = config.get('DEFAULT','DB_HOST')
DB_PORT = config.get('DEFAULT','DB_PORT')
DB_NAME = config.get('DEFAULT','DB_NAME')

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# 📌 You must use the exact column names defined in your Python model when querying in Flask.

db = SQLAlchemy(app)

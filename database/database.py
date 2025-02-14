from flask_sqlalchemy import SQLAlchemy
import configparser
from flask import Flask

config = configparser.ConfigParser()
config.read("config.properties")

#If there is error you need to create config.properties containing below variables
#values should be your pgsql configurations

DB_USER = config.get('DB_USER')
DB_PASSWORD = config.get('DB_PASSWORD')
DB_HOST = config.get('DB_HOST')
DB_PORT = config.get('DB_PORT')
DB_NAME = config.get('DB_NAME')

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 📌 You must use the exact column names defined in your Python model when querying in Flask.

db = SQLAlchemy(app)

from flask import Flask
import os

FINGGU_DATABASE_URI = os.getenv('DATABASE_URI')
FINGGU_SECRET_KEY = os.getenv('SECRET_KEY')

finggu_app = Flask(__name__)
finggu_app.config['SQLALCHEMY_DATABASE_URI'] = FINGGU_DATABASE_URI
finggu_app.config['SECRET_KEY'] = FINGGU_SECRET_KEY

from app import routes, models

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://omwefribumsmni:b09158b3abadbc44442fd3fb013e082c894568dada4e124549abf8212e5f42dc@ec2-3-91-112-166.compute-1.amazonaws.com:5432/dcol1vj6t5vjg4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
UPLOAD_FOLDER = './app/static/uploads'
db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views

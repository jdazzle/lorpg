from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from config import config

app = Flask(__name__)

db = SQLAlchemy()
socketio = SocketIO(app)

def create_app(config_name):
	
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	from .main import main as main_blueprint

	app.register_blueprint(main_blueprint)

	return app
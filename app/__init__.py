from flask import Flask
from flask_login import LoginManager
from flask_principal import Principal
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from config import config

app = Flask(__name__)

db = SQLAlchemy()
socketio = SocketIO(app)
login_manager = LoginManager()
principal = Principal(app)

def create_app(config_name):
	
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	from .main import main as main_blueprint

	app.register_blueprint(main_blueprint)

	db.init_app(app)
	login_manager.init_app(app)

	from .models import User
	@app.before_first_request
	def create_admin_user():
		print('1')
		admin_user = User.query.filter_by(id=1).first()
		if not admin_user:
			new_admin_user = User(
				name = 'admin',
				password = 'password'
			)
			db.session.add(new_admin_user)
			db.session.commit()

	return app
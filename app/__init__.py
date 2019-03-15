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
	from .character import character as character_blueprint
	from .user import user as user_blueprint

	app.register_blueprint(main_blueprint)
	app.register_blueprint(character_blueprint)
	app.register_blueprint(user_blueprint)

	db.init_app(app)
	login_manager.init_app(app)

	from .models import User, Character, Map
	@app.before_first_request
	def create_default_data():
		admin_user = User.query.filter_by(id=1).first()
		if not admin_user:
			new_admin_user = User(
				name = 'admin',
				password = 'password'
			)
			db.session.add(new_admin_user)
			db.session.commit()
			
			new_admin_character = Character(
				user_id = new_admin_user.id,
				name = 'Admin'
			)
			db.session.add(new_admin_character)
			db.session.commit()

		first_map = Map.query.filter_by(id=1).first()
		if not first_map:
			new_map = Map(
				name = 'admin_map'
			)
			db.session.add(new_map)
			db.session.commit()

	return app
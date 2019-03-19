from flask import Flask, url_for
from flask_login import LoginManager
from flask_principal import Principal
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from config import config, basedir
import os, sys

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
	from .map import map as map_blueprint
	from .user import user as user_blueprint

	db.init_app(app)
	login_manager.init_app(app)

	app.register_blueprint(main_blueprint)
	app.register_blueprint(character_blueprint)
	app.register_blueprint(map_blueprint)
	app.register_blueprint(user_blueprint)

	from .models import User, Character, Character_Stat, ImageResource, Map, Map_Tile, Stat, Tile
	@app.before_first_request
	def create_default_data():

		imagesdir = os.path.join(basedir, 'app\\static\\images')

		for subdir, dirs, files in os.walk(imagesdir):
			for file in files:
				relative_path = os.path.join(os.path.relpath(subdir, file), file).replace('..\\app\\', '').replace('\\', '/')
				imageresource = ImageResource.query.filter_by(filename=relative_path).first()
				if not imageresource:
					new_imageresource = ImageResource(
						filename = relative_path
					)
					db.session.add(new_imageresource)
					db.session.commit()

		admin_user = User.query.filter_by(id=1).first()
		if not admin_user:
			admin_user = User(
				name = 'admin',
				password = 'password'
			)
			db.session.add(admin_user)
			db.session.commit()

		admin_character = Character.query.filter_by(id=1).first()
		if not admin_character:
			admin_character = Character(
				user_id = admin_user.id,
				name = 'Admin'
			)
			db.session.add(admin_character)
			db.session.commit()

			stat_character_current_map = Stat(
				name = "current_map"
			)
			db.session.add(stat_character_current_map)
			db.session.commit()
			stat_character_current_x_position = Stat(
				name = "current_x_position"
			)
			db.session.add(stat_character_current_x_position)
			db.session.commit()
			stat_character_current_y_position = Stat(
				name = "current_y_position"
			)
			db.session.add(stat_character_current_y_position)
			db.session.commit()
			stat_character_tileset_filename = Stat(
				name = "tileset_filename"
			)
			db.session.add(stat_character_tileset_filename)
			db.session.commit()

			character_stat_current_map = Character_Stat(
				character_id = admin_character.id,
				stat_id = stat_character_current_map.id,
				value = "admin_map"
			)
			character_stat_current_x = Character_Stat(
				character_id = admin_character.id,
				stat_id = stat_character_current_x_position.id,
				value = "0"
			)
			character_stat_current_y = Character_Stat(
				character_id = admin_character.id,
				stat_id = stat_character_current_y_position.id,
				value = "0"
			)
			character_stat_graphic_filename = Character_Stat(
				character_id = admin_character.id,
				stat_id = stat_character_tileset_filename.id,
				value = 'static/images/characters/characters_1.png'
			)
			db.session.add(character_stat_current_map)
			db.session.commit()
			db.session.add(character_stat_current_x)
			db.session.commit()
			db.session.add(character_stat_current_y)
			db.session.commit()
			db.session.add(character_stat_graphic_filename)
			db.session.commit()

		first_map = Map.query.filter_by(id=1).first()
		if not first_map:
			first_map = Map(
				name = 'admin_map',
				background_filename = 'static/images/tiles/png/grass_1.png',
				width = 480,
				height = 640
			)
			db.session.add(first_map)
			db.session.commit()

			#grass_tile = Tile(
			#	name = 'grass_1',
			#	filename = 'static/images/tiles/png/grass_1.png',
			#	tile_width = 32,
			#	tile_height = 32
			#)
			#db.session.add(grass_tile)
			#db.session.commit()

			#for x in range(20):
			#	for y in range(30):
			#		map_tile = Map_Tile(
			#			map_id = first_map.id,
			#			tile_id = grass_tile.id,
			#			position_x = (x * 32),
			#			position_y = (y * 32),
			#			layer_index = 0
			#		)
			#		db.session.add(map_tile)
			#		db.session.commit()

	return app
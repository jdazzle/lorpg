from . import map
from .. import socketio
from flask import current_app, jsonify, redirect, render_template, url_for
from flask_login import current_user, login_user, login_required
from flask_principal import Identity, identity_changed
from flask_socketio import send, emit
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from app import db, login_manager, principal
from app.models import *
import functools

def authenticated_only(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            disconnect()
        else:
            return f(*args, **kwargs)
    return wrapped

@socketio.on('get_map_by_name')
@authenticated_only
def get_map_by_name(json):
	name = json['name']
	return_json = {}
	map = Map.query.filter_by(name=name).first()
	if map:
		return_json['id'] = map.id
		return_json['name'] = map.name
		return_json['background_filename'] = map.background_filename
		return_json['map_width'] = map.width
		return_json['map_height'] = map.height

		map_tiles_json = []
		for map_tile in map.map_tiles:
			map_tile_json = {
				'id': map_tile.id,
				'position_x': map_tile.position_x,
				'position_y': map_tile.position_y,
				'tile_id': map_tile.tile.id,
				'tile_name': map_tile.tile.name,
				'filename': map_tile.tile.filename
			}
			map_tiles_json.append(map_tile_json)
		return_json['map_tiles'] = map_tiles_json
	emit('get_map_by_name_response', return_json)
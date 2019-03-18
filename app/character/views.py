from . import character
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

@socketio.on('get_user_characters')
@authenticated_only
def get_user_characters(json):
	id = json['id']
	return_json = []
	user = User.query.filter_by(id=id).first()
	if user:
		for character in user.characters:
			character_json = {
				'id': character.id,
				'name': character.name
			}
			return_json.append(character_json)
	emit('get_user_characters_response', return_json)

@socketio.on('select_character')
@authenticated_only
def select_character(json):

	id = json['id']

	selected_character = Character.query.filter_by(id=id).first()
	
	if selected_character:
		current_user.character = selected_character

		json_selected_character = {}
		json_selected_character['id'] = selected_character.id
		json_selected_character['name'] = selected_character.name

		character_stats = []
		for character_stat in selected_character.stats:
			json_character_stat = {}
			json_character_stat['name'] = character_stat.stat.name
			json_character_stat['value'] = character_stat.value
			character_stats.append(json_character_stat)
		json_selected_character['stats'] = character_stats

		print(json_selected_character)

		emit('select_character_response', json_selected_character) 

from . import character
from .. import socketio
from flask import current_app, jsonify, redirect, render_template, url_for
from flask_login import login_user, login_required
from flask_principal import Identity, identity_changed
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from app import db, login_manager, principal
from app.models import *

@character.route('/user/<id>/characters')
@login_required
def get_user_characters(id):
	return_json = []
	user = User.query.filter_by(id=id).first()
	if user:
		for character in user.characters:
			character_json = {
				'id': character.id,
				'name': character.name
			}
			return_json.append(character_json)
	return jsonify(return_json)


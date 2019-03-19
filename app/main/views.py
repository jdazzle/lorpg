from . import main
from .. import socketio
from flask import current_app, jsonify, redirect, render_template, request, url_for
from flask_login import login_user, login_required
from flask_principal import Identity, identity_changed
from flask_socketio import send, emit
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from app import db, login_manager, principal
from app.models import *

connected_sockets = []

@main.route('/')
def index():
	form = LoginForm()
	return render_template('main/login.html', form=form)

@main.route('/game', methods=['GET'])
@login_required
def game():
	return render_template('main/game.html')

@socketio.on('connect')
def on_connect():
	print('socket connected')

@socketio.on('disconnect')
def on_disconnect():
	print('socket_disconnected')

@socketio.on_error()
def socketio_error_handler(e):
	print(e)

@socketio.on('my event')
def handle_my_event(json):
	print("received messagey")
	print(str(json))

@socketio.on('get_image_resources')
def get_image_resources():
	imageresources = ImageResource.query.all()
	return_json = []
	for imageresource in imageresources:
		print(imageresource)
		imageresource_json = {
			'id': imageresource.id,
			'filename': imageresource.filename
		}
		return_json.append(imageresource_json)
	emit('get_image_resources_response', return_json)

class LoginForm(FlaskForm):
	name = StringField('name', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])
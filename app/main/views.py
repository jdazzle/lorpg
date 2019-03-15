from . import main
from .. import socketio
from flask import current_app, jsonify, redirect, render_template, request, url_for
from flask_login import login_user, login_required
from flask_principal import Identity, identity_changed
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from app import db, login_manager, principal
from app.models import *

@main.route('/')
def index():
	form = LoginForm()
	return render_template('main/login.html', form=form)

@main.route('/game', methods=['GET'])
@login_required
def game():
	return render_template('main/game.html')

@socketio.on('my event')
def handle_my_event(json):
	print("received messagey")
	print(str(json))

class LoginForm(FlaskForm):
	name = StringField('name', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])
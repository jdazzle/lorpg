from . import main
from .. import socketio
from flask import current_app, render_template
from flask_login import login_user
from flask_principal import Identity, identity_changed
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from app import db, login_manager, principal
from app.models import *

@main.route('/')
def index():
	form = LoginForm()
	return render_template('main/index.html', form=form)

@login_manager.user_loader
def load_user(user_id):
	return User.query.filter_by(id=user_id).first()

@main.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(name=form.name.data).first()
		if user and form.password.data == user.password:
			login_user(user)
			identity_changed.send(current_app._get_current_object(),
				identity=Identity(user.id))
			print('success')
	return render_template('main/index.html', form=form)

@socketio.on('my event')
def handle_my_event(json):
	print("received messagey")
	print(str(json))

class LoginForm(FlaskForm):
	name = StringField('name', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])
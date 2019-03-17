from . import user
from .. import socketio
from flask import current_app, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_user, login_required
from flask_principal import Identity, identity_changed
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from app import db, login_manager, principal
from app.models import *

@login_manager.user_loader
def load_user(user_id):
	return User.query.filter_by(id=user_id).first()

@user.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(name=form.name.data).first()
		if user and form.password.data == user.password:
			login_user(user)
			identity_changed.send(current_app._get_current_object(),
				identity=Identity(user.id))
			return redirect(url_for('main.game'))
			
	return render_template('main/login.html', form=form)

class LoginForm(FlaskForm):
	name = StringField('name', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])

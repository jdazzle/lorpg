from . import db
from sqlalchemy import sql

class Ability(db.Model):
	__tablename__ = 'abilities'
	id = db.Column(db.Integer, primary_key=True)

class Character(db.Model):
	__tablename__ = 'characters'
	id = db.Column(db.Integer, primary_key=True)

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)

class User_Ability(db.Model):
	__tablename__ = 'users_abilities'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	ability_id = db.Column(db.Integer, db.ForeignKey('abilities.id'))
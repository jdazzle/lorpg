from . import db
from datetime import datetime
from sqlalchemy import sql

class Ability(db.Model):
	__tablename__ = 'abilities'
	id = db.Column(db.Integer, primary_key=True)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

class Ability_Effect(db.Model):
	__tablename__ = 'abilities_effects'
	id = db.Column(db.Integer, primary_key=True)
	ability_id = db.Column(db.Integer, db.ForeignKey('abilities.id'))
	effect_id = db.Column(db.Integer, db.ForeignKey('effects.id'))
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

class Character(db.Model):
	__tablename__ = 'characters'
	id = db.Column(db.Integer, primary_key=True)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

class Character_Ability(db.Model):
	__tablename__ = 'characters_abilities'
	id = db.Column(db.Integer, primary_key=True)
	character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
	ability_id = db.Column(db.Integer, db.ForeignKey('abilities.id'))
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

class Character_Stat(db.Model):
	__tablename__ = 'characters_stats'
	id = db.Column(db.Integer, primary_key=True)
	character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
	stat_id = db.Column(db.Integer, db.ForeignKey('stats.id'))
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

class Effect(db.Model):
	__tablename__ = 'effects'
	id = db.Column(db.Integer, primary_key=True)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

class Map(db.Model):
	__tablename__ = 'maps'
	id = db.Column(db.Integer, primary_key=True)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

class Map_Tile(db.Model):
	__tablename__ = 'maps_tiles'
	id = db.Column(db.Integer, primary_key=True)
	map_id = db.Column(db.Integer, db.ForeignKey('maps.id'))
	tile_id = db.Column(db.Integer, db.ForeignKey('tiles.id'))
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

class Tile(db.Model):
	__tablename__ = 'tiles'
	id = db.Column(db.Integer, primary_key=True)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

class Privileges(db.Model):
	__tablename__ = 'privileges'
	id = db.Column(db.Integer, primary_key=True)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

class Stat(db.Model):
	__tablename__ = 'stats'
	id = db.Column(db.Integer, primary_key=True)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

class User_Role(db.Model):
	__tablename__ = 'users_roles'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)
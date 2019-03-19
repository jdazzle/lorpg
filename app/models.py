from . import db
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import sql
from sqlalchemy_utils import PasswordType

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

class Animation(db.Model):
	__tablename__ = 'animations'
	id = db.Column(db.Integer, primary_key=True)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

class Animation_ImageResource(db.Model):
	__tablename__ = 'animations_imageresources'
	id = db.Column(db.Integer, primary_key=True)
	animation_id = db.Column(db.Integer, db.ForeignKey('animations.id'))
	imageresource_id = db.Column(db.Integer, db.ForeignKey('imageresources.id'))
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

	animation = db.relationship('Animation', foreign_keys=animation_id, backref='animation_imageresources')
	

class Character(db.Model):
	__tablename__ = 'characters'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	name = db.Column(db.Text)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

	user = db.relationship('User', foreign_keys=user_id, backref='characters')

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
	value = db.Column(db.Text)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

	character = db.relationship('Character', foreign_keys=character_id, backref='stats')
	stat = db.relationship('Stat', foreign_keys=stat_id, backref='character_stats')

class Character_Status(db.Model):
	__tablename__ = 'characters_statuses'
	id = db.Column(db.Integer, primary_key=True)
	character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
	status_id = db.Column(db.Integer, db.ForeignKey('statuses.id'))
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

class Effect(db.Model):
	__tablename__ = 'effects'
	id = db.Column(db.Integer, primary_key=True)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

class Item(db.Model):
	__tablename__ = 'items'
	id = db.Column(db.Integer, primary_key=True)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

class Item_Ability(db.Model):
	__tablename__ = 'items_abilities'
	id = db.Column(db.Integer, primary_key=True)
	item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
	ability_id = db.Column(db.Integer, db.ForeignKey('abilities.id'))
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

class Item_Stat(db.Model):
	__tablename__ = 'items_stats'
	id = db.Column(db.Integer, primary_key=True)
	item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
	stat_id = db.Column(db.Integer, db.ForeignKey('stats.id'))
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

class ImageResource(db.Model):
	__tablename__ = 'imageresources'
	id = db.Column(db.Integer, primary_key=True)
	filename = db.Column(db.Text)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)


class Map(db.Model):
	__tablename__ = 'maps'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	background_filename = db.Column(db.Text)
	width = db.Column(db.Text)
	height = db.Column(db.Text)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

class Map_Tile(db.Model):
	__tablename__ = 'maps_tiles'
	id = db.Column(db.Integer, primary_key=True)
	map_id = db.Column(db.Integer, db.ForeignKey('maps.id'))
	tile_id = db.Column(db.Integer, db.ForeignKey('tiles.id'))
	position_x = db.Column(db.Integer)
	position_y = db.Column(db.Integer)
	layer_index = db.Column(db.Integer)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

	map = db.relationship('Map', foreign_keys=map_id, backref='map_tiles')
	tile = db.relationship('Tile', foreign_keys=tile_id, backref='map_tiles')

class Tile(db.Model):
	__tablename__ = 'tiles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	filename = db.Column(db.Text)
	tile_width = db.Column(db.Float)
	tile_height = db.Column(db.Float)
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
	name = db.Column(db.Text)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

class Status(db.Model):
	__tablename__ = 'statuses'
	id = db.Column(db.Integer, primary_key=True)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

class User(db.Model, UserMixin):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	password = db.Column(PasswordType(
		schemes=[
			'pbkdf2_sha512',
			'md5_crypt'
		],
		deprecated=['md5_crypt']
	))
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)

	@property
	def is_active(self):
		return self.deleted_at == None
	

class User_Role(db.Model):
	__tablename__ = 'users_roles'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow)
	deleted_at = db.Column(db.DateTime)
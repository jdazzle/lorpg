import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	DEBUG = False

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'postgresql://mmorpg_user:mmorpg_user@localhost:5432/mmorpg'


config = {
	'default': DevelopmentConfig
}
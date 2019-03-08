import os
from app import create_app, db
from app.models import *
from flask_migrate import Migrate
from flask_socketio import SocketIO

app = create_app('default')

migrate = Migrate(app, db)

#if __name__ == 'main':
	#manager.run()
#	app.socketio.run(host='0.0.0.0')
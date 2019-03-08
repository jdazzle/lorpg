from . import main
from .. import socketio
from flask import render_template

@main.route('/')
def index():
	return render_template('main/index.html')

@socketio.on('my event')
def handle_my_event(json):
	print("received messagey")
	print(str(json))
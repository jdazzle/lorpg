var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function(){
	socket.emit('my event', {data: 'Im connected!'});
});

let app = new PIXI.Application({
	width: 256,
	height: 256,
	antialias: true,
	transparent: false,
	resolution: 1,
	forceCanvas: true
});

var mainDiv = document.getElementById('mainDiv')

mainDiv.appendChild(app.view)

app.renderer.view.style.position = "absolute";
app.renderer.view.style.display = "block";
app.renderer.autoResize = true;
app.renderer.resize(window.innerWidth - 40, window.innerHeight - 40);
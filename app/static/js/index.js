
//Start up the socket-io connection
var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function(){
	socket.emit('my event', {data: 'Im connected!'});
});

//Aliases for PIXI objects for ease of convention
let Application = PIXI.Application,
	loader = PIXI.loader,
	resources = PIXI.loader.resources,
	Sprite = PIXI.Sprite;

//Create a PIXIJS app
let app = new Application({
	width: 256,
	height: 256,
	antialias: true,
	transparent: false,
	resolution: 1,
	forceCanvas: true
});

//Add the PIXIJS app to the div called mainDiv
var mainDiv = document.getElementById('mainDiv')
mainDiv.appendChild(app.view)

//Do some styling on the PIXIJS app
app.renderer.view.style.position = "absolute";
app.renderer.view.style.display = "block";
app.renderer.autoResize = true;
app.renderer.resize(window.innerWidth - 40, window.innerHeight - 40);

//Load images into PIXI loader
loader
	.add('static/images/gui/bg_01_02.png')
	.load(setup);

//This function will be executed when the images have loaded
function setup(){

	let sprite = new Sprite(
		resources['static/images/gui/bg_01_02.png'].texture
	);

	app.stage.addChild(sprite);

	sprite.width = app.renderer.width;
	sprite.height = app.renderer.height;

	state = play;

	//Start the game loop
	app.ticker.add(delta => gameLoop(delta));
}

function gameLoop(delta){

	state(delta);

}

function play(delta){



}

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

let myCharacter = null;

//Add the PIXIJS app to the div called mainDiv
var mainDiv = document.getElementById('mainDiv')
mainDiv.appendChild(app.view)

//Do some styling on the PIXIJS app
app.renderer.view.style.position = "absolute";
app.renderer.view.style.display = "block";
app.renderer.autoResize = true;
app.renderer.resize(window.innerWidth - 40, window.innerHeight - 40);

window.addEventListener("resize", function() {
  app.renderer.resize(window.innerWidth - 40, window.innerHeight - 40);
});

//This function will be executed when the images have loaded
//function assetsLoaded(){

	//let sprite_bg = new Sprite(
	//	resources['static/images/gui/frame_c2_01.png'].texture
	//);

//	create_menu();

//	state = play;

	//Start the game loop
//	app.ticker.add(delta => gameLoop(delta));
//}

get_image_resources();

function gameLoop(delta){

	state(delta);

}

function get_image_resources(){

	socket.emit('get_image_resources');

	socket.on('get_image_resources_response', function(json){
		images_to_load = []
		for(var i = 0; i < json.length; i++){
			var filename = json[i]['filename']
			images_to_load.push(filename);
		}

		//Load images into PIXI loader
		loader.add(images_to_load).load(function(){
			console.log('done');
			create_character_select_stage();
			change_stage('character_select');
		});

	});

}

function change_stage(strStageName){

	switch(strStageName){
		case 'character_select':{
			app.stage = character_select_stage_container;
			break;
		}
		case 'map':{
			app.stage = map_container;
			break;
		}
	}

}

function play(delta){



}
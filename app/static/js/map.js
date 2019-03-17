map_container = new PIXI.Container()

function get_map_by_name(name){

	socket.emit('get_map_by_name', {'name': name});

	socket.on('get_map_by_name_response', function(json){
		console.log(json);
		load_map(json);
	});

}

function load_map(json){

	map_container.removeChildren();

	let map_width = 480;
	let map_height = 640;

	if(json['map_width']){
		map_width = parseInt(map_width);
	}
	if(json['map_height']){
		map_height = parseInt(map_height);
	}

	if(json['background_filename']){
		console.log(json['background_filename']);
		loader.add(json['background_filename']).load(function(){
			let background_tiling_sprite = new PIXI.extras.TilingSprite(
				resources[json['background_filename']].texture,
				map_width,
				map_height
			)
			map_container.addChild(background_tiling_sprite);
			map_container.scale.set(2);
			map_container.x = app.renderer.width / 2 - map_container.width / 2;
			map_container.y = app.renderer.height / 2 - map_container.height / 2;
		});

	}

	change_stage('map');

}

window.addEventListener("resize", function() {
 	map_container.x = app.renderer.width / 2 - map_container.width / 2;
	map_container.y = app.renderer.height / 2 - map_container.height / 2;
});
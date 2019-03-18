let map_container = new PIXI.Container();
let map_info = null;
let map_characters = [];

function get_map_by_name(name){

	socket.emit('get_map_by_name', {'name': name});

	socket.on('get_map_by_name_response', function(json){
		console.log(json);
		load_map(json);
	});

}

function load_map(json){

	map_info = json;

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

	load_map_characters();

	change_stage('map');

}

function load_map_characters(){

	socket.emit('get_map_characters_by_name', {'name': map_info['name']});

	socket.on('get_map_characters_by_name_response', function(json){
		console.log(json);
		
		let map_characters = json['map_characters']
		for(var i = 0; i < map_characters.length; i++){
			let map_character = map_characters[i];
			console.log(map_character);

			let sprite_position_x = map_character['stats'].find(function(element){
				return element['name'] == 'current_x_position';
			});

			let sprite_position_y = map_character['stats'].find(function(element){
				return element['name'] == 'current_y_position';
			});

			let sprite_filename = map_character['stats'].find(function(element){
				return element['name'] == 'tileset_filename';
			});

			if(sprite_filename){
				let texture = PIXI.utils.TextureCache[sprite_filename['value']];
				let character_sprite = new Sprite(texture);
				character_sprite.x = sprite_position_x['value'];
				character_sprite.y = sprite_position_y['value'];
				map_container.addChild(character_sprite);
			}

		}

	});

}

window.addEventListener("resize", function() {
 	map_container.x = app.renderer.width / 2 - map_container.width / 2;
	map_container.y = app.renderer.height / 2 - map_container.height / 2;
});

character_select_stage_container = new PIXI.Container()

let user_id = $("#user_id").val();

let array_characters = [];

let text_style1 = new PIXI.TextStyle({
	fontFamily: 'Arial',
	fontSize: 36,
	dropShadow: true,
	dropShadowBlur: 4,
	fill: ['#ffffff', '#00ff99'],
	stroke: '#4a1850',
	strokeThickness: 5
});

function create_character_select_stage(){

	//Load images into PIXI loader
	loader
		.add('static/images/gui/bg_01_02.png')
		.add('static/images/gui/button_01_01.png')
		.add('static/images/gui/frame_c2_01.png')
		.add('static/images/gui/plank_13.png')
		.load(assetsLoaded);

}

function assetsLoaded(){

	character_select_stage_container.width = app.renderer.width;
	character_select_stage_container.height = app.renderer.height;

	let background_sprite = new Sprite(
		resources['static/images/gui/bg_01_02.png'].texture
	)

	background_sprite.width = app.renderer.width;
	background_sprite.height = app.renderer.height;


	character_select_stage_container.addChild(background_sprite);

	let main_text = new PIXI.Text('Select a Character', text_style1);
	character_select_stage_container.addChild(main_text);

	main_text.x = app.renderer.width / 2 - main_text.width / 2;
	main_text.y = 30;

	get_my_characters();

}

function get_my_characters(){

	socket.emit('get_user_characters', {'id': user_id.toString()});

	socket.on('select_character_response', function(json){
		myCharacter = json;
		console.log(myCharacter);

		current_map = myCharacter.stats.find(function(element){
			return element.name == 'current_map';
		})

		if(current_map){
			get_map_by_name(current_map.value);
		}

	})

	socket.on('get_user_characters_response', function(json){
		
		array_characters = json;

		for(var i = 0; i < array_characters.length; i++){

			let container = new PIXI.Container()
			container.interactive = true;
			container.buttonMode = true;

			let sprite = new Sprite(
				resources['static/images/gui/plank_13.png'].texture
			)
			let text = new PIXI.Text(array_characters[i].name, text_style1);

			container.addChild(sprite);
			container.addChild(text);

			text.x = container.width / 2 - text.width / 2;
			text.y = 20;

			character_select_stage_container.addChild(container);
			container.x = 75;
			container.y = 100 + (i * (container.height + 20));
			container.character = array_characters[i];

			container.on('pointerdown', function(){

				socket.emit('select_character', container.character);

				/*$.ajax({
					url: '/selectcharacter',
					type: 'POST',
					contentType: 'application/json',
					data: JSON.stringify(container.character)
				}).done(function(result){
					console.log(result);
					if(result && result.success == true){
						console.log('good');
					}
				}).fail(function(xhr){
					console.log(xhr);
				}).always(function(){

				});*/

			});

		}

	});

}
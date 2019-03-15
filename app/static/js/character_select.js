
character_select_stage_container = new PIXI.Container()

function create_character_select_stage(){

	//Load images into PIXI loader
	loader
		.add('static/images/gui/bg_01_02.png')
		.add('static/images/gui/button_01_01.png')
		.add('static/images/gui/frame_c2_01.png')
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

}
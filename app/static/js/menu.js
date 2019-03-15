let main_menu_options = ['Options', 'Admin'];

let menuContainer = new PIXI.Container();

let menuButtons = [];

let bShow = false;

function create_menu(){

	create_menu_main_button();

	menuContainer.x = app.renderer.width - menuContainer.width;
	menuContainer.y = app.renderer.height - menuContainer.height;

	create_main_menu_options();

	app.stage.addChild(menuContainer);

}

function create_menu_main_button(){

	let tempContainer = new PIXI.Container();
	tempContainer.interactive = true;
	tempContainer.buttonMode = true;

	menuContainer.addChild(tempContainer);

	let style = new PIXI.TextStyle({
		fontFamily: 'Arial',
		fontSize: 36,
		dropShadow: true,
		dropShadowBlur: 4,
		fill: ['#ffffff', '#00ff99'],
		stroke: '#4a1850',
		strokeThickness: 5
	});

	let sprite_menu_button = new Sprite(
		resources['static/images/gui/button_01_01.png'].texture
	)
	let menu_text = new PIXI.Text('Menu', style);
	menu_text.x = sprite_menu_button.width / 2 - menu_text.width / 2;
	menu_text.y = sprite_menu_button.height / 2 - menu_text.height / 2 - 10;

	tempContainer.addChild(sprite_menu_button);
	tempContainer.addChild(menu_text);

	tempContainer.on('pointerdown', function(){
		
		if(!bShow){
			bShow = true;
			for(var i = 0; i < menuButtons.length; i++){
				menuButtons[i].visible = true;
			}
		} else {
			bShow = false;
			for(var i = 0; i < menuButtons.length; i++){
				menuButtons[i].visible = false;
			}
		}

	});

}

function create_main_menu_options(){

	let style = new PIXI.TextStyle({
		fontFamily: 'Arial',
		fontSize: 36,
		dropShadow: true,
		dropShadowBlur: 4,
		fill: ['#ffffff', '#00ff99'],
		stroke: '#4a1850',
		strokeThickness: 5
	});

	for(var i = 0; i < main_menu_options.length; i++){

		let tempContainer = new PIXI.Container();
		tempContainer.interactive = true;
		tempContainer.buttonMode = true;

		menuContainer.addChild(tempContainer);

		let sprite_menu_option = new Sprite(
			resources['static/images/gui/frame_c2_01.png'].texture
		)
		let menu_text = new PIXI.Text(main_menu_options[i], style);
		menu_text.x = sprite_menu_option.width / 2 - menu_text.width / 2;
		menu_text.y = sprite_menu_option.height / 2 - menu_text.height / 2;

		tempContainer.addChild(sprite_menu_option);
		tempContainer.addChild(menu_text);

		tempContainer.visible = bShow;

		menuButtons.push(tempContainer);

		tempContainer.y -= ((tempContainer.height + 10) * (menuContainer.children.length - 1));

	}

}
# game setup
WIDTH    = 1280	
HEIGTH   = 720
FPS      = 60
TILESIZE = 64

# ui 
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'MLHGW_PyGame_Zelda/graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# weapons 
weapon_data = {
	'sword': {'cooldown': 100, 'damage': 15,'graphic':'MLHGW_PyGame_Zelda/graphics/weapons/sword/full.png'},
	'lance': {'cooldown': 400, 'damage': 30,'graphic':'MLHGW_PyGame_Zelda/graphics/weapons/lance/full.png'},
	'axe': {'cooldown': 300, 'damage': 20, 'graphic':'MLHGW_PyGame_Zelda/graphics/weapons/axe/full.png'},
	'rapier':{'cooldown': 50, 'damage': 8, 'graphic':'MLHGW_PyGame_Zelda/graphics/weapons/rapier/full.png'},
	'sai':{'cooldown': 80, 'damage': 10, 'graphic':'MLHGW_PyGame_Zelda/graphics/weapons/sai/full.png'}}

#magic
magic_data = {
    'flame': {'strength': 5,'cost':20, 'graphic': 'MLHGW_PyGame_Zelda/graphics/particles/flame/fire.png'},
    'heal': {'strength': 20,'cost':10, 'graphic': 'MLHGW_PyGame_Zelda/graphics/particles/heal/heal.png'},
}

#monster
monster_data = {
	'squid': {'health': 100,'damage': 20,'exp': 100,'attack_type':'slash','attack_sound':'MLHGW_PyGame_Zelda/audio/slash.wav','speed': 3,'resistance': 3,'attack_radius': 80,'notice_radius': 360},
	'raccoon': {'health': 300,'damage': 40,'exp': 250,'attack_type':'claw','attack_sound':'MLHGW_PyGame_Zelda/audio/claw.wav','speed': 2,'resistance': 3,'attack_radius': 120,'notice_radius': 400},
	'spirit': {'health': 100,'damage': 8,'exp': 110,'attack_type':'thunder','attack_sound':'MLHGW_PyGame_Zelda/audio/fireball.wav','speed': 4,'resistance': 3,'attack_radius': 60,'notice_radius': 350},
	'bamboo': {'health': 70,'damage': 6,'exp': 120,'attack_type':'leaf_attack','attack_sound':'MLHGW_PyGame_Zelda/audio/slash.wav','speed': 3,'resistance': 3,'attack_radius': 50,'notice_radius': 300}

}
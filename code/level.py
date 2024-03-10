from typing import Iterable
from player import Player
import pygame
from random import choice
from pygame.sprite import AbstractGroup 
from settings import *
from tile import Tile
from debug import debug
from support import *
  # Import moved here

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        #creating the floor
        self.floor_surface = pygame.image.load('MLHGW_PyGame_Zelda/graphics/tilemap/ground.png').convert()
        self.floor_rect= self.floor_surface.get_rect(topleft = (0,0))

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #drwing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface,floor_offset_pos)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_rect = sprite.rect.move(-self.offset.x, -self.offset.y)
            self.display_surface.blit(sprite.image, offset_rect)

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        layout= {
            'boundary': import_csv_layout('MLHGW_PyGame_Zelda/map/map_FloorBlocks.csv'),
            'grass' : import_csv_layout('MLHGW_PyGame_Zelda/map/map_Grass.csv'),
            'object': import_csv_layout('MLHGW_PyGame_Zelda/map/map_LargeObjects.csv'),
        }
        graphics ={
            'grass': import_folder('MLHGW_PyGame_Zelda/graphics/grass'),
            'objects':import_folder('MLHGW_PyGame_Zelda/graphics/objects')
        }
        for style, layout in layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row): 
                    if col != '-1':  
                        x= col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y),[ self.obstacle_sprites],'invisible')
                        if style == 'grass':
                            random_grass_image = choice(graphics['grass'])
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'grass',random_grass_image)
                        if style == 'object':
                            if int(col) < len(graphics['objects']):
                                surf = graphics['objects'][int(col)]
                                Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object',surf)

        # Player instantiation moved outside create_map method
        self.player = Player((400, 300), [self.visible_sprites], self.obstacle_sprites)

    
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

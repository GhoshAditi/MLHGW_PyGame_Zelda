import pygame
from settings import *
from entity import Entity
from support import *

class Enemy(Entity):
    def __init__(self, groups, monster_name, pos):

        #general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'

        #graphics setup
        self.import_graphics(monster_name)
        self.status = 'idle'

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

    def import_graphics(self,name):
        self.animations = {'idle':[],'move':[],'attack':[]}
        main_path = f'MLHGW_PyGame_Zelda/graphics/monsters/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)
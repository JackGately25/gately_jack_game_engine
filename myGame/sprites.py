import pygame as pg
from pygame.sprite import Sprite

from pygame.math import Vector2 as vec
import os
from settings import *
from pygame import mixer

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')


# Initializing the Player Class
playerImage = pygame.image.load(os.path.join(img_folder, 'theBigBell.png'))
player_X = 370
player_Y = 523
player_Xchange = 0

# Initializing the Invader Class
invaderImage = []
invader_X = []
invader_Y = []
invader_Ychange = []
no_of_invaders = 8
# invader speed
invader_Xchange = [0.7] * no_of_invaders


# Initializing the Bullet class
# rest - bullet is not moving
# fire - bullet is moving
bulletImage = pygame.image.load(os.path.join(img_folder, 'bullet.png'))
bullet_X = 0
bullet_Y = 500
bullet_Xchange = 0
bullet_Ychange = 3
bullet_state = "rest"

# Initialize a background class
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location



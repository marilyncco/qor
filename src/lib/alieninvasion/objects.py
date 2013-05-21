# Alien Invasion: 2150 - a game inspired by Space Invaders
# Copyright (C) 2011 Thomas Chace <ithomashc@gmail.com>

# Alien Invasion: 2150 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Alien Invasion: 2150 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame
import random
from pygame.locals import *
from utils import *

import os, sys

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

random.seed()

class Asteroid():
    def __init__(self):
        self.rect = pygame.Surface((24,24))
        self.rect = self.rect.convert()
        self.rect.fill((250, 250, 250))
        self.image = load_image("images/asteroid.png")
        self.position = (random.randrange(0, 640 - 24), -24)
        self.xspeed = random.randrange(-1,1)
        self.yspeed = 5

    def update(self):
        self.position = (self.position[0] + self.xspeed, self.position[1] + self.yspeed)

class Alien():
    def __init__(self):
        self.rect = pygame.Surface((48,48))
        self.rect = self.rect.convert()
        self.rect.fill((250, 250, 250))
        
class Missle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image("images/spaceship.png", -1)
        self.image = load_image("images/asteroid.png")
        self.position = (320, 432)#(random.randrange(0, 640 - 24), -24)
        self.xspeed = 0#random.randrange(-1,1)
        self.yspeed = -8

    def update(self):
        self.position = (self.position[0] + self.xspeed, self.position[1] + self.yspeed)

class Ship(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image("images/spaceship.png", -1)
        #self.image = self.image.convert()
        self.position = (320, 432)
        self.xSpeed = 0
#    def __init__(self):
#        self.image = loadImage("images/spaceship.png")
#        #self.image = self.image.convert()
#        self.position = (320, 432)
#        self.xSpeed = 0
        
    def moveLeft(self):
        self.xSpeed = 10
       
    def moveRight(self):
        self.xSpeed = -10

    def stop(self):
        self.xSpeed = 0

    def update(self):
        self.position = (self.position[0] + self.xSpeed, self.position[1])

    def shoot(self):
        print("shoot!")

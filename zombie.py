import random

import pygame

from pygame.sprite import Sprite

class Zombie(Sprite):
	'''Zombie class.'''
	
	def __init__(self, sk_settings, screen, starting_x, starting_y):
		super().__init__()
		self.screen = screen
		self.sk_settings = sk_settings
		# Load image and initialize the zombie
		self.zombie = pygame.image.load('images/png/male/Idle (1).png')
		self.zombie = pygame.transform.scale(self.zombie, (75, 75))
		self.zombie = self.zombie.convert_alpha()
		self.rect = self.zombie.get_rect(left=25, top=0, width=25)
		self.zombie_health = 100
		
		# Start alien randomly on upper part of screen
		self.starting_x = starting_x
		self.starting_y = starting_y
		self.rect.x = self.starting_x
		self.rect.y = self.starting_y
		
		# Store Zombies Exact Position
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		
		# List of True and False
		self.random_move = (0, 1)
		
	
	def update(self, x_direction, y_direction):
		'''Move zombies around the screen.'''
		# Zombies horizontal movement
		self.x += (self.sk_settings.zombie_xspeed * x_direction)
		self.rect.x = self.x
		# Zombies Vertical movement
		self.y += (self.sk_settings.zombie_yspeed * y_direction)
		self.rect.y = self.y
		 
		
	def blitme(self):
		'''Draw alien to screen to practice.'''
		self.screen.blit(self.zombie, self.rect)
			
		
		

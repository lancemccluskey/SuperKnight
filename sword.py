import pygame

from pygame.sprite import Sprite

class Sword(Sprite):
	'''Store all Sword class attributes and methods.'''
	
	def __init__(self, sk_settings, screen, knight):
		'''Initial Sword attributes.'''
		super().__init__()
		self.screen = screen
		self.sk_settings = sk_settings
		self.knight = knight
		
		
		self.sword = pygame.Surface((40, 60))
		self.rect = self.sword.get_rect() 
		
		# Stores sword position as decimal
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		
		# Initial placement of sword
		self.rect.left = self.knight.rect.centerx + 25
		self.rect.bottom = self.knight.rect.bottom
		
		
	def draw_sword(self):
		'''Draw the sword attack window to the screen.'''
		self.screen.blit(self.sword, self.rect)
		
		
	def update(self, knight, right_direction):
		'''Update sword position to right next to the knight.'''
		if right_direction:
			self.rect.left = knight.rect.centerx + 25
			self.rect.bottom = knight.rect.bottom
		else:
			self.rect.right = knight.rect.centerx + 25
			self.rect.bottom = knight.rect.bottom
		
		
		
		
		
		

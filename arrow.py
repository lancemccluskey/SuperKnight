import pygame

from pygame.sprite import Sprite

class Arrow(Sprite):
	'''Arrow class for the character.'''
	
	def __init__(self, sk_settings, screen, knight, xspeed, yspeed, width, length):
		super().__init__()
		self.sk_settings = sk_settings
		self.screen = screen
		self.xspeed = xspeed
		self.yspeed = yspeed
		self.width = width
		self.length = length
		self.color = (0, 0, 0)
		self.dmg = 5
		
		self.rect = pygame.Rect(0, 0, self.width, self.length)
		
		# Draw arrow at knights position
		self.rect.center = knight.rect.center
		
		# Store arrows pos as a decimal value
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		

	def update(self):
		'''Update arrow positions on the screen.'''
		self.x += self.xspeed
		self.rect.x = self.x
		self.y += self.yspeed
		self.rect.y = self.y
		
		
	def draw_arrow(self):
		'''Draw an arrow to the screen.'''
		pygame.draw.rect(self.screen, self.color, self.rect)


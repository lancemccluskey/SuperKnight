import pygame

class Knight():
	'''Main character knight class.'''
	
	def __init__(self, sk_settings, screen):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.sk_settings = sk_settings
		
		# Make a black circle representing character
		self.knight = pygame.image.load('images/freeknight/png/Idle (1).png')
		self.knight = pygame.transform.scale(self.knight, (75, 75))
		self.knight = self.knight.convert_alpha()
		self.rect = self.knight.get_rect(left=25, top=0, width=25)

		
		# Place knight in middle of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		
		# store knights center coordinates as decimal numbers 
		self.center_x = float(self.rect.centerx)
		self.center_y = float(self.rect.centery)
		
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		
		# arrow direction
		self.shoot_right = False
		self.shoot_left = False
		
		
	def blitme(self):
		'''Draw the knight at his current location.'''
		self.screen.blit(self.knight, self.rect)

		
	def update(self):
		'''update knights position based on movement flag.'''
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center_x += self.sk_settings.kx_speed
		if self.moving_left and self.rect.left > 0:
			self.center_x -= self.sk_settings.kx_speed
		if self.moving_up and self.rect.top > 0:
			self.center_y -= self.sk_settings.ky_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.center_y += self.sk_settings.ky_speed
		# After, update knight rect object from the centerx and y
		self.rect.centerx = self.center_x
		self.rect.centery = self.center_y
		
		
	def recenter_knight(self):
		'''Put knight back in center of screen to restart game.'''
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery

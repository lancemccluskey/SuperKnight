
class Settings():
	'''All the settings for super knight game'''
	
	def __init__(self):
		
		# Screen settings
		self.bg_color = (75, 75, 100)
		self.window_width = 1200
		self.window_height = 800
		
		self.frame_rate = 60
		
		# knight settings
		self.kx_speed = 4
		self.ky_speed = 4
		self.knight_health = 100
		self.knight_armor = 100
		
		# Arrow settings
		self.arrow_dmg = 2
		
		
		# Sword settings
		self.sword_width = 20
		self.sword_length = 8
		self.sword_color = (135, 15, 15)
		self.sword_dmg = 10
		self.sword_swinging = False
		
		# Zombie Settings
		self.zombie_xspeed = 2
		self.zombie_yspeed = 2
		self.zombie_top_xdirection = 1
		self.zombie_top_ydirection = 1
		self.zombie_bottom_xdirection = 1
		self.zombie_bottom_ydirection = 1
		self.zombie_left_xdirection = 1
		self.zombie_left_ydirection = 1
		self.zombie_right_xdirection = 1
		self.zombie_right_ydirection = 1

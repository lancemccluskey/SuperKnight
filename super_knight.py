import time

import pygame
import game_functions as gf

from pygame.sprite import Group
from pygame.sprite import GroupSingle
from settings import Settings
from knight import Knight
from sword import Sword


def run_game():
	pygame.init()
	
	sk_settings = Settings()
	background = pygame.image.load('images/freetileset/png/BG/BG.png')
	background = pygame.transform.smoothscale(background, (sk_settings.window_width,
						sk_settings.window_height))
	screen = pygame.display.set_mode((sk_settings.window_width, 
						sk_settings.window_height))
	
	pygame.display.set_caption('Super Knight')
	fps = pygame.time.Clock()
	knight = Knight(sk_settings, screen)

	sword_container = GroupSingle()
	arrows_right = Group()
	arrows_left = Group()
	zombies_top = Group()
	zombies_bottom = Group()
	zombies_left = Group()
	zombies_right = Group()
	gf.populate_zombies(sk_settings, screen, zombies_top, zombies_bottom,
		zombies_left, zombies_right)
	
	while True:
		# everything redrawn every loop before flip called.
		# Step 1: Check for user input
		gf.check_events(sk_settings, screen, knight, arrows_right,
			arrows_left, sword_container)
		
		# Step 2: Apply user input to game objects
		knight.update()
		gf.update_zombies(sk_settings, screen, knight, arrows_right, arrows_left, 
			zombies_top, zombies_bottom, zombies_left, zombies_right)
		gf.update_arrows(sk_settings, screen, knight, arrows_right, arrows_left,
			zombies_top, zombies_bottom, zombies_left, zombies_right)
		gf.update_sword(sk_settings, screen, knight, sword_container,
			zombies_top, zombies_bottom, zombies_left, zombies_right)
		
		# Step 3: Redraw changes to game objects on the screen
		gf.update_screen(sk_settings, screen, knight, arrows_right,
			arrows_left, fps, zombies_top, zombies_bottom, zombies_left,
			zombies_right, background, sword_container)
		

run_game()

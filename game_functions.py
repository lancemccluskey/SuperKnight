import sys

import pygame

from arrow import Arrow
from sword import Sword
from zombie import Zombie
from time import sleep


def check_keydown_events(sk_settings, screen, knight, arrows_right,
		arrows_left, event, sword_container):
	'''what to do with keydown events.'''
	if event.key == pygame.K_RIGHT:
		knight.moving_right = True
		knight.shoot_right = True
		knight.shoot_left = False
	if event.key == pygame.K_LEFT:
		knight.moving_left = True
		knight.shoot_right = False
		knight.shoot_left = True
	if event.key == pygame.K_UP:
		knight.moving_up = True
	if event.key == pygame.K_DOWN:
		knight.moving_down = True
	if event.key == pygame.K_SPACE:
		fire_arrow(sk_settings, screen, knight, arrows_right,
			arrows_left)
	if event.key == pygame.K_z:
		swing_sword(sk_settings, screen, knight, sword_container)
		

def check_keyup_events(sk_settings, screen, knight, event, sword_container):
	'''Respond to keyup events.'''
	if event.key == pygame.K_RIGHT:
		knight.moving_right = False
	if event.key == pygame.K_LEFT:
		knight.moving_left = False
	if event.key == pygame.K_UP:
		knight.moving_up = False
	if event.key == pygame.K_DOWN:
		knight.moving_down = False
	if event.key == pygame.K_z:
		sheath_sword(sk_settings, screen, knight, sword_container)			
		
			
def check_events(sk_settings, screen, knight, arrows_right, 
		arrows_left, sword_container):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(sk_settings, screen, knight, arrows_right,
				arrows_left, event, sword_container)
		elif event.type == pygame.KEYUP:
			check_keyup_events(sk_settings, screen, knight, event, sword_container)
	
	
def swing_sword(sk_settings, screen, knight, sword_container):
	'''Function to create sword hit box next to knight.'''
	sk_settings.sword_swinging = True
	sword = Sword(sk_settings, screen, knight)
	sword_container.add(sword)
	
	
def sheath_sword(sk_settings, screen, knight, sword_container):
	'''Remove the sword hit box.'''
	sk_settings.sword_swinging = False
	sword_container.empty()
	
	
def update_sword(sk_settings, screen, knight, sword_container, zombies_top, 
		zombies_bottom, zombies_left, zombies_right):
	'''Update swords hit box position.'''
	if knight.shoot_right:
		sword_container.update(knight, knight.shoot_right)
	elif knight.shoot_left:
		sword_container.update(knight, 0)
	check_sword_zombie_collisions(sk_settings, screen, knight, sword_container,
		zombies_top, zombies_bottom, zombies_left, zombies_right)
		
		
def check_sword_zombie_collisions(sk_settings, screen, knight, sword_container,
		zombies_top, zombies_bottom, zombies_left, zombies_right):
	'''Check for sword/zombie collisions.'''
	collision1 = pygame.sprite.groupcollide(sword_container, zombies_top, False, False)
	collision2 = pygame.sprite.groupcollide(sword_container, zombies_bottom, False, False)
	collision3 = pygame.sprite.groupcollide(sword_container, zombies_left, False, False)
	collision4 = pygame.sprite.groupcollide(sword_container, zombies_right, False, False)
	if collision1:
		for zombies in collision1.values():
			for zombie in zombies:
				zombie.zombie_health -= sk_settings.sword_dmg
	if collision2:
		for zombies in collision2.values():
			for zombie in zombies:
				zombie.zombie_health -= sk_settings.sword_dmg
	if collision3:
		for zombies in collision3.values():
			for zombie in zombies:
				zombie.zombie_health -= sk_settings.sword_dmg
	if collision4:
		for zombies in collision4.values():
			for zombie in zombies:
				zombie.zombie_health -= sk_settings.sword_dmg
	
def fire_arrow(sk_settings, screen, knight, arrows_right, arrows_left):
	'''Create and fire an arrow.'''
	if knight.shoot_right:
		new_arrow = Arrow(sk_settings, screen, knight, 6, 0, 15, 4)
		arrows_right.add(new_arrow)
	elif knight.shoot_left:
		new_arrow = Arrow(sk_settings, screen, knight, -6, 0, 15, 4)
		arrows_left.add(new_arrow)
			
			
def update_arrows(sk_settings, screen, knight, arrows_right, arrows_left,
		zombies_top, zombies_bottom, zombies_left, zombies_right):
	'''Update all the arrows positions.'''
	arrows_right.update()
	arrows_left.update()
	for arrow in arrows_right.copy():
		if (arrow.rect.bottom <= 0 or 
		arrow.rect.top >= sk_settings.window_height or
		arrow.rect.left >= sk_settings.window_width or
		arrow.rect.right <= 0):
			arrows_right.remove(arrow)
	for arrow in arrows_left.copy():
		if (arrow.rect.bottom <= 0 or 
		arrow.rect.top >= sk_settings.window_height or
		arrow.rect.left >= sk_settings.window_width or
		arrow.rect.right <= 0):
			arrows_left.remove(arrow)
	check_arrow_zombie_collisions(sk_settings, screen, knight, arrows_right,
		arrows_left, zombies_top, zombies_bottom, zombies_left, zombies_right)
		
	if (len(zombies_top) == 0 and len(zombies_bottom) == 0 and 
		len(zombies_left) == 0 and len(zombies_right) == 0):
		populate_zombies(sk_settings, screen, zombies_top, zombies_bottom,
			zombies_left, zombies_right)
			
			
def check_arrow_zombie_collisions(sk_settings, screen, knight, arrows_right,
		arrows_left, zombies_top, zombies_bottom, zombies_left, zombies_right):
	'''Check for zombie/arrow collisions.'''
	# Check all collisions for right arrows first
	collisions1 = pygame.sprite.groupcollide(arrows_right, zombies_top, True, False)
	collisions2 = pygame.sprite.groupcollide(arrows_right, zombies_bottom, True, False)
	collisions3 = pygame.sprite.groupcollide(arrows_right, zombies_left, True, False)
	collisions4 = pygame.sprite.groupcollide(arrows_right, zombies_right, True, False)
	# Left Arrows
	collisions5 = pygame.sprite.groupcollide(arrows_left, zombies_top, True, False)
	collisions6 = pygame.sprite.groupcollide(arrows_left, zombies_bottom, True, False)
	collisions7 = pygame.sprite.groupcollide(arrows_left, zombies_left, True, False)
	collisions8 = pygame.sprite.groupcollide(arrows_left, zombies_right, True, False)
	if collisions1:
		for zombies in collisions1.values():
			for zombie in zombies:
				zombie.zombie_health -= sk_settings.arrow_dmg
	if collisions2:
		for zombies in collisions2.values():
			for zombie in zombies:
				zombie.zombie_health -= sk_settings.arrow_dmg
	if collisions3:
		for zombies in collisions3.values():
			for zombie in zombies:
				zombie.zombie_health -= sk_settings.arrow_dmg
	if collisions4:
		for zombies in collisions4.values():
			for zombie in zombies:
				zombie.zombie_health -= sk_settings.arrow_dmg
	if collisions5:
		for zombies in collisions5.values():
			for zombie in zombies:
				zombie.zombie_health -= sk_settings.arrow_dmg
	if collisions6:
		for zombies in collisions6.values():
			for zombie in zombies:
				zombie.zombie_health -= sk_settings.arrow_dmg
	if collisions7:
		for zombies in collisions7.values():
			for zombie in zombies:
				zombie.zombie_health -= sk_settings.arrow_dmg
	if collisions8:
		for zombies in collisions8.values():
			for zombie in zombies:
				zombie.zombie_health -= sk_settings.arrow_dmg
			
			
def update_zombies(sk_settings, screen, knight, arrows_right, arrows_left, 
				zombies_top, zombies_bottom, zombies_left, zombies_right):
	'''Update zombies position onscreen.'''
	zombies_top.update(sk_settings.zombie_top_xdirection, 
		sk_settings.zombie_top_ydirection)
	zombies_bottom.update(sk_settings.zombie_bottom_xdirection,
		sk_settings.zombie_bottom_ydirection)
	zombies_left.update(sk_settings.zombie_left_xdirection,
		sk_settings.zombie_left_ydirection)
	zombies_right.update(sk_settings.zombie_right_xdirection,
		sk_settings.zombie_right_ydirection)
	change_zombie_direction(sk_settings, screen, zombies_top, zombies_bottom,
		zombies_left, zombies_right)
	if (pygame.sprite.spritecollideany(knight, zombies_top) or
			pygame.sprite.spritecollideany(knight, zombies_bottom) or
			pygame.sprite.spritecollideany(knight, zombies_left) or
			pygame.sprite.spritecollideany(knight, zombies_right)):
		knight_hit(sk_settings, screen, knight, arrows_right, arrows_left, 
			zombies_top, zombies_bottom, zombies_left, zombies_right)
				
				
def knight_hit(sk_settings, screen, knight, arrows_right, arrows_left, 
				zombies_top, zombies_bottom, zombies_left, zombies_right):
	'''Lower the knights armor first, then health when hit.'''
	if sk_settings.knight_armor > 0:
		sk_settings.knight_armor -= 5
	elif sk_settings.knight_armor <= 0:
		if sk_settings.knight_health > 0:
			sk_settings.knight_health -= 10
		elif sk_settings.knight_health <= 0:
			# Get rid of everything on screen
			arrows_right.empty()
			arrows_left.empty()
			zombies_top.empty()
			zombies_bottom.empty()
			zombies_left.empty()
			zombies_right.empty()
			# Reset Game 
			populate_zombies(sk_settings, screen, zombies_top, zombies_bottom,
				zombies_left, zombies_right)
			knight.recenter_knight()
			sleep(1)
			
			
			
def change_zombie_direction(sk_settings, screen, zombies_top, zombies_bottom,
				zombies_left, zombies_right):
	'''Change the zombies direction if they hit a screen edge.'''
	screen_rect = screen.get_rect()
	for zombie in zombies_top.copy():
		if zombie.zombie_health <= 0:
			zombies_top.remove(zombie)
		if zombie.rect.right >= screen_rect.right:
			sk_settings.zombie_top_xdirection = -1
		elif zombie.rect.left <= 0:
			sk_settings.zombie_top_xdirection = 1
		if zombie.rect.top <= 0:
			sk_settings.zombie_top_ydirection = 1
		elif zombie.rect.bottom >= screen_rect.bottom:
			sk_settings.zombie_top_ydirection = -1	
	for zombie in zombies_bottom.copy():
		if zombie.zombie_health <= 0:
			zombies_bottom.remove(zombie)
		if zombie.rect.right >= screen_rect.right:
			sk_settings.zombie_bottom_xdirection = -1
		elif zombie.rect.left <= 0:
			sk_settings.zombie_bottom_xdirection = 1
		if zombie.rect.top <= 0:
			sk_settings.zombie_bottom_ydirection = 1
		elif zombie.rect.bottom >= screen_rect.bottom:
			sk_settings.zombie_bottom_ydirection = -1	
	for zombie in zombies_left.copy():
		if zombie.zombie_health <= 0:
			zombies_left.remove(zombie)
		if zombie.rect.right >= screen_rect.right:
			sk_settings.zombie_left_xdirection = -1
		elif zombie.rect.left <= 0:
			sk_settings.zombie_left_xdirection = 1
		if zombie.rect.top <= 0:
			sk_settings.zombie_left_ydirection = 1
		elif zombie.rect.bottom >= screen_rect.bottom:
			sk_settings.zombie_left_ydirection = -1	
	for zombie in zombies_right.copy():
		if zombie.zombie_health <= 0:
			zombies_right.remove(zombie)
		if zombie.rect.right >= screen_rect.right:
			sk_settings.zombie_right_xdirection = -1
		elif zombie.rect.left <= 0:
			sk_settings.zombie_right_xdirection = 1
		if zombie.rect.top <= 0:
			sk_settings.zombie_right_ydirection = 1
		elif zombie.rect.bottom >= screen_rect.bottom:
			sk_settings.zombie_right_ydirection = -1		


def populate_zombies(sk_settings, screen, zombies_top, zombies_bottom,
			zombies_left, zombies_right):
	'''Populate zombies on all four sides of the screen.'''
	screen_rect = screen.get_rect()
	zombie_top1 = Zombie(sk_settings, screen, screen_rect.centerx - 300, 25)
	zombie_top2 = Zombie(sk_settings, screen, screen_rect.centerx, 25)
	zombie_top3 = Zombie(sk_settings, screen, screen_rect.centerx + 300, 25)
	zombies_top.add(zombie_top1)
	zombies_top.add(zombie_top2)
	zombies_top.add(zombie_top3)
	zombie_bottom1 = Zombie(sk_settings, screen, screen_rect.centerx - 300, 
							screen_rect.bottom - 100)
	zombie_bottom2 = Zombie(sk_settings, screen, screen_rect.centerx,
							screen_rect.bottom - 100)
	zombie_bottom3 = Zombie(sk_settings, screen, screen_rect.centerx + 300,
							screen_rect.bottom - 100)
	zombies_bottom.add(zombie_bottom1)
	zombies_bottom.add(zombie_bottom2)
	zombies_bottom.add(zombie_bottom3)
	zombie_left1 = Zombie(sk_settings, screen, 25, screen_rect.centery - 200)
	zombie_left2 = Zombie(sk_settings, screen, 25, screen_rect.centery)
	zombie_left3 = Zombie(sk_settings, screen, 25, screen_rect.centery + 200)
	zombies_left.add(zombie_left1)
	zombies_left.add(zombie_left2)
	zombies_left.add(zombie_left3)
	zombie_right1 = Zombie(sk_settings, screen, screen_rect.right - 100,
							screen_rect.centery - 200)
	zombie_right2 = Zombie(sk_settings, screen, screen_rect.right - 100,
							screen_rect.centery)
	zombie_right3 = Zombie(sk_settings, screen, screen_rect.right - 100,
							screen_rect.centery + 200)
	zombies_right.add(zombie_right1)
	zombies_right.add(zombie_right2)
	zombies_right.add(zombie_right3)
	
			
def update_screen(sk_settings, screen, knight, arrows_right, arrows_left,
			fps, zombies_top, zombies_bottom, zombies_left, 
			zombies_right, background, sword_container):
	'''Update the screen with everything drawn.'''
	screen.blit(background, (0, 0))
	for arrow in arrows_right.sprites():
		arrow.draw_arrow()
	for arrow in arrows_left.sprites():
		arrow.draw_arrow()
	if sk_settings.sword_swinging:
		sword_container.sprite.draw_sword()
	knight.blitme()	
	for zombie in zombies_top.sprites():
		zombie.blitme()
	for zombie in zombies_bottom.sprites():
		zombie.blitme()
	for zombie in zombies_left.sprites():
		zombie.blitme()
	for zombie in zombies_right.sprites():
		zombie.blitme()
	fps.tick(sk_settings.frame_rate)
	pygame.display.flip()

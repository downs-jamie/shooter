import pygame
from pygame.sprite import Group, groupcollide
from Player import Player
from Bad_guy import Bad_guy
from bullet import bullet


pygame.init()

screen_size = (1000,800)

background_color = (82,111,53)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("EPIC SHOOTER")

the_player = Player('joker.png',100,100, screen)
bad_guy = Bad_guy(screen)
bad_guys = Group()
bad_guys.add(bad_guy)
bullets = Group()


# the_player_image = pygame.image.load('batman.png')
# player = {
# 	"x": 100,
# 	"y": 100
# }

game_on = True

while game_on:


	for event in pygame.event.get():
		# print event
		if event.type == pygame.QUIT:
			game_on = False
		elif event.type == pygame.KEYDOWN:
			print event.key
			if event.key == 273:
				# the_player.y -= the_player.speed
				the_player.should_move('up',True)
			elif event.key == 274:
				# the_player.y += the_player.speed
				the_player.should_move('down',True)
			elif event.key == 275:
				# the_player.x += the_player.speed
				the_player.should_move('right',True)
			elif event.key == 276:
				# the_player.x -= the_player.speed
				the_player.should_move('left',True)
			elif event.key == 32:
				
				new_bullet = bullet(screen, the_player, 1)
				bullets.add(new_bullet)
				new_bullet = bullet(screen, the_player, 3)
				bullets.add(new_bullet)

		elif event.type == pygame.KEYUP:
			if event.key == 273:
				# the_player.y -= the_player.speed
				the_player.should_move('up',False)
			elif event.key == 274:
				# the_player.y += the_player.speed
				the_player.should_move('down',False)
			elif event.key == 275:
				# the_player.x += the_player.speed
				the_player.should_move('right',False)
			elif event.key == 276:
				# the_player.x -= the_player.speed
				the_player.should_move('left',False)	
	#print bullets			
	screen.fill(background_color)
	for bad_guy in bad_guys:
		bad_guy.update_me(the_player)
	# Bad_guy.update_me(the_player)
		bad_guy.draw_me()
	the_player.draw_me()
	
	for bullet in bullets:
		bullet.update()
		bullet.draw_bullet()

	bullet_hit = groupcollide(bullets,bad_guys,True,True)	

	# screen.blit(the_player.image, [the_player.x, the_player.y])
	pygame.display.flip()





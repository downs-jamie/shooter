import pygame
from Player import Player

pygame.init()

screen_size = (1000,800)

background_color = (82,111,53)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("EPIC SHOOTER")

the_player = Player('joker.png',100,100, screen)

# the_player_image = pygame.image.load('batman.png')
# player = {
# 	"x": 100,
# 	"y": 100
# }

game_on = True

while game_on:


	for event in pygame.event.get():
		print event
		if event.type == pygame.QUIT:
			game_on = False
		elif event.type == pygame.KEYDOWN:
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

	screen.fill(background_color)

	the_player.draw_me()
	# screen.blit(the_player.image, [the_player.x, the_player.y])
	pygame.display.flip()





import pygame

global BLACK, WHITE
BLACK = (0,0,0)
WHITE = (255,255,255)

def main():
	running = True
	(height, width) = (600, 800)
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption('Space Adventure')
	screen.fill(BLACK)
	ship_x = 400
	#ship_y = 10
	bullet_y = 0
	bullet_x = 0
	bullet_yspeed = 0
	ship_xspeed = 0
	#ship_yspeed = 0
	ship = pygame.image.load("spaceship.png").convert()
	ship.set_colorkey(WHITE)
	ship = pygame.transform.scale(ship, (60, 60))
	pygame.init()
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					ship_xspeed = -0.5
				elif event.key == pygame.K_RIGHT:
					ship_xspeed = 0.5
				elif event.key == pygame.K_SPACE:
					bullet_y = 540
					bullet_x = ship_x + 30
					bullet_yspeed = -1
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					ship_xspeed = 0
		#set the ship and bullet speed
		ship_x += ship_xspeed
		bullet_y += bullet_yspeed
		#refill the screen for previous things on screen
		screen.fill(BLACK)
		#draw the ship
		screen.blit(ship, (int(ship_x), 530))
		#draw the bullet
		bullet = pygame.draw.circle(screen, WHITE, (int(bullet_x), int(bullet_y)), 5)
		pygame.display.update()

if __name__ == "__main__":
	main()

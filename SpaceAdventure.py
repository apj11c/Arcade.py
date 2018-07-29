from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import mainScreen
import pygame
import random

global BLACK, WHITE
BLACK = (0,0,0)
WHITE = (255,255,255)
CRIMSON = (220,20,60)

def main():
	running = True
	timeOut = False
	(height, width) = (600, 800)
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption('Space Adventure')
	screen.fill(BLACK)
	astroids = []
	points = 0
	ship_x = 400
	#ship_y = 10
	bullet_y = -10
	bullet_x = -10
	bullet_yspeed = 0
	ship_xspeed = 0
	#ship_yspeed = 0
	ship = pygame.image.load("Images/spaceship.png").convert()
	ship.set_colorkey(WHITE)
	ship = pygame.transform.scale(ship, (60, 60))
	astroid = pygame.image.load("Images/astroid.png").convert()
	astroid.set_colorkey(WHITE)
	astroid = pygame.transform.scale(astroid, (50, 50))
	background = pygame.image.load("Images/background.png").convert()
	background = pygame.transform.scale(background, (800, 650))
	pygame.init()
	start_ticks = pygame.time.get_ticks()
	font = pygame.font.Font(None, 30)

	#game loop
	while running:
		milliseconds=(pygame.time.get_ticks()-start_ticks)
		seconds=(pygame.time.get_ticks()-start_ticks)/1000
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				popUp = mainScreen.QuitMessage()
				reply = popUp.exec_()
				running = False if reply == QMessageBox.Yes else True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					ship_xspeed = -4
				elif event.key == pygame.K_RIGHT:
					ship_xspeed = 4
				elif event.key == pygame.K_SPACE:
					bullet_y = 540
					bullet_x = ship_x + 30
					bullet_yspeed = -8
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					ship_xspeed = 0

		#set the ship and bullet speed
		ship_x += ship_xspeed
		bullet_y += bullet_yspeed

		#refill the screen for previous things on screen
		screen.fill(BLACK)

		screen.blit(background, (0, 0))

		#draw the ship
		screen.blit(ship, (int(ship_x), 530))

		#draw the bullet
		bullet = pygame.draw.circle(screen, CRIMSON, (int(bullet_x), int(bullet_y)), 7)

		#draw the astroids
		astroid_x = random.randint(1, 800)
		astroid_y = random.randint(1, 300)
		if milliseconds % 200 == 0:
			coords = [astroid_x, astroid_y]
			astroids.append(coords)
		for ast in astroids:
			temp = pygame.draw.circle(screen, WHITE, (ast[0]+25, ast[1]+25), 25)
			screen.blit(astroid, (ast[0], ast[1]))
			if bullet.colliderect(temp):
				astroids.remove(ast)
				points += 10

		#points and timer
		if seconds > 60:
			timeOut = True
			break;
		text = font.render("Timer: "+str(60 - int(seconds)), 1, (255,255,255))
		screen.blit(text, (20, 580))
		text2 = font.render("Score: "+str(points), 1, (255,255,255))
		screen.blit(text2, (150, 580))			
		
		pygame.display.update()

	#display the game results
	if timeOut:
		runningGameOverScreen = True
		screen.fill(BLACK)
		text=font.render("GAME OVER", 1, (255,255,255))
		screen.blit(text, (340, 300))
		text3 = font.render("Score: " + str(points), 1, (255,255,255))
		screen.blit(text2, (360, 330))
		pygame.display.update()
		while runningGameOverScreen:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					runningGameOverScreen = False
					break;

	pygame.display.quit()
	pygame.quit()

if __name__ == "__main__":
	main()

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import mainScreen
import pygame
import random

global screen, WHITE, running
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)   

def main():
	running = True
	timeOut = False
	(height, width) = (600, 800)
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption('Milapede')
	screen.fill(BLACK)
	x_speed = 0
	y_speed = 0
	x_coord = 400
	y_coord = 300
	food = None
	food_x = 0
	food_y = 0
	snakeLength = 1
	direction = 0
	pygame.init()
	start_ticks = pygame.time.get_ticks()
	font = pygame.font.Font(None, 30)

	#game main loop
	while running:
		seconds=(pygame.time.get_ticks()-start_ticks)/1000
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				popUp = mainScreen.QuitMessage()
				reply = popUp.exec_()
				running = False if reply == QMessageBox.Yes else True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_speed = -2
					direction = 3
				elif event.key == pygame.K_RIGHT:
					x_speed = 2
					direction = 1
				elif  event.key == pygame.K_UP:
					y_speed = -2
					direction = 0
				elif event.key == pygame.K_DOWN:
					y_speed = 2
					direction = 2
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_speed = 0
				elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_speed = 0
		x_coord += x_speed
		y_coord += y_speed

		#Handle screen wrapping
		if x_coord < 0:
			x_coord = 800
		if x_coord > 800:
			x_coord = 0
		if y_coord < 0:
			y_coord = 600
		if y_coord > 600:
			y_coord = 0

		#re-filling screen from previous circles when moving
		screen.fill(BLACK)

		#Randomly spawn starting food circle
		if food == None:
			food_x = random.randint(1, 800)
			food_y = random.randint(1, 600)
			food = pygame.draw.circle(screen, WHITE, (food_x, food_y), 7)
		else:
			food = pygame.draw.circle(screen, WHITE, (food_x, food_y), 7)

		#draws circle during movement
		head = pygame.draw.circle(screen, WHITE, (int(x_coord), int(y_coord)), 10)

		#drawing preceeding body of snake
		counter = 0
		while counter != snakeLength:
			if direction == 0:
				pygame.draw.circle(screen, WHITE, (int(x_coord), int(y_coord) + (counter*10)), 10)
			elif direction == 2:
				pygame.draw.circle(screen, WHITE, (int(x_coord), int(y_coord) - (counter*10)), 10)
			elif direction == 1:
				pygame.draw.circle(screen, WHITE, (int(x_coord - (counter*10)), int(y_coord)), 10)
			else:
				pygame.draw.circle(screen, WHITE, (int(x_coord + (counter*10)), int(y_coord)), 10)
			counter += 1
		
		#collision detection with food and head of snake
		if head.colliderect(food):
			food = None
			snakeLength += 1
		
		#timer display
		if seconds > 60:
			timeOut = True
			break;
		text = font.render("Timer: "+str(60 - int(seconds)), 1, (255,255,255))
		screen.blit(text, (20, 580))

		#FPS update
		pygame.display.update()
			
#	#display the game results
	if timeOut:
		runningGameOverScreen = True
		screen.fill(BLACK)
		text=font.render("GAME OVER", 1, (255,255,255))
		screen.blit(text, (340, 300))
		text2=font.render("Score: " + str(snakeLength), 1, (255,255,255))
		screen.blit(text2, (360, 330))
		pygame.display.update()
		while runningGameOverScreen:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					runningGameOverScreen = False

	pygame.display.quit()
	pygame.quit()
		
if __name__ == "__main__":
	main()

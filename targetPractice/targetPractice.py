import pygame
import os
import random
import Circle as myCircleClass		#self created class

pygame.init()

dispHeight = 800
dispWidth = 600
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 50, 50)
BLUE = (0,0,255)
GREEN = (34,139,34)
GOLD = (255,215,0)

gameDisplay = pygame.display.set_mode((dispHeight,dispWidth))
pygame.display.set_caption("Target Practice")
fps = pygame.time.Clock()
crashed = False

imageDimensions = gameDisplay.get_rect()
centerX = imageDimensions.centerx
centerY = imageDimensions.centery
speed = 30
count = 0
score = 0
lives = 3
font_name = pygame.font.match_font('arial')
backgroundImage = pygame.image.load("target_background.png").convert()
backgroundImage = pygame.transform.scale(backgroundImage, (800,600))

def drawTarget():
	pygame.draw.circle(gameDisplay, GREEN, [centerX,centerY], 30)
	pygame.draw.circle(gameDisplay, BLACK, [centerX,centerY], 20)
	pygame.draw.circle(gameDisplay, BLUE, [centerX, centerY], 15)

def render(x,y,speed):
	'''displays the circle coming to the target'''
	pygame.draw.circle(gameDisplay, GOLD, [int(x),int(y)], 8)
	fps.tick(speed)

def draw_score(display, x,y):
	font = pygame.font.Font(font_name, 18)
	score_surface = font.render("Total Score: "+ str(score), True, BLACK)
	text_rect = score_surface.get_rect()
	text_rect.midtop = (x,y)
	display.blit(score_surface, text_rect)

def checkHit(x,y):
	'''checks for hit on target based of circles x,y coordinates passed in'''
	pygame.draw.circle(gameDisplay, RED, [int(x), int(y)], 4)

	if ((int(x) >= centerX-30) and (int(x) <= centerX+30)) and ((int(y) >= centerY-30) and (int(y) <= centerY+30)):
		return True
	else:
		return False

def drawLives(display, life):
		font = pygame.font.Font(font_name, 18)
		lives_surface = font.render("Lives remaining : ", True, BLACK)
		text_rect = lives_surface.get_rect()
		text_rect.midtop = (100,570)
		display.blit(lives_surface, text_rect)

		if life == 3:
			pygame.draw.circle(gameDisplay, GOLD, [180,580], 8)
			pygame.draw.circle(gameDisplay, GOLD, [200,580], 8)
			pygame.draw.circle(gameDisplay, GOLD, [220,580], 8)
		elif life == 2:
			pygame.draw.circle(gameDisplay, GOLD, [180,580], 8)
			pygame.draw.circle(gameDisplay, GOLD, [200,580], 8)
		elif life == 1:
			pygame.draw.circle(gameDisplay, GOLD, [180,580], 8)

myCircle = myCircleClass.Circle()

x,y = myCircle.getStartingCoords()
slope =  myCircle.slopeEquation(x,y)
yIntercept = myCircle.getYIntercept(x,y,slope)
scoreFlag = False
gameDisplay.blit(backgroundImage,[0,0])		#shows our background starting at pos (0,0)

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
		#print("This is the speed = ", speed)

	if x > dispHeight or y > dispWidth:
		x,y = myCircle.getStartingCoords()
		slope = myCircle.slopeEquation(x,y)
		yIntercept = myCircle.getYIntercept(x,y,slope)
		scoreFlag = False

	gameDisplay.blit(backgroundImage, [0,0])
	draw_score(gameDisplay, dispWidth/2, 10)
	drawTarget()
	drawLives(gameDisplay, lives)
	render(x,y,speed)

	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_SPACE:
			if checkHit(x,y) == True and scoreFlag == False:
				score += 10
				scoreFlag = True
				speed += 3
			elif checkHit(x,y) == False and scoreFlag == False:
				lives -= 1
			scoreFlag = True

	pygame.display.update()
	x,y = myCircle.getAdjustedXY(x, y, slope, yIntercept)

pygame.quit()
quit()

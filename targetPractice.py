import pygame
import os
import random

pygame.init()

dispHeight = 800
dispWidth = 600
white = (255,255,255)
black = (0,0,0)
red = (255, 50, 50)

gameDisplay = pygame.display.set_mode((dispHeight,dispWidth))
pygame.display.set_caption("Target Practice")
fps = pygame.time.Clock()
crashed = False

imageDimensions = gameDisplay.get_rect()
centerX = imageDimensions.centerx
centerY = imageDimensions.centery
speed = 30
count = 0

def getStartingCoords():
	'''returns the starting coordinates of a newly generated circle'''
	x = random.randint(1,800)
	y = 0
	return x,y

def drawCircle():
	'''draws the circle of the target'''
	pygame.draw.circle(gameDisplay, black, [centerX,centerY], 30, 4)
	pygame.draw.circle(gameDisplay, black, [centerX,centerY], 20, 3)
	pygame.draw.circle(gameDisplay, black, [centerX, centerY], 15, 1)

def render(x,y,speed):
	'''displays the circle coming to the target'''
	pygame.draw.circle(gameDisplay, red, [int(x),int(y)], 8, 1)
	pygame.display.update()
	fps.tick(speed)

def slopeEquation(x,y):
	'''return slope of the line that the cirlce is traveling on
	based on m = (y_2 - y_1)/(x_2 - x_1)'''
	if (centerX - x) == 0:
		return 0
	else:
		slope = (centerY - y) / (centerX - x)
		return slope

def getYIntercept(x,y,slope):
	'''returns the y-intercept, based off y=mx+b where b = (mx-y)*-1'''
	b = ((slope * x) - y) * -1
	return b

def getAdjustedXY(x,y,m,b):
	'''returns the adjusted x,y of the circle after it moves
	once again based off of y=mx+b'''
	y += 5
	if m == 0:
		return y
	else:
		x = (y - b) / m
		return x,y

def checkHit(x,y):
	'''checks for hit on target based of circles x,y coordinates passed in'''
	print("the x is ", x, "the y is ", y)

while not crashed:
	x,y = getStartingCoords()
	slope = slopeEquation(x,y)
	yIntercept = getYIntercept(x,y,slope)

	while x < 800 and y < 600:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True
		#print("This is the speed = ", speed)

		gameDisplay.fill(white)
		drawCircle()
		render(x,y,speed)
		pygame.display.flip

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				checkHit(x,y)

		x,y = getAdjustedXY(x, y, slope, yIntercept)

		if count == 3:
			count = 0
			speed += 3
	if count < 3:
		count += 1

pygame.quit()
quit()

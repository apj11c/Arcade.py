import pygame
import os
from random import randint
from Node import Node	#self written class to handle graph nodes

pygame.init()

dispWidth = 600
dispHeight = 600
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 50, 50)
BLUE = (0,0,255)
GREEN = (34,139,34)
GOLD = (255,215,0)
MOVEMENT_FLAG = ''
wallFlag = ''
SCORE = 0
INKY_FLAG = ''
PINKY_FLAG = ''
BLINKY_FLAG = ''
CLYDE_FLAG = ''
PINKY_START = False
BLINKY_START = False
CLYDE_START = False

nodeList= [(16,16), (125,16), (249, 16), (321, 16), (445,16), (554,16), (16,89), (125,89), (190,89), (249,89), (321,89), (385,89), (445,89), (554,89), (16,150), (125,150), (190, 149), (254, 149), (320,149), (385,149), (445,150), (554,150), (190, 209), (254, 209), (320,209), (385,209), (16,265), (125,265), (190,265), (385,265), (445,265), (554,265), (190, 325), (385,325), (16,379), (125,379), (190,379), (250,379), (320,379), (385,379), (445,379), (554,379), (16,440), (60,440), (125,440), (186,440), (250, 440), (320,440), (385,440), (445, 440), (510,440), (554,440), (16, 498), (60,498), (125,498), (186,498), (249,498), (321,498), (385,498), (445,498), (510, 498), (554,498), (16, 554), (249,554), (321, 554), (554,554)]
#list of all the decision points in the graph
foodList= [(16,16), (125,16), (249, 16), (321, 16), (445,16), (554,16), (16,89), (125,89), (190,89), (249,89), (321,89), (385,89), (445,89),(554,89), (16,150), (125,150), (190, 149), (254, 149), (320,149), (385,149), (445,150), (554,150), (190, 209), (254, 209), (320,209),(385,209), (16,265), (125,265), (190,265), (385,265), (445,265), (554,265), (190, 325), (385,325), (16,379), (125,379), (190,379),(250,379), (320,379), (385,379), (445,379), (554,379), (16,440), (60,440), (125,440), (186,440), (250, 440), (320,440), (385,440),(445, 440), (510,440), (554,440), (16, 498), (60,498), (125,498), (186,498), (249,498), (321,498), (385,498), (445,498), (510, 498), (554,498), (16, 554), (249,554), (321, 554), (554,554)]

font_name = pygame.font.match_font('arial')
gameDisplay = pygame.display.set_mode((dispWidth,dispHeight))
pygame.display.set_caption("Pacman")
pacmanImage = pygame.image.load("pacman.png").convert()
pacmanImage.set_colorkey(WHITE)
pacmanImage = pygame.transform.scale(pacmanImage, (30,30))
pacmanImageDown = pacmanImage
pacmanImageUp = pacmanImage
pacmanImageLeft = pacmanImage
pacmanImageUp = pygame.transform.rotate(pacmanImageUp, 90)
pacmanImageLeft = pygame.transform.rotate(pacmanImageLeft, 180)
pacmanImageDown = pygame.transform.rotate(pacmanImageDown, 270)
pacmanBackground = pygame.image.load("pacmanBackground.png").convert()
pacmanBackground = pygame.transform.scale(pacmanBackground, (600,600))
pacmanFood = pygame.image.load("pacmanFood.png").convert()
pacmanFood.set_colorkey(WHITE)
pacmanFood = pygame.transform.scale(pacmanFood, (8,8))

inkyImage = pygame.image.load("Inky.png").convert()
inkyImage.set_colorkey(WHITE)
inkyImage = pygame.transform.scale(inkyImage, (25,25))

pinkyImage = pygame.image.load("Pinky.png").convert()
pinkyImage.set_colorkey(WHITE)
pinkyImage = pygame.transform.scale(pinkyImage, (25,25))

blinkyImage = pygame.image.load("Blinky.png").convert()
blinkyImage.set_colorkey(WHITE)
blinkyImage = pygame.transform.scale(blinkyImage, (22,22))

clydeImage = pygame.image.load("Clyde.png").convert()
clydeImage.set_colorkey(WHITE)
clydeImage = pygame.transform.scale(clydeImage, (22,22))

fps = pygame.time.Clock()
crashed = False

pacmanXcoord, pacmanYcoord = 285, 325
inkyXcoord, inkyYcoord = 285, 250
pinkyXcoord, pinkyYcoord = 285, 250
blinkyXcoord, blinkyYcoord = 285, 250
clydeXcoord, clydeYcoord = 285, 250

def setUp():
	gameDisplay.blit(pacmanImage, [pacmanXcoord, pacmanYcoord])
	gameDisplay.blit(pacmanBackground, [0,0])

def pacmanMovement(x, y, image):
	gameDisplay.blit(image, [x,y])
	fps.tick(48)

def inkyMovement(x,y, inky):
	gameDisplay.blit(inky, [x,y])

def pinkyMovement(x,y, pinky):
	gameDisplay.blit(pinky, [x,y])

def blinkyMovement(x,y, blinky):
	gameDisplay.blit(blinky, [x,y])

def clydeMovement(x,y, clyde):
	gameDisplay.blit(clyde, [x,y])

def getRandomDirection():
	direction = randint(1,4)
	if direction == 1:
		return 'left'
	if direction == 2:
		return 'right'
	if direction == 3:
		return 'up'
	if direction == 4:
		return 'down'

def draw_score(display):
	font = pygame.font.Font(font_name, 16)
	score_surface = font.render("Score: "+ str(SCORE), True, WHITE)
	text_rect = score_surface.get_rect()
	text_rect.midtop = (530,330)
	display.blit(score_surface, text_rect)

def wallCheck(x,y,movement):
	'''checks if pacman has hit a the border of screen'''
	if x >= 555 and (movement == 'right' or movement == 'left'):
		return 'rightBoundX'
	elif x <= 15 and (movement == 'right' or movement == 'left'):
		return 'leftBoundX'
	elif y >= 555 and (movement == 'up' or movement == 'down'):
		return 'upperBoundY'
	elif y <= 15 and (movement == 'up' or movement == 'down'):
		return 'lowerBoundY'

def foodMaker(currentNode):
	'''makes a food for each decision point on the graph, handles eating food as well'''

	for index,tup in enumerate(foodList):
		if foodList[index] != 0:
			'''display all the food for pacman to eat'''
			gameDisplay.blit(pacmanFood, [tup[0], tup[1]])

		if (currentNode == (index + 1)) and (foodList[index] != 0):
			'''if pacman is at current node and theres food there, make food dissapear in future
			by removing its position from foodList, increment score'''
			foodList[index] = 0
			#SCORE += 100

def positionNodeCheck(x,y, ghostFlag):
	'''if current position is within threshold of a turning point, mark the current node'''
	for index,tup in enumerate(nodeList):
		if (x == tup[0]) and (y == tup[1]):
			currentNode = index + 1
			return currentNode

	if(x == 285 and y == 325):		#special value for starting pacman position
		return 100

	if(x == 285 and y == 250):		#special value of starting ghost position
		return 201

	if (x == 285 and y == 209) and ghostFlag == True:	#first node after ghosts exit box
		return 200

'''***********************************SETUP and GAME EVENTS START HERE****************'''
myNode = Node()
myNode.setNodeData(285,325,100,100)	#100 is pacman special start node

inkyNode = Node()
inkyNode.setNodeData(285,250,200,201)	#200 is ghosts special start node
					#201 is ghosts position when leaving box
pinkyNode = Node()
pinkyNode.setNodeData(285,250,200,201)

blinkyNode = Node()
blinkyNode.setNodeData(285,250,200,201)

clydeNode = Node()
clydeNode.setNodeData(285,250,200,201)

while not crashed:
	setUp()
	ghostFlag = None

	gameDisplay.blit(pacmanBackground, [0,0])
	draw_score(gameDisplay)

	whatNodeAmIAt = positionNodeCheck(pacmanXcoord, pacmanYcoord, ghostFlag)
	if(whatNodeAmIAt != myNode.getCurrentNode()):
		myNode.setCurrentNode(whatNodeAmIAt)

	foodMaker(myNode.getCurrentNode())

	if myNode.getNextNode() == 32 and MOVEMENT_FLAG == 'left':
		myNode.setCurrentNode(32)
		pacmanXcoord = 554
		pacmanYcoord = 265
		pacmanMovement(pacmanXcoord, pacmanYcoord, pacmanImageLeft)
	elif myNode.getNextNode() == 27 and MOVEMENT_FLAG == 'right':
		myNode.setCurrentNode(27)
		pacmanXcoord = 16
		pacmanYcoord = 265
		pacmanMovement(pacmanXcoord, pacmanYcoord, pacmanImage)


	'''So pacman continues motion between decision points'''
	if MOVEMENT_FLAG == 'left' and (wallFlag != 'leftBoundX'):
		if myNode.getNextNode() != myNode.getCurrentNode():
			pacmanXcoord -= 1
			pacmanMovement(pacmanXcoord, pacmanYcoord, pacmanImageLeft)
		else:
			pacmanMovement(pacmanXcoord, pacmanYcoord, pacmanImageLeft)
	elif MOVEMENT_FLAG == 'right' and (wallFlag != 'rightBoundX'):
		if myNode.getNextNode() != myNode.getCurrentNode():
			pacmanXcoord += 1
			pacmanMovement(pacmanXcoord, pacmanYcoord, pacmanImage)
		else:
			pacmanMovement(pacmanXcoord, pacmanYcoord, pacmanImage)
	elif MOVEMENT_FLAG == 'up' and (wallFlag != 'lowerBoundY'):
		if myNode.getNextNode() != myNode.getCurrentNode():
			pacmanYcoord -= 1
			pacmanMovement(pacmanXcoord, pacmanYcoord, pacmanImageUp)
		else:
			pacmanMovement(pacmanXcoord, pacmanYcoord, pacmanImageUp)
	elif MOVEMENT_FLAG == 'down' and (wallFlag != 'upperBoundY'):
		if myNode.getNextNode() != myNode.getCurrentNode():
			pacmanYcoord += 1
			pacmanMovement(pacmanXcoord, pacmanYcoord, pacmanImageDown)
		else:
			pacmanMovement(pacmanXcoord, pacmanYcoord, pacmanImageDown)
	else:
		pacmanMovement(pacmanXcoord, pacmanYcoord, pacmanImage)


	'''**************************GHOST SECTION*************************'''
	ghostFlag = True

	whatNodeIsInkyAt = positionNodeCheck(inkyXcoord, inkyYcoord, ghostFlag)
	if(whatNodeIsInkyAt != inkyNode.getCurrentNode()):
		inkyNode.setCurrentNode(whatNodeIsInkyAt)

	if inkyNode.getNextNode() != inkyNode.getCurrentNode():
		if inkyNode.getCurrentNode() == 201:
			INKY_FLAG = 'up'

		if INKY_FLAG == 'up':
			inkyYcoord -= 1
			inkyMovement(inkyXcoord, inkyYcoord, inkyImage)
		elif INKY_FLAG == 'down':
			inkyYcoord += 1
			inkyMovement(inkyXcoord, inkyYcoord, inkyImage)
		elif INKY_FLAG == 'left':
			inkyXcoord -= 1
			inkyMovement(inkyXcoord, inkyYcoord, inkyImage)
		elif INKY_FLAG == 'right':
			inkyXcoord += 1
			inkyMovement(inkyXcoord, inkyYcoord, inkyImage)
		else:
			inkyMovement(inkyXcoord, inkyYcoord, inkyImage)
	elif inkyNode.getNextNode() == inkyNode.getCurrentNode():
		INKY_FLAG = getRandomDirection()
		PINKY_START = True
		if inkyNode.nodeCheck(INKY_FLAG) != None:
			inkyNode.setNextNode(inkyNode.nodeCheck(INKY_FLAG))

	whatNodeIsPinkyAt = positionNodeCheck(pinkyXcoord, pinkyYcoord, ghostFlag)
	if(whatNodeIsPinkyAt != pinkyNode.getCurrentNode()):
		pinkyNode.setCurrentNode(whatNodeIsPinkyAt)

	if (pinkyNode.getNextNode() != pinkyNode.getCurrentNode()) and (PINKY_START != False):
		if pinkyNode.getCurrentNode() == 201:
			PINKY_FLAG = 'up'

		if PINKY_FLAG == 'up':
			pinkyYcoord -= 1
			pinkyMovement(pinkyXcoord, pinkyYcoord, pinkyImage)
		elif PINKY_FLAG == 'down':
			pinkyYcoord += 1
			pinkyMovement(pinkyXcoord, pinkyYcoord, pinkyImage)
		elif PINKY_FLAG == 'left':
			pinkyXcoord -= 1
			pinkyMovement(pinkyXcoord, pinkyYcoord, pinkyImage)
		elif PINKY_FLAG == 'right':
			pinkyXcoord += 1
			pinkyMovement(pinkyXcoord, pinkyYcoord, pinkyImage)
		else:
			pinkyMovement(pinkyXcoord, pinkyYcoord, pinkyImage)
	elif pinkyNode.getNextNode() == pinkyNode.getCurrentNode():
		PINKY_FLAG = getRandomDirection()
		BLINKY_START = True
		if pinkyNode.nodeCheck(PINKY_FLAG) != None:
			pinkyNode.setNextNode(pinkyNode.nodeCheck(PINKY_FLAG))

	whatNodeIsBlinkyAt = positionNodeCheck(blinkyXcoord, blinkyYcoord, ghostFlag)
	if(whatNodeIsBlinkyAt != blinkyNode.getCurrentNode()):
		blinkyNode.setCurrentNode(whatNodeIsBlinkyAt)

	if (blinkyNode.getNextNode() != blinkyNode.getCurrentNode()) and (BLINKY_START != False):
		if blinkyNode.getCurrentNode() == 201:
			BLINKY_FLAG = 'up'

		if BLINKY_FLAG == 'up':
			blinkyYcoord -= 1
			blinkyMovement(blinkyXcoord, blinkyYcoord, blinkyImage)
		elif BLINKY_FLAG == 'down':
			blinkyYcoord += 1
			blinkyMovement(blinkyXcoord, blinkyYcoord, blinkyImage)
		elif BLINKY_FLAG == 'left':
			blinkyXcoord -= 1
			blinkyMovement(blinkyXcoord, blinkyYcoord, blinkyImage)
		elif BLINKY_FLAG == 'right':
			blinkyXcoord += 1
			blinkyMovement(blinkyXcoord, blinkyYcoord, blinkyImage)
		else:
			blinkyMovement(blinkyXcoord, blinkyYcoord, blinkyImage)
	elif blinkyNode.getNextNode() == blinkyNode.getCurrentNode():
		BLINKY_FLAG = getRandomDirection()
		CLYDE_START = True
		if blinkyNode.nodeCheck(BLINKY_FLAG) != None:
			blinkyNode.setNextNode(blinkyNode.nodeCheck(BLINKY_FLAG))

	whatNodeIsClydeAt = positionNodeCheck(clydeXcoord, clydeYcoord, ghostFlag)
	if(whatNodeIsClydeAt != clydeNode.getCurrentNode()):
		clydeNode.setCurrentNode(whatNodeIsClydeAt)

	if (clydeNode.getNextNode() != clydeNode.getCurrentNode()) and (CLYDE_START != False):
		if clydeNode.getCurrentNode() == 201:
			CLYDE_FLAG = 'up'

		if CLYDE_FLAG == 'up':
			clydeYcoord -= 1
			clydeMovement(clydeXcoord, clydeYcoord, clydeImage)
		elif CLYDE_FLAG == 'down':
			clydeYcoord += 1
			clydeMovement(clydeXcoord, clydeYcoord, clydeImage)
		elif CLYDE_FLAG == 'left':
			clydeXcoord -= 1
			clydeMovement(clydeXcoord, clydeYcoord, clydeImage)
		elif CLYDE_FLAG == 'right':
			clydeXcoord += 1
			clydeMovement(clydeXcoord, clydeYcoord, clydeImage)
		else:
			clydeMovement(clydeXcoord, clydeYcoord, clydeImage)
	elif clydeNode.getNextNode() == clydeNode.getCurrentNode():
		CLYDE_FLAG = getRandomDirection()
		if clydeNode.nodeCheck(CLYDE_FLAG) != None:
			clydeNode.setNextNode(clydeNode.nodeCheck(CLYDE_FLAG))

	'''**********************************EVENT RESPONSE SECTION************************'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

		if event.type == pygame.KEYDOWN:
			''' use node checker from Node class to establish the next node to head to based on direction
			provided by user it will return the next node and set it using the mutator fuction '''

			if myNode.getCurrentNode() == myNode.getNextNode():
				if event.key == pygame.K_LEFT and (wallFlag != 'leftBoundX'):
					MOVEMENT_FLAG = 'left'
					if myNode.nodeCheck(MOVEMENT_FLAG) != None:	#if a node is returned
						myNode.setNextNode(myNode.nodeCheck(MOVEMENT_FLAG))
						pacmanXcoord -= 1
						pacmanMovement(pacmanXcoord, pacmanYcoord, pacmanImageLeft)
				if event.key == pygame.K_RIGHT and (wallFlag != 'rightBoundX'):
					MOVEMENT_FLAG = 'right'
					if myNode.nodeCheck(MOVEMENT_FLAG) != None:
						myNode.setNextNode(myNode.nodeCheck(MOVEMENT_FLAG))
						pacmanXcoord += 1
						pacmanMovement(pacmanXcoord, pacmanYcoord, pacmanImage)
				if event.key == pygame.K_UP and (wallFlag != 'lowerBoundY'):
					MOVEMENT_FLAG = 'up'
					if myNode.nodeCheck(MOVEMENT_FLAG) != None:
						myNode.setNextNode(myNode.nodeCheck(MOVEMENT_FLAG))
						pacmanYcoord -= 1
						pacmanMovement(pacmanXcoord, pacmanYcoord, pacmanImageUp)
				if event.key == pygame.K_DOWN and (wallFlag != 'upperBoundY'):
					MOVEMENT_FLAG = 'down'
					if myNode.nodeCheck(MOVEMENT_FLAG) != None:
						myNode.setNextNode(myNode.nodeCheck(MOVEMENT_FLAG))
						pacmanYcoord += 1
						pacmanMovement(pacmanXcoord, pacmanYcoord, pacmanImageDown)

	pygame.display.update()
	wallFlag = wallCheck(pacmanXcoord, pacmanYcoord, MOVEMENT_FLAG)
	#print("X is = ", pacmanXcoord, "Y is = ", pacmanYcoord)

pygame.quit()
quit()

import pygame
import os
import random
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
nodeList= [(16,16), (125,16), (249, 16), (321, 16), (445,16), (554,16), (16,89), (125,89), (190,89), (249,89), (321,89), (385,89), (445,89), (554,89), (16,150), (125,150), (190, 149), (254, 149), (320,149), (385,149), (445,150), (554,150), (190, 209), (254, 209), (320,209), (385,209), (16,265), (125,265), (190,265), (385,265), (445,265), (554,265), (190, 325), (385,325), (16,379), (125,379), (190,379), (250,379), (320,379), (385,379), (445,379), (554,379), (16,440), (60,440), (125,440), (186,440), (250, 440), (320,440), (385,440), (445, 440), (510,440), (554,440), (16, 498), (60,498), (125,498), (186,498), (249,498), (321,498), (385,498), (445,498), (510, 498), (554,498), (16, 554), (249,554), (321, 554), (554,554)]
#list of all the decision points in the graph

gameDisplay = pygame.display.set_mode((dispWidth,dispHeight))
pygame.display.set_caption("Pacman")
pacmanImage = pygame.image.load("pacman.png").convert()
pacmanImage.set_colorkey(WHITE)

pacmanImage = pygame.transform.scale(pacmanImage, (30,30))
pacmanBackground = pygame.image.load("pacmanBackground.png").convert()
pacmanBackground = pygame.transform.scale(pacmanBackground, (600,600))

fps = pygame.time.Clock()
crashed = False
pacmanXcoord, pacmanYcoord = 285, 325
CURRENT_NODE = 0


def setUp():
	gameDisplay.blit(pacmanImage, [pacmanXcoord, pacmanYcoord])
	gameDisplay.blit(pacmanBackground, [0,0])

def pacmanMovement(x, y):
	gameDisplay.blit(pacmanImage, [x,y])
	fps.tick(30)

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

def nodeMaker():
	'''makes a node for each decision point on the graph'''
	mapNodes = [Node() for i in range(0,66)]
	for index,tup in enumerate(nodeList):
		mapNodes[index].setNodeData(tup[0], tup[1], 0,0)
		#print('Node number =', index)
		mapNodes[index].printNode()

def positionNodeCheck(x,y):
	'''if current position is within threshold of a turning point, mark the current node'''
	for index,tup in enumerate(nodeList):
		if (x == tup[0]) and (y == tup[1]):
			currentNode = index + 1
			print('we are at this node ', currentNode)
			return currentNode

	if(x == 285 and y == 325):		#special value for starting position
		return 100

nodeMaker()

myNode = Node()
myNode.setNodeData(285,325,100,100)

while not crashed:
	setUp()

	gameDisplay.blit(pacmanBackground, [0,0])

	whatNodeAmIAt = positionNodeCheck(pacmanXcoord, pacmanYcoord)
	if(whatNodeAmIAt != myNode.getCurrentNode()):
		myNode.setCurrentNode(whatNodeAmIAt)

	if MOVEMENT_FLAG == 'left' and (wallFlag != 'leftBoundX'):
		print('left')
		print('myNode.getNext Node is = ', myNode.getNextNode(), 'my node.GetCurrentNode = ',myNode.getCurrentNode())
		if myNode.getNextNode() != myNode.getCurrentNode():
			pacmanXcoord -= 1
			pacmanMovement(pacmanXcoord, pacmanYcoord)
		else:
			pacmanMovement(pacmanXcoord, pacmanYcoord)
	elif MOVEMENT_FLAG == 'right' and (wallFlag != 'rightBoundX'):
		print('right')
		print('myNode.getNext Node is = ', myNode.getNextNode(), 'my node.GetCurrentNode = ',myNode.getCurrentNode())
		if myNode.getNextNode() != myNode.getCurrentNode():
			pacmanXcoord += 1
			pacmanMovement(pacmanXcoord, pacmanYcoord)
		else:
			pacmanMovement(pacmanXcoord, pacmanYcoord)
	elif MOVEMENT_FLAG == 'up' and (wallFlag != 'lowerBoundY'):
		print('up')
		print('myNode.getNext Node is = ', myNode.getNextNode(), 'my node.GetCurrentNode = ',myNode.getCurrentNode())
		if myNode.getNextNode() != myNode.getCurrentNode():
			pacmanYcoord -= 1
			pacmanMovement(pacmanXcoord, pacmanYcoord)
		else:
			pacmanMovement(pacmanXcoord, pacmanYcoord)
	elif MOVEMENT_FLAG == 'down' and (wallFlag != 'upperBoundY'):
		print('down')
		print('myNode.getNext Node is = ', myNode.getNextNode(), 'my node.GetCurrentNode = ',myNode.getCurrentNode())
		if myNode.getNextNode() != myNode.getCurrentNode():
			pacmanYcoord += 1
			pacmanMovement(pacmanXcoord, pacmanYcoord)
		else:
			pacmanMovement(pacmanXcoord, pacmanYcoord)
	else:
		pacmanMovement(pacmanXcoord, pacmanYcoord)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

		if event.type == pygame.KEYDOWN:
			''' use node checker from Node class to establish the next node to head to based on direction
			provided by user it will return the next node and set it using the mutator fuction '''

			if myNode.getCurrentNode() == myNode.getNextNode():
				if event.key == pygame.K_LEFT and (wallFlag != 'leftBoundX'):
					MOVEMENT_FLAG = 'left'
					myNode.setNextNode(myNode.nodeCheck(MOVEMENT_FLAG))
					pacmanXcoord -= 1
					pacmanMovement(pacmanXcoord, pacmanYcoord)
				if event.key == pygame.K_RIGHT and (wallFlag != 'rightBoundX'):
					MOVEMENT_FLAG = 'right'
					myNode.setNextNode(myNode.nodeCheck(MOVEMENT_FLAG))
					pacmanXcoord += 1
					pacmanMovement(pacmanXcoord, pacmanYcoord)
				if event.key == pygame.K_UP and (wallFlag != 'lowerBoundY'):
					MOVEMENT_FLAG = 'up'
					myNode.setNextNode(myNode.nodeCheck(MOVEMENT_FLAG))
					pacmanYcoord -= 1
					pacmanMovement(pacmanXcoord, pacmanYcoord)
				if event.key == pygame.K_DOWN and (wallFlag != 'upperBoundY'):
					MOVEMENT_FLAG = 'down'
					myNode.setNextNode(myNode.nodeCheck(MOVEMENT_FLAG))
					pacmanYcoord += 1
					pacmanMovement(pacmanXcoord, pacmanYcoord)

	pygame.display.update()
	wallFlag = wallCheck(pacmanXcoord, pacmanYcoord, MOVEMENT_FLAG)
	#print("X is = ", pacmanXcoord, "Y is = ", pacmanYcoord)

pygame.quit()
quit()

'''node class used in pacman, each node corresponds to a
	different possible decision point on the map where pacman
	and the ghosts could turn'''

class Node:
	def __init__(self):
		self.x = None
		self.y = None
		self.nextNode = None
		self.currentNode = None

	def setNodeData(self, x, y, next, curr):
		self.x = x
		self.y = y
		self.nextNode = next
		self.currentNode = curr

	def printNode(self):
		print("X coordinate of node is = " + str(self.x) + "\nY coordinate of node is = " + str(self.y) + "\nNext node is " + str(self.nextNode) + "\nCurrent node is = " + str(self.currentNode))

	def getCurrentNode(self):
		return self.currentNode

	def setCurrentNode(self, nodeNum):
		self.currentNode = nodeNum

	def getNextNode(self):
		return self.nextNode

	def setNextNode(self, next):
		self.nextNode = next

	def nodeCheck(self, dir):
		print('MOVEMENT_FLAG = ', dir)
		print('Current Node = ', self.currentNode)
		print('Next node = ', self.nextNode)

		if self.currentNode == 0:
			return 34
		elif self.currentNode == 1:
			if dir == 'down':
				return 7
			if dir == 'right':
				return 2
		elif self.currentNode == 2:
			if dir == 'left':
				return 1
			if dir == 'right':
				return 3
			if dir == 'down':
				return 8
		elif self.currentNode == 3:
			if dir == 'left':
				return 2
			if dir == 'right':
				return 4
			if dir == 'down':
				return 10
		elif self.currentNode == 4:
			if dir == 'left':
				return 3
			if dir == 'right':
				return 5
			if dir == 'down':
				return 11
		elif self.currentNode == 5:
			if dir == 'left':
				return 4
			if dir == 'right':
				return 6
			if dir == 'down':
				return 13
		elif self.currentNode == 6:
			if dir == 'left':
				return 5
			if dir == 'down':
				return 14
		elif self.currentNode == 7:
			if dir == 'up':
				return 1
			if dir == 'down':
				return 15
			if dir == 'right':
				return 8
		elif self.currentNode == 8:
			if dir == 'up':
				return 2
			if dir == 'down':
				return 16
			if dir == 'left':
				return 7
			if dir == 'right':
				return 9
		elif self.currentNode == 9:
			if dir == 'left':
				return 8
			if dir == 'right':
				return 10
			if dir == 'down':
				return 17
		elif self.currentNode == 10:
			if dir == 'left':
				return 9
			if dir == 'right':
				return 11
			if dir == 'up':
				return 3
		elif self.currentNode == 11:
			if dir == 'left':
				return 10
			if dir == 'right':
				return 12
			if dir == 'up':
				return 4
		elif self.currentNode == 12:
			if dir == 'left':
				return 11
			if dir == 'right':
				return 13
			if dir == 'down':
				return 20
		elif self.currentNode == 13:
			if dir == 'left':
				return 12
			if dir == 'right':
				return 14
			if dir == 'up':
				return 5
			if dir == 'down':
				return 21
		elif self.currentNode == 14:
			if dir == 'left':
				return 13
			if dir == 'up':
				return 6
			if dir == 'down':
				return 22
		elif self.currentNode == 15:
			if dir == 'right':
				return 16
			if dir == 'up':
				return 7
		elif self.currentNode == 16:
			if dir == 'left':
				return 15
			if dir == 'up':
				return 8
			if dir == 'down':
				return 28
		elif self.currentNode == 17:
			if dir == 'up':
				return 9
			if dir == 'right':
				return 18
		elif self.currentNode == 18:
			if dir == 'left':
				return 17
			if dir == 'down':
				return 24
		elif self.currentNode == 19:
			if dir == 'right':
				return 20
			if dir == 'down':
				return 25
		elif self.currentNode == 20:
			if dir == 'left':
				return 19
			if dir == 'up':
				return 12
		elif self.currentNode == 21:
			if dir == 'up':
				return 13
			if dir == 'right':
				return 22
			if dir == 'down':
				return 31
		elif self.currentNode == 22:
			if dir == 'left':
				return 21
			if dir == 'up':
				return 14
		elif self.currentNode == 23:
			if dir == 'down':
				return 29
			if dir == 'right':
				return 24
		elif self.currentNode == 24:
			if dir == 'left':
				return 23
			if dir == 'right':
				return 25
			if dir == 'up':
				return 18
		elif self.currentNode == 25:
			if dir == 'left':
				return 24
			if dir == 'right':
				return 26
			if dir == 'up':
				return 19
		elif self.currentNode == 26:
			if dir == 'left':
				return 25
			if dir == 'down':
				return 30
		elif self.currentNode == 27:
			if dir == 'left':
				return 32
			if dir == 'right':
				return 28
		elif self.currentNode == 28:
			if dir == 'left':
				return 27
			if dir == 'right':
				return 29
			if dir == 'up':
				return 16
			if dir == 'down':
				return 36
		elif self.currentNode == 29:
			if dir == 'left':
				return 28
			if dir == 'up':
				return 23
			if dir == 'down':
				return 33
		elif self.currentNode == 30:
			if dir == 'right':
				return 31
			if dir == 'up':
				return 26
			if dir == 'down':
				return 34
		elif self.currentNode == 31:
			if dir == 'left':
				return 30
			if dir == 'right':
				return 32
			if dir == 'up':
				return 21
			if dir == 'down':
				return 41
		elif self.currentNode == 32:
			if dir == 'right':
				return 27
			if dir == 'left':
				return 31
		elif self.currentNode == 33:
			if dir == 'right':
				return 34
			if dir == 'up':
				return 29
			if dir == 'down':
				return 37
		elif self.currentNode == 100:
			if dir == 'left':
				return 33
			if dir == 'right':
				return 34
		elif self.currentNode == 34:
			if dir == 'left':
				return 33
			if dir == 'up':
				return 30
			if dir == 'down':
				return 40
		elif self.currentNode == 35:
			if dir == 'right':
				return 36
			if dir == 'down':
				return 43
		elif self.currentNode == 36:
			if dir == 'left':
				return 35
			if dir == 'right':
				return 37
			if dir == 'up':
				return 28
			if dir == 'down':
				return 45
		elif self.currentNode == 37:
			if dir == 'left':
				return 36
			if dir == 'right':
				return 38
			if dir == 'up':
				return 33
		elif self.currentNode == 38:
			if dir == 'left':
				return 27
			if dir == 'down':
				return 47
		elif self.currentNode == 39:
			if dir == 'right':
				return 40
			if dir == 'down':
				return 48
		elif self.currentNode == 40:
			if dir == 'left':
				return 39
			if dir == 'right':
				return 41
			if dir == 'up':
				return 34
		elif self.currentNode == 41:
			if dir == 'left':
				return 40
			if dir == 'right':
				return 42
			if dir == 'up':
				return 31
			if dir == 'down':
				return 50
		elif self.currentNode == 42:
			if dir == 'left':
				return 41
			if dir == 'down':
				return 52
		elif self.currentNode == 43:
			if dir == 'right':
				return 44
			if dir == 'up':
				return 35
		elif self.currentNode == 44:
			if dir == 'left':
				return 43
			if dir == 'down':
				return 54
		elif self.currentNode == 45:
			if dir == 'right':
				return 46
			if dir == 'up':
				return 36
			if dir == 'down':
				return 55
		elif self.currentNode == 46:
			if dir == 'left':
				return 45
			if dir == 'right':
				return 47
			if dir == 'down':
				return 56
		elif self.currentNode == 47:
			if dir == 'left':
				return 46
			if dir == 'right':
				return 48
			if dir == 'up':
				return 38
		elif self.currentNode == 48:
			if dir == 'left':
				return 47
			if dir == 'right':
				return 49
			if dir == 'up':
				return 39
		elif self.currentNode == 49:
			if dir == 'left':
				return 48
			if dir == 'right':
				return 50
			if dir == 'down':
				return 59
		elif self.currentNode == 50:
			if dir == 'left':
				return 49
			if dir == 'up':
				return 41
			if dir == 'down':
				return 60
		elif self.currentNode == 51:
			if dir == 'right':
				return 52
			if dir == 'down':
				return 61
		elif self.currentNode == 52:
			if dir == 'left':
				return 51
			if dir == 'up':
				return 42
		elif self.currentNode == 53:
			if dir == 'right':
				return 54
			if dir == 'down':
				return 63
		elif self.currentNode == 54:
			if dir == 'right':
				return 55
			if dir == 'left':
				return 53
			if dir == 'up':
				return 44
		elif self.currentNode == 55:
			if dir == 'left':
				return 54
			if dir == 'up':
				return 45
		elif self.currentNode == 56:
			if dir == 'right':
				return 57
			if dir == 'up':
				return 46
		elif self.currentNode == 57:
			if dir == 'left':
				return 56
			if dir == 'down':
				return 64
		elif self.currentNode == 58:
			if dir == 'right':
				return 59
			if dir == 'down':
				return 65
		elif self.currentNode == 59:
			if dir == 'left':
				return 58
			if dir == 'up':
				return 48
		elif self.currentNode == 60:
			if dir == 'right':
				return 61
			if dir == 'up':
				return 50
		elif self.currentNode == 61:
			if dir == 'left':
				return 60
			if dir == 'right':
				return 62
			if dir == 'up':
				return 51
		elif self.currentNode == 62:
			if dir == 'left':
				return 61
			if dir == 'down':
				return 66
		elif self.currentNode == 63:
			if dir == 'right':
				return 64
			if dir == 'up':
				return 53
		elif self.currentNode == 64:
			if dir == 'left':
				return 63
			if dir == 'right':
				return 64
			if dir == 'up':
				return 57
		elif self.currentNode == 65:
			if dir == 'left':
				return 64
			if dir == 'right':
				return 66
			if dir == 'up':
				return 58
		elif self.currentNode == 66:
			if dir == 'left':
				return 65
			if dir == 'up':
				return 62

if __name__ == "__main__":
	Node1 = Node()
	Node1.setNodeData(16,16,66,0)
	Node1.printNode()

	Node2 = Node()
	Node2.setNodeData(10,10,0,0)
	Node2.printNode()

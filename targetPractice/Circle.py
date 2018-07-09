'''class used to draw circles for targetPractice.py
contains all the necessary methods for one circle'''
import random

class Circle():
	def __init__(self):
		self.centerX = 400
		self.centerY = 300

	def getStartingCoords(self):
		'''returns the starting coordinates of a newly generated circle'''
		x = random.randint(1,800)
		y = 0
		return x,y

	def slopeEquation(self,x,y):
		'''return slope of the line that the cirlce is traveling on
		based on m = (y_2 - y_1)/(x_2 - x_1)'''
		if (self.centerX - x) == 0:
			return 0
		else:
			slope = (self.centerY - y) / (self.centerX - x)
			return slope

	def getYIntercept(self,x,y,slope):
		'''returns the y-intercept, based off y=mx+b where b = (mx-y)*-1'''
		b = ((slope * x) - y) * -1
		return b

	def getAdjustedXY(self,x,y,m,b):
		'''returns the adjusted x,y of the circle after it moves
		once again based off of y=mx+b'''
		y += 5
		if m == 0:
			return x,y
		else:
			x = (y - b) / m
			return x,y

if __name__ == "__main__":
	myCircle = Circle()
	x,y = myCircle.getStartingCoords()
	print("This is x = ", x, ", y = ", y)
	slope = myCircle.slopeEquation(x,y)
	print("This is slope = ", slope)
	y_intercept = myCircle.getYIntercept(x,y,slope)
	print("This is the y-intercept = ", y_intercept)
	x,y = myCircle.getAdjustedXY(x,y, slope, y_intercept)
	print("after adjusting the x and y coordinates they are x = ", x, ", y = ", y)

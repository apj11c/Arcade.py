# Game choosing screen 

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


class MainScreen(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.setup()

	def setup(self):
		self.setWindowTitle("PyArcade")	

		self.label = QLabel("Welcome to PyArcade! Please select a game.")
		self.label.setAlignment(Qt.AlignCenter)		

		# Button initializations/placements
		self.gameBtn1 = QPushButton("Blackjack", self)
		self.gameBtn1.clicked.connect(self.playBlackjack)

		self.gameBtn2 = QPushButton("Roulette", self)
		self.gameBtn2.clicked.connect(self.playRoulette)
	
		self.gameBtn3 = QPushButton("Millipede", self)
		self.gameBtn3.clicked.connect(self.playMillipede)
		
		self.gameBtn4 = QPushButton("Pac Man", self)
		self.gameBtn4.clicked.connect(self.playPacMan)

		self.layout = QVBoxLayout()

		self.layout.addWidget(self.label)
		self.layout.addWidget(self.gameBtn1)
		self.layout.addWidget(self.gameBtn2)
		self.layout.addWidget(self.gameBtn3)
		self.layout.addWidget(self.gameBtn4)
		self.setLayout(self.layout)

		self.show()
	
	def playBlackjack(self):
		# Insert function call to blackjack gameplay here
		print("Run blackjack gameplay code")

	def playRoulette(self):
		# Insert function call to roulette gameplay here
		print("Run roulette gameplay code")

	def playMillipede(self):
		# Insert function call to millipede gameplay here
		print("Run millipede gameplay code")

	def playPacMan(self):
		# Insert function call to pac man gameplay here
		print("Run pac man gameplay code")


if __name__ == "__main__":
	app = QApplication(sys.argv)
	main_window = MainScreen()
	main_window.show()
	app.exec_()


# Game choosing screen 

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,\
							QVBoxLayout, QLabel, QMessageBox
from PyQt5.QtCore import Qt

import sys
import roulette
import blackjack
import Milapede
import SpaceAdventure
import time


class MainScreen(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.setup()

	def setup(self):
		self.setWindowTitle("PyArcade")	

		self.tpCount = 0

		self.label = QLabel("Welcome to PyArcade! Please select a game.")
		self.label.setAlignment(Qt.AlignCenter)		

		# Button initializations/placements
		self.gameBtn1 = QPushButton("Roulette", self)
		self.gameBtn1.clicked.connect(self.playRoulette)
	
		self.gameBtn2 = QPushButton("Blackjack", self)
		self.gameBtn2.clicked.connect(self.playBlackjack)

		self.gameBtn3 = QPushButton("Millipede", self)
		self.gameBtn3.clicked.connect(self.playMilapede)
		
		self.gameBtn4 = QPushButton("Space Adventures", self)
		self.gameBtn4.clicked.connect(self.playSpaceAdventures)

		self.gameBtn5 = QPushButton("Target Practice", self)
		self.gameBtn5.clicked.connect(self.playTargetPractice)

		self.gameBtn6 = QPushButton("Pac Man", self)
		self.gameBtn6.clicked.connect(self.playPacMan)

		self.layout = QVBoxLayout()

		self.layout.addWidget(self.label)
		self.layout.addWidget(self.gameBtn1)
		self.layout.addWidget(self.gameBtn2)
		self.layout.addWidget(self.gameBtn3)
		self.layout.addWidget(self.gameBtn4)
		self.layout.addWidget(self.gameBtn5)
		self.layout.addWidget(self.gameBtn6)
		self.setLayout(self.layout)

		self.show()

	def playBlackjack(self):
		self.blackjackWindow = blackjack.BlackjackTable()

	def playRoulette(self):
		self.rouletteWindow = roulette.RouletteTable()

	def playMilapede(self):
		Milapede.main()

	def playSpaceAdventures(self):
		SpaceAdventure.main()

	def playTargetPractice(self):
		import targetPractice
		del sys.modules['targetPractice']

	def playPacMan(self):
		import pacman
		del sys.modules['pacman']

class QuitMessage(QtWidgets.QMessageBox):
	def __init__(self):
		QtWidgets.QMessageBox.__init__(self)
		self.setText("Quit game?")
		self.addButton(self.No)
		self.addButton(self.Yes)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	main_window = MainScreen()
	main_window.show()
	app.exec_()


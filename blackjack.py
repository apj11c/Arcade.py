from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import mainScreen
import sys
import random

class BlackjackTable(QtWidgets.QMainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		self.setup()

	def setup(self):
		self.setWindowTitle('Blackjack')
		self.setGeometry(100, 100, 1100, 550)
		self.setFixedSize(self.size())
		self.setAutoFillBackground(True)

		self.image = DisplayImage(self)
		self.setCentralWidget(self.image)

		self.yourCards = []; self.dealerCards = []
		self.pImages = []; self.dImages = []
		self.wins = 0; self.losses = 0; self.ties = 0
		self.gameNotOver = True
		self.userStay = False; self.dealerStay = False

		self.combo = QtWidgets.QComboBox(self)
		self.combo.addItem('Regular')
		self.combo.addItem('Advanced')
		self.combo.move(1000, 5)

		self.prompt = QtWidgets.QLabel(self)
		self.prompt.setText("Please select a mode:")
		self.prompt.setStyleSheet("color: lightgreen")
		self.prompt.setFixedWidth(150)
		self.prompt.move(850, 5)

		self.yourCardsLabel = QtWidgets.QLabel(self)
		self.yourCardsLabel.setText("Your cards:")
		self.yourCardsLabel.setStyleSheet('color: lightgreen')
		self.yourCardsLabel.setFixedWidth(85)
		self.yourCardsLabel.move(5, 5)
		self.yourCardsLabel.hide()

		self.dealerCardsLabel = QtWidgets.QLabel(self)
		self.dealerCardsLabel.setText("Dealer's cards:")
		self.dealerCardsLabel.setStyleSheet('color: lightgreen')
		self.dealerCardsLabel.setFixedWidth(110)
		self.dealerCardsLabel.move(5, 250)
		self.dealerCardsLabel.hide()

		self.startGameBtn = QtWidgets.QPushButton("Start Game", self)
		self.startGameBtn.clicked.connect(self.startGame)
		self.startGameBtn.move(1000, 35)

		self.hitBtn = QtWidgets.QPushButton("Hit", self)
		self.hitBtn.clicked.connect(self.hit)
		self.hitBtn.move(5, 520)
		self.hitBtn.hide()
		self.stayBtn = QtWidgets.QPushButton("Stay", self)
		self.stayBtn.clicked.connect(self.stay)
		self.stayBtn.move(95, 520)
		self.stayBtn.hide()

		self.continueBtn = QtWidgets.QPushButton("Yes", self)
		self.continueBtn.clicked.connect(self.startGame)
		self.continueBtn.move(5, 520)
		self.continueBtn.hide()
		self.quitBtn = QtWidgets.QPushButton("No", self)
		self.quitBtn.clicked.connect(self.gameOver)
		self.quitBtn.move(95, 520)
		self.quitBtn.hide()

		self.continueLabel = QtWidgets.QLabel(self)
		self.continueLabel.setText("Continue playing?")
		self.continueLabel.setFixedWidth(120)
		self.continueLabel.setStyleSheet('color: lightgreen')
		self.continueLabel.move(5, 500)
		self.continueLabel.hide()

		self.yourScoreLabel = QtWidgets.QLabel(self)
		self.yourScoreLabel.setFixedWidth(100)
		self.yourScoreLabel.setStyleSheet('color: lightgreen')
		self.yourScoreLabel.move(400, 250)
		self.yourScoreLabel.hide()

		self.dealerScoreLabel = QtWidgets.QLabel(self)
		self.dealerScoreLabel.setFixedWidth(150)
		self.dealerScoreLabel.setStyleSheet('color: lightgreen')
		self.dealerScoreLabel.move(500, 250)

		self.resultLabel = QtWidgets.QLabel(self)
		self.resultLabel.setFixedWidth(70)
		self.resultLabel.move(650, 250)

		self.winLabel = QtWidgets.QLabel(self)
		self.winLabel.setFixedWidth(100)
		self.winLabel.setStyleSheet('color: lightgreen')
		self.winLabel.move(1020, 450)
		self.winLabel.hide()

		self.lossLabel = QtWidgets.QLabel(self)
		self.lossLabel.setFixedWidth(100)
		self.lossLabel.setStyleSheet('color: lightgreen')
		self.lossLabel.move(1020, 480)
		self.lossLabel.hide()

		self.tieLabel = QtWidgets.QLabel(self)
		self.tieLabel.setFixedWidth(100)
		self.tieLabel.setStyleSheet('color: lightgreen')
		self.tieLabel.move(1020, 510)
		self.tieLabel.hide()

		font = QtGui.QFont()
		font.setPointSize(72)
		self.gameOverLabel = QtWidgets.QLabel(self)
		self.gameOverLabel.setText("GAME OVER")
		self.gameOverLabel.setFixedWidth(500)
		self.gameOverLabel.setFixedHeight(350)
		self.gameOverLabel.setFont(font)
		self.gameOverLabel.setStyleSheet('color: red')
		self.gameOverLabel.move(360, 80)
		self.gameOverLabel.hide()
	
		exitAction = QtWidgets.QAction('Exit', self)
		exitAction.triggered.connect(QtWidgets.qApp.quit)

		if self.score(self.dealerCards) > 21:
			self.dealerStay = True

		self.show()

	def startGame(self):
		self.startGameBtn.setEnabled(False)
		self.combo.setEnabled(False)
		self.yourCardsLabel.show()
		self.dealerCardsLabel.show()
		self.hitBtn.show()
		self.stayBtn.show()
		self.continueBtn.hide()
		self.continueLabel.hide()
		self.yourScoreLabel.hide()
		self.dealerScoreLabel.hide()
		self.quitBtn.hide()
		self.resultLabel.hide()
		
		self.userStay = False; self.dealerStay = False
	
		for i in self.pImages:
			i.hide()
	
		for i in self.dImages:
			i.hide()

		self.pImages = []
		self.dImages = []

		self.pIndex = 2
		self.dIndex = 2
		self.pOffset = self.dOffset = 225
		self.deck, self.dealerCards, self.yourCards = self.deal()		
		self.pImages.append(self.displayCard(self.yourCards[0], 5, 60))
		self.pImages.append(self.displayCard(self.yourCards[1], 115, 60))
		self.dImages.append(self.displayCard("red_back", 5, 300))
		self.dImages.append(self.displayCard("red_back", 115, 300))

	def hit(self):
		self.yourCards.append(self.deck[random.randint(0, len(self.deck) - 1)])
		self.deck.remove(self.yourCards[self.pIndex])
		self.pImages.append(self.displayCard(self.yourCards[self.pIndex],
											 self.pOffset, 60))
		self.pOffset += 110
		self.pIndex += 1
	
		if self.combo.currentText() == "Regular":
			self.dealerStay = True if random.randint(0, 1) == 0 else False	
		else:	
			self.dealerStay = True if self.score(self.dealerCards) > 16 \
									  else False

		if self.score(self.dealerCards) > 21:
			self.dealerStay = True

		if not self.dealerStay:
			self.dealerCards.append(self.deck[random.randint(0,
											  len(self.deck) - 1)])
			self.deck.remove(self.dealerCards[self.dIndex])
			self.dImages.append(self.displayCard("red_back", self.dOffset, 300))
			self.dOffset += 110
			self.dIndex += 1

		if self.score(self.yourCards) > 21:
			self.stay()

	def stay(self):
		self.userStay = True
		self.hitBtn.hide()
		self.stayBtn.hide()
		self.continueLabel.show()
		self.continueBtn.show()
		self.quitBtn.show()

		if self.combo.currentText() == "Regular":
			self.dealerStay = True if random.randint(0, 1) == 0 else False	
		else:	
			self.dealerStay = True if self.score(self.dealerCards) > 16 \
									  else False

		while not self.dealerStay and self.score(self.dealerCards) <= 21:
			self.dealerCards.append(self.deck[random.randint(0,
								   (len(self.deck) - 1))])
			self.deck.remove(self.dealerCards[self.dIndex])
			self.dImages.append(self.displayCard("red_back", self.dOffset, 300))
			self.dOffset += 110
			self.dIndex += 1

			if self.combo.currentText() == "Regular":
				self.dealerStay = True if random.randint(0, 1) == 0 else False	
			else:	
				self.dealerStay = True if self.score(self.dealerCards) > 16 \
									   else False

		self.yourScoreLabel.setText("Your score: " +	
								 str(self.score(self.yourCards)))
		self.yourScoreLabel.show()
		self.dealerScoreLabel.setText("Dealer's score: " +	
								 	   str(self.score(self.dealerCards)))
		self.dealerScoreLabel.show()

		n = 0
		for i in self.dealerCards:
			self.dImages.append(self.displayCard(i, 5 + (110 * n), 300))
			n += 1

		won = False
		lost = False
		if self.score(self.yourCards) > 21:
			self.losses += 1
			lost = True
		elif self.score(self.dealerCards) > 21:
			self.wins += 1
			won = True
		elif self.score(self.yourCards) > self.score(self.dealerCards):
			self.wins += 1
			won = True
		elif self.score(self.yourCards) < self.score(self.dealerCards):
			self.losses += 1
			lost = True
		else:
			self.ties += 1
			self.resultLabel.setText("You tied!")
			self.resultLabel.setStyleSheet('color: lightblue')

		if lost:
			self.resultLabel.setText("You lost!")
			self.resultLabel.setStyleSheet('color: red')
		elif won:
			self.resultLabel.setText("You won!")
			self.resultLabel.setStyleSheet('color: lightgreen')

		self.resultLabel.show()

		self.winLabel.setText("Wins:\t" + str(self.wins))
		self.winLabel.show()
		self.lossLabel.setText("Losses:\t" + str(self.losses))
		self.lossLabel.show()
		self.tieLabel.setText("Ties:\t" + str(self.ties))
		self.tieLabel.show()

	def gameOver(self):
		self.gameNotOver = False
		self.hitBtn.hide()
		self.stayBtn.hide()
		self.yourScoreLabel.hide()
		self.dealerScoreLabel.hide()
		self.resultLabel.hide()
		self.continueBtn.setEnabled(False)
		self.quitBtn.setEnabled(False)
		self.gameOverLabel.show()

	def closeEvent(self, event):
		if self.gameNotOver:
			popUp = mainScreen.QuitMessage()
			reply = popUp.exec_()
			if reply == QtWidgets.QMessageBox.Yes:
				event.accept()
			else:
				event.ignore()
		else:
			event.accept()

	def displayCard(self, cardName, xPos, yPos):
		card = QLabel(self)
		cardPixmap = QPixmap()
		cardPixmap = QtGui.QPixmap("Images/Cards/" + cardName + ".png")
		card.resize(100, 155)
		card.setPixmap(cardPixmap.scaled(card.size(),
					   QtCore.Qt.IgnoreAspectRatio))
		card.move(xPos, yPos)
		card.show()

		return card

	def score(self, cards):
		sum = 0
		aceCount = 0
		for i in cards:
			if i[0] == "A":
				aceCount += 1
			elif str.isdigit(i[0]):
				if i[0] == "1":
					sum += 10
				else:
					sum += int(i[0])
			else:
				sum += 10
		
		for i in range(aceCount):
			sum += 1
		
		for i in range(aceCount):
			if sum + 10 <= 21:
				sum += 10

		return sum

	def deal(self):
		deck = ["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S",
				"JS", "QS", "KS", "AH", "2H", "3H", "4H", "5H", "6H", "7H",
				"8H", "9H", "10H", "JH", "QH", "KH", "AC", "2C", "3C", "4C",
				"5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AD",
				"2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD",
				"QD", "KD"]

		dCards = []; pCards = []
		pCards.append(deck[random.randint(0, len(deck) - 1)])
		deck.remove(pCards[0])
		dCards.append(deck[random.randint(0, len(deck) - 1)])
		deck.remove(dCards[0])
		pCards.append(deck[random.randint(0, len(deck) - 1)])
		deck.remove(pCards[1])
		dCards.append(deck[random.randint(0, len(deck) - 1)])
		deck.remove(dCards[1])

		return deck, dCards, pCards


class DisplayImage(QtWidgets.QWidget):
	def __init__(self, parent):
		QtWidgets.QWidget.__init__(self, parent)
		self.setup()

	def setup(self):
		self.image = QtWidgets.QLabel(self)
		pixmap = QtGui.QPixmap("Images/casinoTable.jpg")
		self.image.resize(1100, 550)
		self.image.setPixmap(pixmap.scaled(self.image.size(),
							 QtCore.Qt.IgnoreAspectRatio))
		self.image.move(0, 0)		

"""
class QuitMessage(QtWidgets.QMessageBox):
	def __init__(self):
		QtWidgets.QMessageBox.__init__(self)
		self.setText("Quit game?")
		self.addButton(self.No)
		self.addButton(self.Yes)
"""

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	main_window = BlackjackTable()
	app.exec_()

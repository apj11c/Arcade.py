from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import mainScreen
import random
import sys
import time

class RouletteTable(QtWidgets.QMainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		self.setup()

	def setup(self):
		self.setWindowTitle('Roulette')
		self.setGeometry(200, 200, 700, 350)
		self.setFixedSize(self.size())
		self.setAutoFillBackground(True)

		self.image = DisplayImage(self)
		self.setCentralWidget(self.image)
		
		self.cb = QtWidgets.QLabel(self)
		self.cb.setText("Current Balance:")
		self.cb.move(5, 0)
	
		self.money = 10000
		self.gameNotOver = True

		self.balance = QtWidgets.QLineEdit(self)
		self.balance.setFixedWidth(95)
		self.balance.setText("$" + str(self.money))
		self.balance.move(115, 2)
		self.balance.setReadOnly(True)

		self.prompt = QtWidgets.QLabel(self)
		self.prompt.setText("Bet on how many numbers? (0 to end game)")
		self.prompt.setFixedWidth(275)
		self.prompt.move(430, 0)

		self.enterBetsCount = 0
		self.combo = QtWidgets.QComboBox(self)
		self.combo.addItem('0')
		self.combo.addItem('1')
		self.combo.addItem('2')
		self.combo.addItem('3')
		self.combo.addItem('4')
		self.combo.addItem('5')
		self.combo.addItem('6')
		self.combo.move(600, 30)
		self.combo.currentTextChanged.connect(self.enterBets)
		self.numBets = 0 #int(str(self.combo.currentText()))

		self.text1 = QtWidgets.QLineEdit(self)
		self.text2 = QtWidgets.QLineEdit(self)
		self.text3 = QtWidgets.QLineEdit(self)
		self.text4 = QtWidgets.QLineEdit(self)
		self.text5 = QtWidgets.QLineEdit(self)
		self.text6 = QtWidgets.QLineEdit(self)
		
		self.texts = [self.text1, self.text2, self.text3,
					  self.text4, self.text5, self.text6]

		offset = 0
		for i in self.texts:
			i.setFixedWidth(120)
			i.move(575, 60 + offset)
			i.hide()
			offset += 40
			
		self.placeBetsCount = 0
		self.placeBetBtn = QtWidgets.QPushButton('Place Bets', self)
		self.placeBetBtn.clicked.connect(self.placeBets)
		self.placeBetBtn.move(600, 290)

		self.howMuch = QtWidgets.QLabel(self)
		self.howMuch.setText("How much do you want to bet?")
		self.howMuch.setFixedWidth(240)
		self.howMuch.move(5, 30)

		self.betAmt = QtWidgets.QLineEdit(self)
		self.betAmt.setFixedWidth(120)
		self.betAmt.move(5, 60)
	
		self.betAmtError = QtWidgets.QLabel(self)
		self.betAmtError.setText("Valid range is 1-Current Balance")
		self.betAmtError.setStyleSheet('color: red')
		self.betAmtError.setFixedWidth(200)
		self.betAmtError.move(5, 90)
		self.betAmtError.hide()

		self.wheelRangeError = QtWidgets.QLabel(self)
		self.wheelRangeError.setText("Valid range is 0-36 and 00")
		self.wheelRangeError.setStyleSheet("color: red")
		self.wheelRangeError.setFixedWidth(170)
		self.wheelRangeError.move(530, 310)
		self.wheelRangeError.hide()

		self.alreadyUsedError = QtWidgets.QLabel(self)
		self.alreadyUsedError.setText("Only use each number once")
		self.alreadyUsedError.setStyleSheet("color: red")
		self.alreadyUsedError.setFixedWidth(170)
		self.alreadyUsedError.move(530, 310)
		self.alreadyUsedError.hide()

		self.resultLabel = QtWidgets.QLabel(self)
		self.resultLabel.hide()
		self.winLoss = QtWidgets.QLabel(self)
		self.winLoss.hide()
		self.gameOverLabel = QtWidgets.QLabel(self)
		self.gameOverLabel.hide()
		self.gameOverMessage = QtWidgets.QLabel(self)
		self.gameOverMessage.hide()

		exitAction = QtWidgets.QAction('Exit', self)
		exitAction.triggered.connect(QtWidgets.qApp.quit)

		self.show()

	def enterBets(self):
		self.enterBetsCount += 1
		remove = 0

		if self.enterBetsCount > 1:
			remove = self.numBets - int(str(self.combo.currentText()))

		self.numBets = int(str(self.combo.currentText()))

		if remove > 0:
			for i in range(remove):
				self.texts[remove + self.numBets - 1 - i].hide()

		for i in range(self.numBets):			
			self.texts[i].show()
		
		if self.numBets == 0:
			self.betAmt.setReadOnly(True)
		else:
			self.betAmt.setReadOnly(False)	

		self.placeBetBtn.setEnabled(True)
		
	def placeBets(self):
		self.placeBetsCount += 1
		self.combo.setEnabled(False)
		
		wheelError = False
		doublingError = False

		for i in range(self.numBets):
			if self.isInRange(self.texts[i].text()) == False:
				wheelError = True
		
		wheelNums = []
		for i in range(self.numBets):
			if self.texts[i].text() not in wheelNums:
				wheelNums.append(self.texts[i].text())
			elif not wheelError:
				self.alreadyUsedError.show()
				doublingError = True

		if wheelError and not doublingError:
			self.alreadyUsedError.hide()
			self.wheelRangeError.show()
		elif not wheelError:
			self.wheelRangeError.hide()
			if not doublingError:
				for i in range(self.numBets):
					self.texts[i].setReadOnly(True)
				self.alreadyUsedError.hide()

		if self.numBets == 0:
			self.gameNotOver = False
			self.gameOver()

		if self.gameNotOver:
			if int(self.betAmt.text()) < 1 or \
			   int(self.betAmt.text()) > self.money:
				self.betAmtError.show()
			else:
				self.betAmtError.hide()
				self.betAmt.setReadOnly(True)

				if not wheelError and not doublingError:
					self.play()

	def isInRange(self, bet):
		if (int(bet) >= 0 and int(bet) <= 36) or bet == "00":
			return True
		
		return False

	def play(self):
		wheel = {0 : "0", 1 : "28", 2 : "9", 3 : "26", 4 : "30", 5 : "11",
		 			  6 : "7", 7 : "20", 8 : "32", 9 : "17", 10 : "5",
					  11 : "22", 12 : "34", 13 : "15", 14 : "3", 15 : "24",
					  16 : "36", 17 : "13", 18 : "1", 19 : "00", 20 : "27",
					  21 : "10", 22 : "25", 23 : "29", 24 : "12", 25 : "8",
					  26 : "19", 27 : "31", 28 : "18", 29 : "6", 30 : "21",
					  31 : "33", 32 : "16", 33 : "4", 34 : "23", 35 : "35",
					  36 : "14", 37 : "2"}
		
		odds = [35, 17, 11, 8, 6, 5]

		if self.gameNotOver:
			result = random.randint(0, 37)
			self.resultLabel.setText("Result: " + wheel[result])
			self.resultLabel.move(5, 120)
			self.resultLabel.show()
			self.placeBetBtn.setEnabled(False)

			betNums = [i.text() for i in self.texts]
			if wheel[result] in betNums:
				self.winLoss.setText("You won!")
				self.winLoss.setStyleSheet('color: green')
				self.money += (odds[self.numBets - 1] * int(self.betAmt.text()))
			else:
				self.winLoss.setText("You lost!")
				self.winLoss.setStyleSheet('color: red')
				self.money -= int(self.betAmt.text())
			
			self.winLoss.move(5, 150)
			self.winLoss.show()			
			self.balance.setText("$" + str(self.money))

			self.combo.setEnabled(True)
			self.betAmt.setReadOnly(False)
			for i in self.texts:
				i.setText("")
				i.setReadOnly(False)
				i.hide()
		
			if self.money == 0:
				self.gameNotOver = False
				self.gameOver()

	def gameOver(self):
		self.placeBetBtn.setEnabled(False)
		self.betAmt.setReadOnly(True)
		self.combo.setEnabled(False)

		if int(self.money) > 10000:
			self.gameOverMessage.setText("You made money! You win!!!")
			self.gameOverMessage.setStyleSheet('color: green')
		elif int(self.money) < 10000:
			self.gameOverMessage.setText("You lost money! You lose!")
			self.gameOverMessage.setStyleSheet('color: red')
		else:
			self.gameOverMessage.setText(
			"You broke even! That's a win in my book.")
		
		self.gameOverMessage.setFixedWidth(300)
		self.gameOverMessage.move(5, 320)
		self.gameOverMessage.show()
	
		self.gameOverLabel.setText("GAME OVER")
		self.gameOverLabel.setFixedWidth(80)
		self.gameOverLabel.move(315, 320)
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

class DisplayImage(QtWidgets.QWidget):
	def __init__(self, parent):
		QtWidgets.QWidget.__init__(self, parent)
		self.setup()

	def setup(self):
		self.image = QtWidgets.QLabel(self)
		pixmap =  QtGui.QPixmap("Images/rouletteWheel.jpg")
		self.image.resize(280, 280)
		self.image.setPixmap(pixmap.scaled(self.image.size(),
							 QtCore.Qt.IgnoreAspectRatio))
		self.image.move(210, 35)		

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
	main_window = RouletteTable()
	app.exec_()

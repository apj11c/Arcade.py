from PyQt4 import QtGui
import sys

import design

class GameApp(QtGui.QMainWindow, design.Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)

def main():
	app = QtGui.QApplication(sys.argv)
	form = GameApp()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()

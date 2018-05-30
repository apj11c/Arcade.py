from Tkinter import *
import tkFont
import Tkinter

class mainInterface(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.grid()
		fixed40 = tkFont.Font(family='Fixedsys', size=40)
		game1Button = Tkinter.Button(self,text=u"Game 1",
                                command=self.OnButton1Click)
		game1Button.grid(column=0,row=0)
		game1Button['font'] = fixed40

		game2Button = Tkinter.Button(self,text=u"Game 2",
                                command=self.OnButton2Click)
		game2Button.grid(column=1,row=0)
		game2Button['font'] = fixed40

		game3Button = Tkinter.Button(self,text=u"Game 3",
                                command=self.OnButton3Click)
		game3Button.grid(column=2,row=0)
		game3Button['font'] = fixed40

		self.grid_columnconfigure(0,weight=1)

	def OnButton1Click(self):
		print "GAME1 code goes here"

	def OnButton2Click(self):
		print "GAME2 code goes here"

	def OnButton3Click(self):
		print "GAME3 code goes here"


if __name__ == "__main__":
	app = mainInterface(None)
	app.title('Arcade.py')
	app.mainloop()

#encoding=utf8
import tkinter

import global_variable
class GuiSubWindow():
	"""提供选择清晰度的窗口"""

	def __init__(self,master=None):
		self.master = master
		self.frame = tkinter.Frame(self.master)
		self.master.title("Select")
		self.CreateWidgets()

		self.frame.pack()

		pass

	def CreateWidgets(self):
		self.info_text = tkinter.Text(self.frame)
		self.info_text.grid(column = 0,row = 1,columnspan = 2,sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W)
		pass


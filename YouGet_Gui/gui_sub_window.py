#encoding=utf8
import tkinter
from tkinter import ttk

import global_variable
class GuiSubWindow():
	"""提供选择清晰度的窗口"""

	def __init__(self,master=None,video_info=None):
		self.master_ = master
		self.frame_ = tkinter.Frame(self.master_)

		self.video_info_ = video_info
		self.master_.title("Select")
		self.CreateWidgets()

		self.frame_.pack()

	def CreateWidgets(self):
		self.info_text_ = tkinter.Text(self.frame_)
		self.info_text_.grid(column = 0,row = 1,columnspan = 2,sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

		#创建选择清晰度的Combobox
		#number = ttk.StringVar()

		self.format_choice_combobox_ = ttk.Combobox(self.frame_)
		self.format_choice_combobox_.grid(column = 0,row = 2,sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

		#按钮
		self.ok_button_ = tkinter.Button(self.frame_)

	def Format(self,json_data):
		
		pass
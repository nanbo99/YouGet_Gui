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

		self.current_display = -1
		self.DisplayInfo()


	def CreateWidgets(self):
		self.info_text_ = tkinter.Text(self.frame_)
		self.info_text_.grid(column = 0,row = 1,columnspan = 2,sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

		#创建选择清晰度的Combobox
		#number = ttk.StringVar()

		self.format_choice_combobox_ = ttk.Combobox(self.frame_)
		self.format_choice_combobox_.grid(column = 0,row = 2,sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
		self.format_choice_combobox_['state'] = 'readonly'

		#按钮
		self.ok_button_ = tkinter.Button(self.frame_,command = self.DisplayInfo)
		self.ok_button_.grid(column = 1,row = 2,sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

	def DisplayInfo(self):
		if self.current_display == len(self.video_info_) - 1:
			#全部弄完
			pass

		self.current_display = self.current_display + 1
		self.chosen_type = []
		single_video_info = self.video_info_[self.current_display]
		self.info_text_.delete("1.0", tkinter.END)
		self.info_text_.insert("1.0", single_video_info['raw_buffer'])
		variable = tkinter.StringVar(self.frame_)
		
		if 'streams' in single_video_info:
			self.format_choice_combobox_['values'] = single_video_info['streams']
			self.format_choice_combobox_.current(0)
		else:
			self.format_choice_combobox_['values'] = 'Default'
			self.format_choice_combobox_.current(0)

		if not self.current_display == len(self.video_info_) - 1:
			self.ok_button_['text'] = '设置下一个'
		else:
			self.ok_button_['text'] = '开始全部下载'

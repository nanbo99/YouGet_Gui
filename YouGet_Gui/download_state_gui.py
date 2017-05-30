import tkinter
from tkinter import ttk

class gui_download_window(object):
	"""下载界面的window"""
	def __init__(self,video_info, **kwargs):
		self.master_ = master
		self.frame_ = tkinter.Frame(self.master_)
		self.master_.title("Download Form")
		self.video_info_ = video_info
		self.CreateWidgets()
		self.frame_.pack()
		self.current_display_index = 0
		return super().__init__(**kwargs)

	def CreateWidgets(self):

		self.current_title_label_ = tkinter.Label(self.master_,text = '当前下载的标题:')
		self.current_title_label_.grid(column = 0,row =0,sticky = tkinter.W)

		self.current_title_entry_ = tkinter.Entry(self.master_,state='readonly')
		self.current_title_entry_.grid(column = 0,row=1,columnspan = 2,sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W)

		self.download_progress = ttk.Progressbar(self.master_)
		self.download_progress.grid(column = 0,row = 2,colunmspan =2,sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W)

	def Display(self):
		self.current_title_entry_['state'] = 'normal'
		self.current_title_entry_.delete(0,tkinter.END)
		self.current_title_entry_.insert(0,self.video_info_[self.current_display_index])

		pass
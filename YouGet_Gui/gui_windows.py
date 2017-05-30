import tkinter
import tkinter.filedialog

import global_variable
import YouGet_Gui
class GuiWindow():
	"""使用Tkinter提供一个Gui的窗口"""

	def __init__(self, master=None):
		"""初始化"""
		self.master_ = master
		self.frame_ = tkinter.Frame(self.master_)
		
		self.CreateWidgets()

		self.frame_.pack()

	def OpenFileDialog(self):
		filepath = tkinter.filedialog.askdirectory()
		if filepath:
			self.askdir_text_['state'] = 'normal'
			# self.askdir_text.config(state='normal')
			self.askdir_text_.delete(0,tkinter.END)
			self.askdir_text_.insert(0,filepath)
			global_variable.you_get_caller_instance.SetDir(filepath)
			self.askdir_text_['state'] = 'readonly'
			# self.askdir_text.config(state='readonly')
			# print(filepath)

	def CreateWidgets(self):
		"""创建控件"""

		# 提示文本
		self.url_label = tkinter.Label(self.frame_,text = "需要下载的网页的网站")
		self.url_label.grid(column = 0,row = 0,sticky =tkinter.W)
		# self.url_label.pack()

		# 文本框
		self.url_text = tkinter.Text(self.frame_,height = 10)
		self.url_text.grid(column = 0,row = 1,columnspan = 2,sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W)
		#self.url_text.pack()

		# 位置选择的文本框
		self.askdir_text_ = tkinter.Entry(self.frame_,state='readonly')#,width = 30)
		self.askdir_text_.grid(column = 0,row = 2,columnspan=2,sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W)

		# 位置选择
		self.askdir_button = tkinter.Button(self.frame_,text="选择保存文件的位置",command = self.OpenFileDialog)
		self.askdir_button.grid(column = 1,row = 2,sticky = tkinter.E)

		# 开始按钮
		self.start_download_button_ = tkinter.Button(self.frame_,text = "开始",command = YouGet_Gui.StartPreDownload)
		self.start_download_button_.grid(column = 1,row = 3,sticky = tkinter.E)
		# self.button_ok.pack()

		# 状态栏
		self.status_bar_label_ = tkinter.Label(self.frame_)
		self.status_bar_label_.grid(column = 0,row = 3,sticky = tkinter.W)
		self.SetStatusBarText()

	def SetStatusBarText(self,text = 'Status Bar'):
		self.status_bar_label_['text'] = text
		pass

	def GetText(self):
		"""获取Text控件中用户输入的信息"""

		# TODO
		# 判断用户的输入
		text = self.url_text.get("1.0",tkinter.END).split('\n')
		return text
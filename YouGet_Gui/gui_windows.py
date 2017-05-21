import tkinter
import tkinter.filedialog

import global_variable
import YouGet_Gui
class GuiWindow():
	"""使用Tkinter提供一个Gui的窗口"""

	def __init__(self, master=None):
		"""初始化"""
		self.master = master
		self.frame = tkinter.Frame(self.master)
		
		self.CreateWidgets()

		self.frame.pack()

	def OpenFileDialog(self):
		filepath = tkinter.filedialog.askdirectory()
		if filepath:
			self.askdir_text['state'] = 'normal'
			#self.askdir_text.config(state='normal')
			self.askdir_text.delete(0,tkinter.END)
			self.askdir_text.insert(0,filepath)
			global_variable.you_get_caller_instance.SetDir(filepath)
			self.askdir_text['state'] = 'readonly'
			#self.askdir_text.config(state='readonly')
			#print(filepath)

	def CreateWidgets(self):
		"""创建控件"""

		"""提示文本"""
		self.url_label = tkinter.Label(self.frame,text = "需要下载的网页的网站")
		self.url_label.grid(column = 0,row = 0,sticky =tkinter.W)
		#self.url_label.pack()

		"""文本框"""
		self.url_text = tkinter.Text(self.frame,height = 10)
		self.url_text.grid(column = 0,row = 1,columnspan = 2,sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W)
		#self.url_text.pack()

		"""位置选择的文本框"""
		self.askdir_text = tkinter.Entry(self.frame,state='readonly')#,width = 30)
		self.askdir_text.grid(column = 0,row = 2,columnspan=2,sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W)

		"""位置选择"""
		self.askdir_button = tkinter.Button(self.frame,text="选择保存文件的位置",command = self.OpenFileDialog)
		self.askdir_button.grid(column = 1,row = 2,sticky = tkinter.E)

		"""开始按钮"""
		self.start_download_button = tkinter.Button(self.frame,text = "开始下载",command = YouGet_Gui.StartDownload)
		self.start_download_button.grid(column = 1,row = 3,sticky = tkinter.E)
		#self.button_ok.pack()
	def GetText(self):
		"""获取Text控件中用户输入的信息"""
		text = self.url_text.get("1.0",tkinter.END).split(';')
		return text
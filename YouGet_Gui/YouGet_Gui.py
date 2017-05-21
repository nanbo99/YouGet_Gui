
#encoding=utf8
import tkinter
import you_get_caller
import global_variable
import gui_windows

def StartDownload():
	pass
def Test():
	print(global_variable.you_get_caller_instance)
def main():
	global_variable.you_get_caller_instance = you_get_caller.YouGetCaller()
	global_variable.you_get_caller_instance = you_get_caller.YouGetCaller()
	
	global_variable.gui_windows_instance = gui_windows.GuiWindow()
	global_variable.gui_windows_instance.master.title('You Get GUI')
	global_variable.gui_windows_instance.mainloop()

	pass

if __name__ == '__main__':
	global_variable.init()
	main()
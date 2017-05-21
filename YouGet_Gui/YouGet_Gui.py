#encoding=utf8
import tkinter
import tkinter.messagebox
import you_get_caller
import global_variable
import gui_windows
import gui_sub_window

def StartDownload():
	global_variable.gui_windows_instance.sub_window_root = tkinter.Toplevel(global_variable.gui_windows_instance.master)
	global_variable.gui_windows_instance.sub_window_instance = gui_sub_window.GuiSubWindow(global_variable.gui_windows_instance.sub_window_root)
	pass

def main():
	global_variable.you_get_caller_instance = you_get_caller.YouGetCaller()

	root = tkinter.Tk()
	global_variable.gui_windows_instance = gui_windows.GuiWindow(root)
	root.title('You Get GUI')
	root.mainloop()

	pass

if __name__ == '__main__':
	global_variable.init()
	main()
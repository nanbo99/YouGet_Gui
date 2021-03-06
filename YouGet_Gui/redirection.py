import sys
class Redirection(object):
	def __init__(self):
		self.buffer_ = ''
		self.last_message_ = ''

	def SetupToRedirect(self):
		self.console_backup_ = sys.stdout
		sys.stdout = self

	def Reset(self):
		self.buffer_ = ''
		sys.stdout = self.console_backup_

	def GetLastMessage(self):
		return self.last_message_

	def write(self,out_stream):
		# self.PrintToScreen(out_stream)
		self.last_message_ = out_stream
		self.buffer_+=out_stream

	def flush(self):
		self.buffer_ = ''

	def PrintToScreen(self, content):
		self.console_backup_.write(content)

	def GetBuffer(self):
		return self.buffer_
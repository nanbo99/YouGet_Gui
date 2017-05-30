import redirection
import you_get_caller
import global_variable

class download_state(object):

	def __init__(self, **kwargs):


		return super().__init__(**kwargs)

	def check(self):
		"""判断能不能通过输出查看进度"""
		pass

	def update_state(self):
		"""更新进度"""
		global_variable.global_lock.acquire()
		global_variable.redirection_instance.GetLastMessage()
		global_variable.global_lock.release()


		pass
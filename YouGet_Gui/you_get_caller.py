from you_get.common import any_download_playlist, any_download, download_main
import os
import global_variable

class YouGetCaller(object):
	"""You-Get的调用类"""

	def __init__(self):
		self.DefaultKwargs()
		pass
	def DefaultKwargs(self):
		default_dir = os.getcwd()
		self.kwargs = {'output_dir': default_dir,
			'merge': True,
			'json_output': False,
			'caption': True,
			'playlist': False}
	def SetDir(self,new_dir):
		self.kwargs['output_dir'] = new_dir

	def GetVideoInfo(self,urls):
		temp_kwargs = self.kwargs
		temp_kwargs['info_only'] = True
		download_main(any_download, any_download_playlist, urls, **self.kwargs)
		print(self.kwargs)
		pass
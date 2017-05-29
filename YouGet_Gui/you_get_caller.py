from you_get.common import any_download_playlist, any_download, download_main
import os
import global_variable
import subprocess
import re
import redirection
class YouGetCaller(object):
	"""
	you-get的调用类
	
	you-get暂时还没有提供api供程序直接调用
	又不想修改它的源码，以免在以后you-get更多的commit后，通过pip升级有麻烦
	还不如直接用命令行调用
	"""

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
		"""获取视频信息

		返回:
			title: 标题
			all_format: 所有的format
			all_video_profile: 所有的video_profile
			whole_content: 全部返回的字符
		"""
		global_variable.redirection_instance.SetupToRedirect()

		kwargs = self.kwargs
		kwargs['info_only'] = True
		kwargs['json_output'] = True

		download_main(any_download, any_download_playlist, urls, **kwargs)

		json_output = global_variable.redirection_instance.GetBuffer()

		global_variable.redirection_instance.Reset()

		for single_json in json_output:
			yield ast.literal_eval(single_json)
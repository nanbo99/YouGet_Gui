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

	def ParseInfo(self,raw_buffer):
		info = {}
		for single in raw_buffer.split('\n'):
			if single.lower().startswith('site'):
				info['site'] = single[5:].replace(' ', '')
			elif single.lower().startswith('title'):
				info['title'] = single[6:].replace(' ', '')
			elif single.lower().startswith('type'):
				info['type'] = single[5:].replace(' ', '')
			elif single.lower().startswith('size'):
				info['size'] = single[5:].replace(' ', '')
			elif single.lower().startswith('streams'):
				info['streams'] = []
			if single.lower().startswith('    # download-with'):
				type_begin = single.find('--')
				option_begin = single.find('=', type_begin)

				type_ = single[type_begin + 2:option_begin]
				option_ = single[option_begin + 1:-6]
				info['streams'].append(option_)
				info['streams_type'] = type_

		info['raw_buffer'] = raw_buffer
		return info
	def DownloadVideo(self,urls):
		pass
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

		info = []
		for url in urls:
			if url == '':
				break
			pack_url = [url]
			try:
				download_main(any_download, any_download_playlist, pack_url, **kwargs)
			except:
				global_variable.redirection_instance.PrintToScreen('Something unexpected happened')
			output = global_variable.redirection_instance.GetBuffer()
			info.append(self.ParseInfo(output))
			global_variable.redirection_instance.flush()
		global_variable.redirection_instance.Reset()

		print(info)
		return info
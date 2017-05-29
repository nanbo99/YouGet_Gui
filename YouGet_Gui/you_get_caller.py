from you_get.common import any_download_playlist, any_download, download_main
import os
import global_variable
import subprocess
import re
class YouGetCaller(object):
	"""
	you-get的调用类
	
	you-get暂时还没有提供api供程序直接调用
	又不想修改它的源码，以免在以后you-get更多的commit后，通过pip升级有麻烦
	还不如直接用命令行调用
	"""

	def __init__(self):
		#self.DefaultKwargs()
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
		"""
		以下是临时代码
		temp_kwargs = self.kwargs
		temp_kwargs['info_only'] = True
		download_main(any_download, any_download_playlist, urls, **self.kwargs)
		print(self.kwargs)
		return self.kwargs
		"""
		for url in urls:
			whole_content = str(subprocess.check_output(['python', '-m', 'you_get', '-i', url]), encoding='gb2312')

			re_rule_title = re.compile('title:.*')
			re_rule_format = re.compile('format:.*')
			re_rule_video_profile = re.compile('video-profile:.*')

			text_title = re_rule_title.findall(whole_content)
			text_profile = re_rule_video_profile.findall(whole_content)
			text_format = re_rule_format.findall(whole_content)

			all_format = []
			all_video_profile = []

			for single_format in text_format:
				all_format.append(single_format[7:-1].replace(' ', ''))
			for single_video_profile in text_profile:
				all_video_profile.append(single_video_profile[14:-1].replace(' ', ''))
			yield (text_title[6:-1].replace(' ', ''), all_format, all_video_profile,whole_content)
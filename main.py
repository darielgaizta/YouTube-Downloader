from pytube import YouTube
from pathlib import Path
import os

class YouTubeDownloader(object):
	"""docstring for YouTubeDownloader"""
	def __init__(self, link):
		super(YouTubeDownloader, self).__init__()
		self.link = link
		self.name = YouTube(link).title
		self.path = os.path.dirname(__file__) + '\\downloads'
	
	def download_as_video(self):
		yt = YouTube(self.link).streams.get_highest_resolution()
		try: yt.download(output_path=self.path)
		except Exception as e:
			print('Oops, something went wrong.')
			raise e

	def download_as_audio(self):
		yt = YouTube(self.link).streams.filter(only_audio=True).first()
		try: file = yt.download(output_path=self.path)
		except Exception as e:
			print('Oops, something went wrong.')
			raise e
		base, ext = os.path.splitext(file)
		os.rename(file, base + '.mp3')

def main():
	# Create a new instance (object) ytd
	ytd = YouTubeDownloader(input('Enter your YouTube video URL: '))

	# Get user input
	download_as = input('Download as:\n[1] Video\n[2] Audio\n>>> ')

	# Validate user input
	while download_as != '1' and download_as != '2':
		print('[ERROR] Incorrect input, please choose to download as [1] Video or [2] Audio.')
		download_as = input('Download as:\n[1] Video\n[2] Audio\n>>> ')

	print(f'Preparing to download {ytd.name}...')

	if download_as == '1':
		ytd.download_as_video()
		print(f'Video has been saved to {ytd.path}.')
	else:
		ytd.download_as_audio()
		print(f'Audio has been saved to {ytd.path}.')
	print('--- End of Program ---')


if __name__ == '__main__':
	main()
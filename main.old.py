from pytube import YouTube as yt
import ipdb
import sys

# https://www.youtube.com/vEQ8CXFWLZU

link = sys.argv[1]
my_proxies = {}

def progress_func(self):
    print(f"Video found")
    print(f"Downloading video... ")

def complete_func(self):
    print("DONE!")

'''
object = yt(
        link,
        on_progress_callback=progress_func,
        on_complete_callback=complete_func,
        proxies=my_proxies,
        use_oauth=False,
        allow_oauth_cache=True
    )
'''

object = yt(link)
stream = object.streams.get_highest_resolution()

wsl_file_path = f"/mnt/c/Users/Bizzo/Desktop/Aulas/"

stream.download(wsl_file_path)


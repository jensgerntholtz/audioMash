#!/usr/bin/env python3

from time import sleep
from youtube_dl import YoutubeDL
import sox


# Log Object
class state_logger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        print(msg)

    def error(self, msg):
        print(msg)


# Functions
def download_audio(video_url):

    # Options for the YouTube Downloader
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'logger': state_logger(),
        'progress_hooks': [download_progress]
    }

    # Set this variables to be accessible for the entire script
    global video_title, file_name

    # Download audio
    with YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(video_url, download=False)
        video_title = video_info.get('title', None)
        video_id = video_info.get('display_id', None)
        file_name = video_title + '-' + video_id + ".wav"
        ydl.download([video_url])


def download_progress(d):
    animation_chars = ["|", "/", "-", "\\"]
    download_msg = f"Downloading \"{video_title}\""

    # Display a download animation
    if d['status'] != 'finished':
        for i in range(len(animation_chars)):
            print(f"{download_msg} {d['_percent_str']} {animation_chars[i]}", end="\r")
            sleep(0.15)
    else:
        # Clear the line 
        print(" " * (len(download_msg)+9), end="\r") # Adding 8 because of the whitespace, percentage and the aniamated char
        print("Download complete!")


def process_audio(file_name, bass_boost_magnitude):
    # Warn the user if he choose a value of 100 or higher
    if bass_boost_magnitude >= 100:
        print("WARNING: Setting the bass_boost to a value of 100 or higher might produce damage to your ears/headphones")

    # Create a Transformer instance
    tfm = sox.Transformer()
    tfm.bass(bass_boost_magnitude)

    # Compress file
    tfm.compand()

    # Save the ear rape audio
    output_file = file_name.replace(".wav", "-earrape.wav")
    tfm.build(file_name, output_file)
    tfm.effects_log


video_url = input("Paste a YouTube url (e.g https://www.youtube.com/watch?v=ZZ5LpwO-An4) -> ")
bass_boost = int(input("Set the bass_boost (0-100) -> "))
download_audio(video_url)
print(f"Processing \"{video_title}\"...")
process_audio(file_name, bass_boost)
print("Complete!")

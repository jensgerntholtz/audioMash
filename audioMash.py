from __future__ import unicode_literals
import youtube_dl
#audio manipulator
import sox
import os

class state_logger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Download completed, now processing ...')

def download_audio():
    global video_url
    global video_title
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'logger': state_logger(),
        'progress_hooks': [my_hook],
    }
    video_url = raw_input("Paste your YouTube video link in the standard format \ne.g. https://www.youtube.com/watch?v=ZZ5LpwO-An4 \n :")
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
        info_dict = ydl.extract_info(video_url, download=False)
        video_title = info_dict.get('title', None)

def process_audio(video_url,video_title):
    global file_name
    bass_boost_setting = raw_input('Please choose a bass boost magnitude: \n0:Moderate\n1:Strong\n2:TiniTerminate\n:')

    options_bass_boost_setting =   {0 : bass_boost_magnitude=10,
                                    1 : bass_boost_magnitude=20,
                                    2 : bass_boost_magnitude=30,
    }
    options_bass_boost_choice[bass_boost_choice]()

    # creates a Transformer instance
    bass_boost_magnitude = 20
    tfm = sox.Transformer()
    tfm.bass(bass_boost_magnitude)
    # compresses file
    tfm.compand()
    pos = video_url.find('=')+1;
    file_name = video_title+'-'+video_url[pos:]
    # File input and output can't be the same name
    tfm.build(file_name+'.wav', video_title+'-AudioMashed'+'.wav')
    tfm.effects_log

def rundown():
    global file_name
    os.remove(file_name+'.wav')

video_url = ''
video_title = ''
file_name = ''
download_audio()
process_audio(video_url,video_title)

continuation = raw_input('Enter (0):\tAccept changes and exit.\nEnter (1):\tRevert changes and try a different bass boost magnitude\nEnter (2):\tAccept changes and process another song\n')
options_continuation = {0 : rundown,
                        1 : process_audio(video_url,video_title),
                        2 : download_audio,
}
options_continuation[int(continuation)]()

#convert webm to wav
# ffmpeg -i "" -acodec pcm_s16le -ac 1 -ar 22050 ""
#
# #sox only supports wav
# /usr/local/bin/sox-14.4.2/sox -v 4.0 "" -r 16k "" treble +50 bass +50 treble +50

![Build Status](https://travis-ci.org/jensgerntholtz/audioMash.svg?branch=master)
# audioMash
A Python-based command-line-program that extracts audio from youtube videos and adjusts the listening experience

- [DESCRIPTION](#description)
- [INSTALLATION](#installation)
- [USAGEGUIDE](#usageguide)
- [BUGS](#bugs)

# DESCRIPTION
audioMash is a tool for creators that contribute towards the meme internet culture. Specifically to automate the creation of "Ear rape" audio. "Ear rape" is a trend, in which the audio is modified in such a way that it sounds, terrible for comedic effect.

audioMash runs using Python.

WARNING: Please be cautious when playing back the processed audio files. It will damage your ears, as well as the playback device at a sufficient volume.

**DISCLAIMER WE ARE NOT RESPOSIBLE FOR ANY DAMAGES CAUSED BY THIS SOFTWARE AS WELL AS THE PLAYBACK OF THE AUDIO FILES**

# INSTALLATION

youtube-dl
https://github.com/rg3/youtube-dl/blob/master/README.md#installation

sox
https://github.com/rabitt/pysox

# USAGEGUIDE
Paste your YouTube video link (standard playback format) in your command-line-interface
e.g. `https://www.youtube.com/watch?v=ZZ5LpwO-An4`

# BUGS

Entering options does not affect the outcome. 
The title of the video may not contain a '/' or '\'

Selecting bassboost options does not impact outcome.

Selecting option 1 & 2 at the end of the program cuases issues

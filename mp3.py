#Python Program to Extract mp3 from mp4 

import moviepy
import moviepy.editor
#put your file path here 
video = moviepy.editor.VideoFileClip("")
audio = video.audio
audio.write_audiofile('new_audio.mp3') 
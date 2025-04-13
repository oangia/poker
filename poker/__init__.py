from poker.Media import play_audio, play_video
from poker.File import random_file, file_exists
from poker.TTS import text_to_speech, speech_to_text
from poker.Audio import adjust_volume, adjust_speed
from poker.Subtitle import Subtitle
from poker.Video import Video
import numpy as np
from moviepy.editor import *
from pydub import AudioSegment

def process_audio(audio, bg_music):
    narrator = adjust_volume(audio, target_dBFS=-28)
    music = adjust_volume(bg_music, target_dBFS=-39)
    final_audio = narrator.overlay(music)
    final_audio.export("output_audio.wav", format="wav")
    final_audio = AudioFileClip("output_audio.wav")
    return final_audio

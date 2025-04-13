from poker.Media import play_audio, play_video
from poker.File import random_file, file_exists
from poker.TTS import text_to_speech, speech_to_text
from poker.Audio import adjust_volume, adjust_speed
from poker.Subtitle import Subtitle
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
    
def process_video(video_path):
    video = VideoFileClip(video_path)
    # Set target size for YouTube Shorts (9:16 aspect ratio)
    target_width = 1080
    target_height = 1920
    
    # Resize video to fit 9:16 aspect ratio (resize while maintaining the center)
    video_resized = video.resize(height=target_height)
    video_resized = video_resized.crop(x1=(video_resized.w - target_width) // 2, x2=(video_resized.w + target_width) // 2)
    
    return video_resized

from poker.Media import play_audio, play_video
from poker.File import random_file, file_exists
from poker.TTS import text_to_speech, speech_to_text
from poker.Audio import adjust_volume, adjust_speed

from moviepy.editor import *
from pydub import AudioSegment

def make_video(video_path, audio, bg_music):
    narrator = adjust_volume(audio, target_dBFS=-28)
    music = adjust_volume(bg_music, target_dBFS=-39)
    final_audio = narrator.overlay(music)
    final_audio.export("output_audio.wav", format="wav")
    final_audio = AudioFileClip("output_audio.wav")
    video = VideoFileClip(video_path)
    video_duration = video.duration
    audio_duration = final_audio.duration
    
    # If audio is longer than video, loop the video
    if audio_duration > video_duration:
        num_loops = int(audio_duration // video_duration) + 1  # Loop video enough times
        video = video.fx(vfx.loop, num_loops)  # Loop the video
        
    # Trim the video to match audio duration
    video = video.subclip(0, audio_duration)
    
    # Final video
    final_video = video.set_audio(final_audio)
    
    # Output final video
    final_video.write_videofile("output_video.mp4", codec="libx264", audio_codec="aac" , logger=None)

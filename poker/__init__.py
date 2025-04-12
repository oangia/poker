from poker.Media import play_audio, play_video
from poker.File import random_file, file_exists
from poker.TTS import text_to_speech, speech_to_text
from poker.Audio import adjust_volume, adjust_speed
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from moviepy.editor import *
from pydub import AudioSegment

def make_video(video_path, audio, bg_music, texts):
    audio = process_audio(audio, bg_music)
    video = process_video(video_path)
    video_duration = video.duration
    audio_duration = audio.duration
    
    # If audio is longer than video, loop the video
    if audio_duration > video_duration:
        num_loops = int(audio_duration // video_duration) + 1  # Loop video enough times
        video = video.fx(vfx.loop, num_loops)  # Loop the video
        
    # Trim the video to match audio duration
    video = video.subclip(0, audio_duration)
    
    # Final video
    final_video = video.set_audio(audio)
    text_clips = add_text_to_video(texts, final_video)

    # Combine the video with all text clips
    final = CompositeVideoClip([final_video] + text_clips)
    # Output final video
    final.write_videofile("output_video.mp4", codec="libx264", audio_codec="aac" , logger=None)

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

def add_text_to_video(texts, video):
    total_count = 0
    for text in texts:
        total_count += len(text)
    

    # Use default font
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size=40)
    text_clips = []
    current_time = 0
    # Create a text clip for each entry in the array
    for text in texts:
        # Create transparent image for each text clip
        img = Image.new("RGBA", (video.w, video.h), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        start_time = total_count * video.duration / len(texts)
        text_duration = len(text) * video.duration / total_count
        # Center the text
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (video.w - text_width) // 2
        y = (video.h - text_height) // 2

        # Add a solid rectangle background behind the text (semi-transparent)
        background_padding = 10  # Space between text and background
        draw.rectangle(
            [x - background_padding, y - background_padding, x + text_width + background_padding, y + text_height + background_padding],
            fill=(0, 0, 0, 64)  # Semi-transparent black background (RGBA)
        )

        draw.text((x, y), text, font=font, fill="white")

        # Convert image to clip
        text_img = np.array(img)
        txt_clip = ImageClip(text_img, duration=text_duration - 0.2).set_start(current_time)

        # Add to the list of text clips
        text_clips.append(txt_clip)
        current_time += text_duration + 0.2

    return text_clips


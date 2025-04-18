from poker.File import random_file
from moviepy.editor import VideoFileClip, vfx

class Video:
    def __init__(self, path):
        video = VideoFileClip(path)
        target_width = 1080
        target_height = 1920
        
        # Resize video to fit 9:16 aspect ratio (resize while maintaining the center)
        self.video = video.resize(height=target_height)
        self.video = self.video.crop(x1=(self.video.w - target_width) // 2, x2=(self.video.w + target_width) // 2)

    @staticmethod
    def get_random(path):
        return Video(random_file(path))

    def get_duration(self):
        return self.video.duration

    def adjust_duration(self, audio_duration):
        # If audio is longer than video, loop the video
        if audio_duration > self.video.duration:
            num_loops = int(audio_duration // self.video.duration) + 1  # Loop video enough times
            self.video = self.video.fx(vfx.loop, num_loops)  # Loop the video
        
        # Trim the video to match audio duration
        self.video = self.video.subclip(0, audio_duration)

    def set_audio(self, audio):
        self.video = self.video.set_audio(audio)

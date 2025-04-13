from pydub import AudioSegment
from moviepy.editor import AudioFileClip
from poker.File import random_file

class Audio:
    def __init__(self, path):
        self.audio = AudioSegment.from_file(path, format=audio_file[-3:])

    @staticmethod
    def get_random(path):
        return Audio(random_file(path))

    def overlay(self, background, output="output_audio.wav"):
        final_audio = self.audio.overlay(background.audio)
        final_audio.export(output, format=output[-3:])
        return Video(output)
        
    def process_audio(audio, bg_music):
        narrator = Video(audio)
        narrator.adjust_volume(target_dBFS=-28)
        music = Video.get_random(bg_music)
        music.adjust_volume(target_dBFS=-39)
        final_audio = narrator.audio.overlay(music.audio)
        final_audio.export("output_audio.wav", format="wav")
        return Video("output_audio.wav")

    def adjust_volume(target_dBFS):
        change_in_dBFS = target_dBFS - self.audio.dBFS
        self.audio = self.audio.apply_gain(change_in_dBFS)
        
    def adjust_speed(output_file, speed=0.5):
        slowed_sound = self.audio._spawn(self.audio.raw_data, overrides={
            "frame_rate": int(self.audio.frame_rate * speed)
        }).set_frame_rate(self.audio.frame_rate)
        slowed_sound.export(output_file, format="mp3")



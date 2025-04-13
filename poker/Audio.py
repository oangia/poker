from pydub import AudioSegment
from moviepy.editor import AudioFileClip
from poker.File import random_file
import speech_recognition as sr
from IPython.display import Audio as DisplayAudio

class Audio:
    def __init__(self, path, target_dBFS=None):
        self.path = path
        self.audio = AudioSegment.from_file(path, format=path[-3:])
        if target_dBFS is not None:
            self.adjust_volume(target_dBFS)
        
    @staticmethod
    def get_random(path, target_dBFS=None):
        return Audio(random_file(path), target_dBFS)

    def overlay(self, background, output="output_audio.wav"):
        final_audio = self.audio.overlay(background.audio)
        final_audio.export(output, format=output[-3:])
        return AudioFileClip(output)

    def adjust_volume(self, target_dBFS):
        change_in_dBFS = target_dBFS - self.audio.dBFS
        self.audio = self.audio.apply_gain(change_in_dBFS)
        
    def adjust_speed(self, output_file, speed=0.5):
        slowed_sound = self.audio._spawn(self.audio.raw_data, overrides={
            "frame_rate": int(self.audio.frame_rate * speed)
        }).set_frame_rate(self.audio.frame_rate)
        slowed_sound.export(output_file, format="mp3")

    def speech_to_text(self):
        self.audio.export("converted.wav", format="wav")
        recognizer = sr.Recognizer()
        with sr.AudioFile("converted.wav") as source:
            audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError:
            print("Could not request results")

    def play_audio(self, autoplay=True):
        display(DisplayAudio(self.path, autoplay=autoplay))
        

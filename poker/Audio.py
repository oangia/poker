from pydub import AudioSegment
from moviepy.editor import AudioFileClip
from poker.File import random_file
import speech_recognition as sr
from IPython.display import Audio

class Audio:
    def __init__(self, path):
        self.path = path
        self.audio = AudioSegment.from_file(path, format=audio_file[-3:])

    @staticmethod
    def get_random(path):
        return Audio(random_file(path))

    def overlay(self, background, output="output_audio.wav"):
        final_audio = self.audio.overlay(background.audio)
        final_audio.export(output, format=output[-3:])
        return Video(output)

    def adjust_volume(target_dBFS):
        change_in_dBFS = target_dBFS - self.audio.dBFS
        self.audio = self.audio.apply_gain(change_in_dBFS)
        
    def adjust_speed(output_file, speed=0.5):
        slowed_sound = self.audio._spawn(self.audio.raw_data, overrides={
            "frame_rate": int(self.audio.frame_rate * speed)
        }).set_frame_rate(self.audio.frame_rate)
        slowed_sound.export(output_file, format="mp3")

    def speech_to_text():
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

    def play_audio(autoplay=True):
        display(Audio(self.path, autoplay=autoplay))
        

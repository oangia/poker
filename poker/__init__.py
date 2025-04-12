from gtts import gTTS
from pydub import AudioSegment
from pydub.effects import normalize
from IPython.display import Audio, display
import os
import speech_recognition as sr
import random
from pydub import AudioSegment
from IPython.display import HTML

def random_file(folder_path):
    files = os.listdir(folder_path)
    return folder_path + "/" + random.choice(files)

def adjust_volume(audio_file, target_dBFS):
    sound = AudioSegment.from_file(audio_file, format=audio_file[-3:])
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)
    
def speech_to_text(file, format):
    audio = AudioSegment.from_file(file, format=format)
    audio.export("converted.wav", format="wav")
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
    
def text_to_speech(text, audio_file):
    tts = gTTS(text)
    tts.save(audio_file)

def slow_down_audio(input_file, output_file, speed=0.5):
    sound = AudioSegment.from_file(input_file)
    slowed_sound = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    }).set_frame_rate(sound.frame_rate)
    slowed_sound.export(output_file, format="mp3")
    
def play_audio(file, autoplay=True):
    display(Audio(file, autoplay=autoplay))

def play_video(file):
    HTML("""
    <video width="640" height="360" controls autoplay>
      <source src="{file}" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    """)
def file_exists(filename):
    """
    Check if a file exists.

    :param filename: The path to the file to check.
    :return: True if the file exists, False otherwise.
    """
    return os.path.isfile(filename)

# Load the audio file
def normalize_sound(input_file, format="mp3"):
    sound = AudioSegment.from_file(input_file, format=format)
    normalized_sound = adjust_volume(sound, -22.0)  # Normalize to -20 dBFS
    normalized_sound.export("output_audio.wav", format="wav")
    return "output_audio.wav"

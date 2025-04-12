from gtts import gTTS
from pydub import AudioSegment
from pydub.effects import normalize
from poker.Media import play_audio, play_video
from poker.File import random_file, file_exists
import speech_recognition as sr
    
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
    


# Load the audio file
def normalize_sound(input_file, format="mp3"):
    sound = AudioSegment.from_file(input_file, format=format)
    normalized_sound = adjust_volume(sound, -22.0)  # Normalize to -20 dBFS
    normalized_sound.export("output_audio.wav", format="wav")
    return "output_audio.wav"

import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
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

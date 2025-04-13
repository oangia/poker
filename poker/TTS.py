from gtts import gTTS
    
def text_to_speech(text, audio_file):
    tts = gTTS(text)
    tts.save(audio_file)

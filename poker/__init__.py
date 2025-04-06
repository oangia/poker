from gtts import gTTS
from pydub import AudioSegment

def textToSpeech(text, audio_file):
    tts = gTTS(text)
    tts.save(audio_file)

def slow_down_audio(input_file, output_file, speed=0.5):
    sound = AudioSegment.from_file(input_file)
    slowed_sound = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    }).set_frame_rate(sound.frame_rate)
    slowed_sound.export(output_file, format="mp3")

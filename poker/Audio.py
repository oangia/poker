from pydub import AudioSegment

def adjust_volume(audio_file, target_dBFS):
    sound = AudioSegment.from_file(audio_file, format=audio_file[-3:])
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

def adjust_speed(input_file, output_file, speed=0.5):
    sound = AudioSegment.from_file(input_file)
    slowed_sound = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    }).set_frame_rate(sound.frame_rate)
    slowed_sound.export(output_file, format="mp3")

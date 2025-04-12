from IPython.display import Audio, Video, display

def play_audio(file, autoplay=True):
    display(Audio(file, autoplay=autoplay))

def play_video(file):
    Video(file, embed=True)

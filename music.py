from pygame import mixer

def play_music(file,stopper):
    mixer.init()
    mixer.music.load(file,stopper)
    mixer.music.set_volume(0.9)
    mixer.music.play()

if __name__ == '__main__':
    while True:
        play_music('Water.mp3','stop')

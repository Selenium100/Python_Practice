from pygame import mixer
from datetime import datetime
from time import time

def play_music(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(0.9)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open('log.txt' , 'a') as f:
        f.write(f"{datetime.now()} {msg}\n")


if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersec = 15*60
    eyessecs = 30*60
    exercisesecs = 45*60
    while True:
        if time() - init_water > watersec:
            print('Its time to Drink water and type stop to stop alarm')
            play_music('Water.mp3', 'stop')
            init_water = time()
            log_now('Drank Water')

        if time() - init_eyes > eyessecs:
            print('Its time to exercise your eyes and type stop to stop alarm')
            play_music('Exercise.mp3', 'stop')
            init_eyes = time()
            log_now('Eyes Relaxed')

        if time() - init_exercise > exercisesecs:
            print('Its time to physical exercise and type stop to stop alarm')
            play_music('Water.mp3', 'stop')
            init_exercise = time()
            log_now('Physical Exercise done')





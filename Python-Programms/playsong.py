import os
import random

def play_music():
    path = 'D:/songs'
    songs = os.listdir(path)
    print(songs)
    print(len(songs))
    ran = random.randint(0, len(songs))
    os.startfile(os.path.join(path, songs[ran]))


play_music()
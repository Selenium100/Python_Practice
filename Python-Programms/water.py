import time
from plyer import notification
from pygame import mixer
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def play_music(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(0.9)
    mixer.music.play()


while True:
    notification.notify(
        title='***Please Drink Water Now',
        message='Getting enough water every day is important for your health. Drinking water can prevent dehydration',
        app_icon='C:/Users/nitya/PycharmProjects/firsrproj/icon.ico',
        timeout=10,

    )
    speak("please drink water")
    time.sleep(6)


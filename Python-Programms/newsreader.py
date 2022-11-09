import pyttsx3
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

def speak(voice):
    engine.say(voice)
    engine.runAndWait()

res = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=acc9d6804dc54d999825718bf47cea34")
for i in range(19):
    print(res.json()["articles"][i]["content"])
    speak(f"{i} news is...")
    speak(res.json()["articles"][i]["content"])





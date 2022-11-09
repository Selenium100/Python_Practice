import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("goodmorning nitya")
    elif hour >= 12 and hour <= 18:
        speak("goodafternoon nitya")
    else:
        speak("goodevening nitya")

    speak("I am your alexa.. Please tell me how i help you?")


def takeCommandAndCovertString():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio,language='en-in')
        print(f'user said: {query}\n')
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommandAndCovertString().lower()


        if "wikipedia" in query:
            speak('searching from wikipedia..')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(result)





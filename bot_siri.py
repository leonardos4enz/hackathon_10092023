# Bot Siri

import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser


name = 'Diana'
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)
            return rec
    except sr.UnknownValueError:
        print("No se ha entendido la entrada de voz.")
        return ""
    except sr.RequestError as e:
        print(f"Error en la solicitud de reconocimiento de voz: {e}")
        return ""

def get_command():
    rec = input().lower()
    return rec

def run():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce ', '')
        talk('Reproduciendo ' + music)
        pywhatkit.playonyt(music)

run()


import datetime
import speech_recognition as sr
from custom_voices import speak
from src.commands import time, date


# While the speech recognition doesn't work, we'll query with the terminal
TERMINAL = 1


def takecommand():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    if TERMINAL == 0:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Ouvindo....')
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print('Analisando...')
            query = r.recognize_google(audio, language='pt-br')
        except sr.UnknownValueError:
            speak('Desculpe. Tente novamente')
            query = ''
    else:
        query = str(input("Comando >>> "))

    return query


def greet():
    hour = datetime.datetime.now().hour
    greeting = ""

    if 6 < hour <= 12:
        greeting = "bom dia"
    elif 12 < hour <= 18:
        greeting = "boa tarde"
    elif 18 < hour or hour <= 6:
        greeting = "boa noite"

    speak(f"{greeting}, como posso ajudar?")


def goodbye():
    hour = datetime.datetime.now().hour
    # speak("até logo")
    bye = "até logo,"

    if 6 < hour <= 12:
        speak(f"{bye} tenha um bom dia")
    elif 12 < hour <= 18:
        speak(f"{bye} tenha uma boa tarde")
    elif 18 < hour or hour <= 6:
        speak(f"{bye} tenha uma boa noite")
    exit()


if __name__ == "__main__":
    greet()
    while True:
        command = takecommand().lower()
        print(command)

        if not ('desligue' in command or 'pare' in command):
            print("--- Comando aceito ---")
        else:
            goodbye()

        if "bom dia" in command:
            speak('bom dia')

        elif "boa tarde" in command:
            speak('boa tarde')

        elif "boa noite" in command:
            speak('boa noite')

        elif "horas" in command:
            time()

        elif "dia" in command:
            date()

        else:
            speak("desculpe, não entendi")

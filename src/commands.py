import datetime
from custom_voices import speak


def time():
    currenttime = datetime.datetime.now().strftime("%H:%M")
    print(currenttime)
    speak(f"Agora são {currenttime}")


def date():
    currentdate = datetime.datetime.now().date()
    print(currentdate)
    speak(f"Hoje é {currentdate}")


if __name__ == "__main__":
    time()
    date()

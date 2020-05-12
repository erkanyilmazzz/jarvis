
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init()


# print(wikipedia.summary("osman pamukoglu"))


def take_coment():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"you:{query}\n")

    except Exception as e:
        print(e)
        print("sory say it again")
        return "none"

    return query


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak("how may ı help you")


def start():

    wishMe()
    wish = take_coment()
    words = wish.split(" ")
    for word in words:
        if(word == "close"):
            speak("good by")
            exit()

        if(word == "Google"):
            webbrowser.open("www.google.com")

        if(word == "Wikipedia"):
            speak("what will I search")
            sum = wikipedia.summary(take_coment())
            first_sentence = sum.split(".")
            print(first_sentence[0])
            speak(first_sentence[0])

        if(word == "YouTube"):
            webbrowser.open("www.youtube.com")

    start()


speak("hiii my name is jarvis.your personal asistant")
start()

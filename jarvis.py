import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        return command.lower()
    except:
        return ""

def main():
    speak("Hello Viraj, how can I help you?")
    while True:
        command = take_command()
        if "time" in command:
            speak(datetime.datetime.now().strftime("%H:%M:%S"))
        elif "open youtube" in command:
            webbrowser.open("https://youtube.com")
        elif "stop" in command:
            speak("Goodbye!")
            break

main()

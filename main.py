import tkinter as tk
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import wikipedia

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning, Sumit!")
    elif 12 <= hour < 18:
        speak("Good afternoon, Sumit!")
    else:
        speak("Good evening, Sumit!")
    speak("I am your desktop assistant. How can I help you today?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = r.listen(source, timeout=5)
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query.lower()
        except:
            speak("Sorry, I could not understand. Please say that again.")
            return ""

def process_command(command):
    if 'time' in command:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
    elif 'date' in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif 'open notepad' in command:
        os.system("notepad.exe")
    elif 'open calculator' in command:
        os.system("calc.exe")
    elif 'search wikipedia' in command:
        speak("What should I search on Wikipedia?")
        topic = take_command()
        if topic:
            result = wikipedia.summary(topic, sentences=2)
            speak("According to Wikipedia")
            speak(result)
    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com")
    elif 'exit' in command:
        speak("Goodbye, Sumit!")
        root.destroy()
    else:
        speak("I didn't understand that. Try saying it differently.")

def run_assistant():
    greet_user()
    while True:
        command = take_command()
        if command:
            process_command(command)
            if 'exit' in command:
                break

def start_gui():
    global root
    root = tk.Tk()
    root.title("Sumit Assistant")
    root.geometry("400x300")

    label = tk.Label(root, text="Welcome to Sumit Assistant", font=("Arial", 16))
    label.pack(pady=20)

    btn_start = tk.Button(root, text="Start Listening", command=run_assistant, bg="green", fg="white", font=("Arial", 12))
    btn_start.pack(pady=10)

    btn_exit = tk.Button(root, text="Exit", command=root.destroy, bg="red", fg="white", font=("Arial", 12))
    btn_exit.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    start_gui()

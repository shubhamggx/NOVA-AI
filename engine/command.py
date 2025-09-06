import pyttsx3
import speech_recognition as sr
import eel
import webbrowser
import time
import threading
import signal
import sys
import os

#  Initialize Eel
eel.init("web")  # Make sure you have a folder named 'web' with index.html inside
stop_flag = False
listening_flag = False  # Continuous listening ke liye

#  Speak function with voice and Eel output
def speak(text):
    text = str(text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Female voice 1 (use voices[0] for male)
    engine.setProperty('rate', 140)
    engine.setProperty('volume', 1.0)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()

#  Voice input function with feedback to user
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        eel.DisplayMessage(query)
        time.sleep(2)
        if "hashtag" in query:
            query = query.replace("hashtag", "").strip()
            if not query:
                return "None"
        return query.lower()

    except Exception as e:
        print("Say that again please...")
        eel.DisplayMessage("Say that again please...")

        return "None"


#  Core Command Execution Function
@eel.expose
def allCommands(message=1, continuous=False):
    if message == 1:
        query = takecommand()
        print(query)
    else:
        query = message
    
    try:
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            flag = ""
            contact_no, name = findContact(query)
            if contact_no != 0:
                if "send message" in query:
                    flag = 'message'
                    speak("what message to send")
                    query = takecommand()
                elif "phone call" in query:
                    flag = 'call'
                else:
                    flag = 'video call'
                whatsApp(contact_no, query, flag, name)
        else:
            from engine.features import query_openrouter
            query_openrouter(query)

        
        if not continuous:
            eel.ShowHood()

    except Exception as e:
        print("error:", e)
        eel.DisplayMessage("Something went wrong. Please try again.")
        speak("Something went wrong. Please try again.")
        if not continuous:
            eel.ShowHood()


# ------------------  Continuous Listening Part ------------------
def listening_loop():
    global listening_flag
    while listening_flag:
        query = takecommand()
        if query == "none":
            continue
        #elif query=="stop listning":
            #stoplisthening()
            # eel.showhood()
        print(f"Command received: {query}")
        allCommands (query, continuous=True)

@eel.expose
def start_listening():
    global listening_flag
    if not listening_flag:
        listening_flag = True
        threading.Thread(target=listening_loop, daemon=True).start()
        eel.DisplayMessage("Voice Assistant Started")
        print("Voice Assistant Started")

@eel.expose
def stop_listening():
    global listening_flag
    listening_flag = False
    eel.DisplayMessage("Voice Assistant Stopped")
    print("Voice Assistant Stopped")

# -----------------------------------------------------------------

@eel.expose
def stop_response():
    global stop_flag
    stop_flag = True
    engine = pyttsx3.init()
    engine.stop()
    print("AI response stopped.")
    eel.DisplayMessage("Response stopped.")
    eel.ShowHood()
    stop_flag = False

def signal_handler(sig, frame):
    global stop_flag
    stop_flag = True
    engine = pyttsx3.init()
    engine.stop()
    print("Application closing...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

@eel.expose
def on_close():
    print("Browser tab closed, stopping application...")
    signal_handler(None, None)
    os._exit(0)


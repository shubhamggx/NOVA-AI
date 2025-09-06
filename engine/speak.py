import pyttsx3
import threading
import eel

# Global engine instance
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice
engine.setProperty('rate', 140)
engine.setProperty('volume', 1.0)
engine_lock = threading.Lock()

def speak(text):
    text = str(text)
    eel.DisplayMessage(text)
    
    def run_speak():
        with engine_lock:
            engine.say(text)
            engine.runAndWait()
    
    threading.Thread(target=run_speak, daemon=True).start()

def stop_response():
    with engine_lock:
        try:
            engine.stop()
        except:
            pass

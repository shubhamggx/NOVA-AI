import re
from shlex import quote
import struct
import subprocess
from playsound import playsound
import eel
import pyaudio
import pyautogui
import requests
from engine.command import speak
from engine.config import ASSISTANT_NAME
import os
import pywhatkit as kit
import time
import webbrowser
import sqlite3
from engine.helper import extract_term, remove_words
import pvporcupine

# Connect to local database
conn = sqlite3.connect('my.db')
cursor = conn.cursor()

# Play assistant boot sound
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\audio.mp3"
    playsound(music_dir)

# Open applications or websites
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "").replace("open", "").strip().lower()
    app_name = query

    if app_name:
        try:
            # Check in system apps
            cursor.execute("SELECT path FROM sys_command WHERE LOWER(name) = ?", (app_name,))
            result = cursor.fetchone()
            if result:
                speak("Opening " + app_name)
                os.startfile(result[0])
                return

            # Check in website commands
            cursor.execute("SELECT url FROM web_command WHERE LOWER(name) = ?", (app_name,))
            result = cursor.fetchone()
            if result:
                speak("Opening " + app_name)
                webbrowser.open(result[0])
                return

            # Fallback to system command
            speak(f"opening...... '{app_name}' .")
            try:
                os.system(f'start {app_name}')
            except:
                speak("Still couldn't open it.")

        except Exception as e:
            speak("Something went wrong.")
            print(" Error:", e)
    else:
        speak("Please specify what you want me to open.")

# Play video/music on YouTube
def PlayYoutube(query):
    search_term = extract_term(query, "youtube")
    if search_term:
        speak("Playing " + search_term + " on YouTube")
        kit.playonyt(search_term)
        time.sleep(2)
        eel.ShowHood()
    else:
        speak("Sorry, I didn't understand what to play on YouTube.")
        eel.ShowHood()

# whatsapp
def findContact(query):
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        # if not mobile_number_str.startswith('+91'):
            # mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0


def whatsApp(mobile_no, message, flag, name):
    # Encode the message for URL
    encoded_message = quote(message)
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp chat
    subprocess.run(full_command, shell=True)
    time.sleep(5)  # Wait for WhatsApp to open

    # Click the send button automatically
    if flag == 'message':
        pyautogui.press('enter')
        speak(f"Message sent successfully to {name}")

    # Start a voice call using shortcut
    elif flag == 'call':
        pyautogui.hotkey('ctrl', 'shift', 'c')
        speak(f"Calling {name}")

    # Start a video call using shortcut
    elif flag == 'video':
        pyautogui.hotkey('ctrl', 'shift', 'v')
        speak(f"Starting video call with {name}")

def query_openrouter(prompt):
    from engine.config import api_key  # Make sure this points to your actual API key variable

    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "http://localhost",  # Required by OpenRouter
        "X-Title": "AI Voice Assistant",      # Optional, for dashboard
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek/deepseek-chat-v3-0324",
        "messages": [
            {"role": "system", "content":(
                "You are a smart, helpful, and friendly AI assistant."
                "Do not use emojis in your response. "
                "Avoid using any symbols or decorative characters.")},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    try:
        message = response.json()["choices"][0]["message"]["content"]
        print(message)
        speak(message)
    except Exception as e:
        print("Error:",e)
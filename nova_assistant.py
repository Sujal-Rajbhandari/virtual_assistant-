import time
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import pyautogui
import threading
import dateparser
import google.generativeai as genai
import requests
import win32gui 
import time

from dotenv import load_dotenv
time.sleep(10)  

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

genai.configure(api_key = GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def talk(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if "female" in voice.name.lower() or "zira" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print(f"Recognized: {command}")
        return command
    except:
        return ""

def get_active_window():
    # Get the active window title
    window = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(window)
    return window_title.lower()

def check_if_call_is_active():
    # Check if a calling app like WhatsApp, Skype, Discord is in the foreground
    active_window = get_active_window()
    print(f"Active window: {active_window}")

    # Check if the active window is related to a call (WhatsApp, Discord, etc.)
    calling_apps = ['whatsapp', 'skype', 'discord', 'zoom', 'teams', 'slack']
    return any(app in active_window for app in calling_apps)

def wait_for_wake_word():
    while True:
        # If a call is active, pause the assistant
        if check_if_call_is_active():
            print("A call is active. Pausing assistant.")
            time.sleep(5)  # Check every 5 seconds if the call has ended
            continue  # Skip activating the assistant while on a call
        
        command = listen()
        if "nova" in command:
            command = command.replace("nova", "").strip()
            if command:
                handle_command(command)
            else:
                talk("Yes, how can I assist you?")
                return

def increase_volume():
    for _ in range(5):
        pyautogui.press("volumeup")
    talk("Increased volume.")

def decrease_volume():
    for _ in range(5):
        pyautogui.press("volumedown")
    talk("Decreased volume.")

def play_youtube_song(song_name):
    query = song_name.replace(" ", "+")
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={query}&key={YOUTUBE_API_KEY}&type=video"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()
        if results["items"]:
            video_id = results["items"][0]["id"]["videoId"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            webbrowser.open(video_url)
            return f"Playing {song_name} on YouTube."
        else:
            return "No video found."
    else:
        return f"Error: {response.status_code}"

def set_reminder(command):
    # Try to extract the time-related part of the command
    words = command.lower().split("for", 1)
    if len(words) > 1:
        time_part = words[1].strip()
    else:
        talk("Sorry, I couldn't find the reminder time.")
        return

    reminder_time = dateparser.parse(time_part)
    if reminder_time:
        now = datetime.datetime.now()
        delay = (reminder_time - now).total_seconds()

        if delay > 0:
            talk(f"Reminder set for {reminder_time.strftime('%I:%M %p')}")
            threading.Timer(delay, lambda: talk("This is your reminder.")).start()
        else:
            talk("That time has already passed.")
    else:
        talk("Sorry, I couldn't understand the time.")


def gemini_query(query):
    try:
        response = model.generate_content(query)
        full_response = response.text.strip()

        sentences = full_response.split('. ')
        short_response = '. '.join(sentences[:2]) + '.' if len(sentences) > 1 else full_response

        return short_response
    except Exception as e:
        return f"Error with Gemini API: {str(e)}"

def handle_command(command):
    if "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        talk(f"The current time is {now}")
    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        talk(f"Today is {today}")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        talk("Opening YouTube")
    elif "play music" in command:
        song = command.replace("play music", "").strip()
        response = play_youtube_song(song)
        talk(response)
    elif "open browser" in command:
        os.system("start brave")
        talk("Opening Browser")
    elif "shutdown laptop" in command or "shutdown computer" in command:
        talk("Shutting down the laptop. Good Night Boss!")
        os.system("shutdown /s /t 1")
    elif "search" in command:
        query = command.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        talk(f"Searching for {query}")
    elif "stop" in command or "exit" in command:
        talk("Goodbye!")
        exit()
    elif "set reminder" in command:
        set_reminder(command)
    elif "what is" in command or "who is" in command or "tell me" in command or "where is" in command:
        answer = gemini_query(command)
        talk(answer)
    elif "increase volume" in command:
            increase_volume()

    elif "decrease volume" in command:
            decrease_volume()
    else:
        talk("Sorry, I didn't understand that.")

def nova():
    while True:
        wait_for_wake_word()
        while True:
            command = listen()
            if not command:
                continue
            handle_command(command)

if __name__ == "__main__":
    talk("Nova is online.")
    nova()
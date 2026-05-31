# Nova AI Voice Assistant

Nova is a Python-based desktop AI voice assistant that listens for voice commands, responds using text-to-speech, performs system automation tasks, and answers general questions using **Gemini 1.5 Flash**.

The assistant supports wake-word activation, YouTube music playback, web search, reminders, system volume control, browser launching, and call-aware behavior that pauses the assistant when a meeting or calling app is active.

---

## Features

* Wake-word activation using the keyword **"Nova"**
* Speech-to-text command recognition
* Text-to-speech voice responses
* Gemini 1.5 Flash integration for general question answering
* YouTube music playback using YouTube Data API
* Google web search through voice command
* Open YouTube and browser using voice command
* Increase and decrease system volume
* Set voice-based reminders
* Get current time and date
* Shutdown laptop using voice command
* Detect active calling apps such as WhatsApp, Skype, Discord, Zoom, Teams, and Slack
* Automatically pauses listening when a call or meeting app is active

---

## Project Structure

```bash
nova-ai-voice-assistant/
│
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* Gemini 1.5 Flash
* SpeechRecognition
* pyttsx3
* PyAudio
* pyautogui
* dateparser
* requests
* python-dotenv
* YouTube Data API
* win32gui

---

## How It Works

1. The assistant starts and says: **"Nova is online."**
2. It continuously listens for the wake word **"Nova"**.
3. After detecting the wake word, it listens for a command.
4. Based on the command, Nova performs an action such as:

   * answering a question
   * opening YouTube
   * playing music
   * searching Google
   * setting reminders
   * adjusting volume
   * shutting down the computer
5. For general questions, Nova sends the query to Gemini 1.5 Flash and speaks a short response.
6. If a call or meeting app is active, Nova pauses itself temporarily.

---

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd nova-ai-voice-assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

---

## Install Dependencies

Create a `requirements.txt` file:

```txt
SpeechRecognition
pyttsx3
pyautogui
dateparser
google-generativeai
requests
python-dotenv
pywin32
pyaudio
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
YOUTUBE_API_KEY=your_youtube_api_key_here
```

---

## Required API Keys

### Gemini API Key

Nova uses Gemini 1.5 Flash for answering general questions.

You need a Gemini API key and must save it in the `.env` file as:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### YouTube API Key

Nova uses the YouTube Data API to search and play songs on YouTube.

Save your YouTube API key in the `.env` file as:

```env
YOUTUBE_API_KEY=your_youtube_api_key_here
```

---

## How to Run

Run the assistant:

```bash
python main.py
```

When the assistant starts, it will say:

```text
Nova is online.
```

Then say:

```text
Nova
```

After that, give a command.

---

## Example Voice Commands

### Ask General Questions

```text
Nova, what is machine learning?
```

```text
Nova, who is Elon Musk?
```

```text
Nova, tell me about Nepal.
```

---

### Time and Date

```text
Nova, what is the time?
```

```text
Nova, what is today's date?
```

---

### Open Websites

```text
Nova, open YouTube
```

```text
Nova, search best AI tools
```

---

### Play Music

```text
Nova, play music Shape of You
```

---

### Volume Control

```text
Nova, increase volume
```

```text
Nova, decrease volume
```

---

### Reminder

```text
Nova, set reminder for 5 minutes
```

```text
Nova, set reminder for tomorrow at 9 AM
```

---

### System Command

```text
Nova, shutdown laptop
```

---

### Stop Assistant

```text
Nova, stop
```

```text
Nova, exit
```

---

## Main Functions

### `talk(text)`

Converts text into speech using `pyttsx3`.

### `listen()`

Uses the microphone to capture voice input and converts it into text using Google Speech Recognition.

### `wait_for_wake_word()`

Continuously listens for the wake word **"Nova"** before activating the assistant.

### `gemini_query(query)`

Sends the user query to Gemini 1.5 Flash and returns a short response.

### `play_youtube_song(song_name)`

Searches YouTube using the YouTube Data API and opens the top result in the browser.

### `set_reminder(command)`

Parses reminder time using `dateparser` and sets a reminder using `threading.Timer`.

### `check_if_call_is_active()`

Checks whether apps like WhatsApp, Skype, Discord, Zoom, Teams, or Slack are currently active.

### `handle_command(command)`

Routes the recognized command to the correct action.

---

## Notes

* This project is mainly designed for Windows because it uses `win32gui` and Windows-specific system commands.
* The `open browser` command uses `start brave`, so Brave browser should be installed.
* `shutdown laptop` will immediately shut down your computer.
* Speech recognition requires a working microphone.
* Internet connection is required for Gemini, Google Speech Recognition, YouTube search, and web search.

---

## Limitations

* Wake-word detection is basic and depends on Google Speech Recognition.
* The assistant may mishear commands in noisy environments.
* It currently does not support long conversation memory.
* Some commands are Windows-specific.
* YouTube playback depends on the YouTube Data API.
* The assistant only gives short Gemini responses by taking the first 1–2 sentences.

---

## Future Improvements

* Add continuous conversation memory
* Add better wake-word detection
* Add GUI interface
* Add cross-platform support for macOS and Linux
* Add local speech recognition
* Add calendar integration
* Add email sending support
* Add smart home control
* Add command confirmation before shutdown
* Add logging and error handling
* Add custom voice selection
* Add support for Nepali voice commands

---

## Author

**Sujal Rajbhandari**
AI/ML Engineer
Kathmandu, Nepal

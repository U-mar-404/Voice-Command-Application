# Voice Command Application (Pretrained ASR)

A simple, lightweight Voice Command Application built with Python using a pretrained Automatic Speech Recognition (ASR) system. The application records voice input via microphone, transcribes it using Google's pretrained ASR model, and executes corresponding actions based on predefined voice commands.

---

## 📌 Features

- **Microphone Input**: Captures live audio speech using PyAudio and SpeechRecognition.
- **Ambient Noise Calibration**: Automatically adjusts for background noise before listening.
- **Pretrained ASR**: Employs Google Speech Recognition API for fast, accurate speech-to-text conversion without requiring API keys.
- **Predefined Voice Commands & Actions**:
  1. 🕒 **Time Command (`"time"` / `"what time is it"`)**: Fetches and prints the current system time formatted in 12-hour AM/PM format.
  2. 😂 **Joke Command (`"joke"` / `"tell me a joke"`)**: Outputs a programming joke.
  3. 🌐 **Browser Command (`"open google"` / `"browser"`)**: Automatically launches the default web browser and navigates to Google.
- **Robust Error Handling**: Handles speech timeouts, unintelligible audio, and network connectivity errors gracefully.

---

## 🛠️ Requirements & Installation

### Prerequisites
- Python 3.8+
- macOS / Linux / Windows

### 1. Install System Dependencies (macOS)
On macOS, `pyaudio` requires `portaudio`:
```bash
brew install portaudio
```

### 2. Install Python Packages
```bash
pip install SpeechRecognition pyaudio
```

*(On Apple Silicon Macs, if needed)*:
```bash
CFLAGS="-I/opt/homebrew/include" LDFLAGS="-L/opt/homebrew/lib" pip install pyaudio
```

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/U-mar-404/Voice-Command-Application.git
   cd Voice-Command-Application
   ```

2. Run the application:
   ```bash
   python3 voice_command.py
   ```

3. Speak your command into the microphone when prompted:
   - *"What time is it?"*
   - *"Tell me a joke."*
   - *"Open Google."*

---

## 📋 Code Overview

```python
import speech_recognition as sr
import datetime
import webbrowser

recognizer = sr.Recognizer()

# Step 1: Capture speech from microphone
with sr.Microphone() as source:
    print("Adjusting for ambient noise... please wait 1 second.")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("\n>>> Listening now! Speak your command into the microphone... <<<")
    audio = recognizer.listen(source, timeout=8, phrase_time_limit=6)

# Step 2: Convert Speech to Text using Pretrained ASR
try:
    transcript = recognizer.recognize_google(audio).lower()
    print(f"\nASR Transcript: \"{transcript}\"")

    # Step 3 & 4: Voice Commands & Actions
    if "time" in transcript:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(f"Response: The current time is {current_time}.")

    elif "joke" in transcript:
        print("Response: Why do programmers prefer dark mode? Because light attracts bugs!")

    elif "open google" in transcript or "browser" in transcript:
        print("Response: Opening Google in your web browser...")
        webbrowser.open("https://www.google.com")

    else:
        print("Response: Unknown command. Try saying 'time', 'joke', or 'open google'.")

except sr.WaitTimeoutError:
    print("Error: No speech detected within the timeout period.")
except sr.UnknownValueError:
    print("Error: Could not understand audio.")
except sr.RequestError as e:
    print(f"Error connecting to ASR service: {e}")
```

---

## 🎯 Verification & Deliverables Checklist

| Requirement | Implementation | Status |
| :--- | :--- | :---: |
| **Speech Input** | Captured using `sr.Microphone()` with ambient noise calibration | ✅ |
| **Pretrained ASR** | Transcribed using `recognizer.recognize_google(audio)` | ✅ |
| **ASR Transcript** | Outputted to the console | ✅ |
| **Command 1** | `"time"` &rarr; displays current time | ✅ |
| **Command 2** | `"joke"` &rarr; prints programmer joke | ✅ |
| **Command 3** | `"open google"` &rarr; opens browser | ✅ |

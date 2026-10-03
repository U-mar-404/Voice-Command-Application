import speech_recognition as sr
import datetime
import webbrowser

# Initialize Recognizer (Pretrained ASR system)
recognizer = sr.Recognizer()

# Step 1: Capture speech from microphone
with sr.Microphone() as source:
    print("Adjusting for ambient noise... please wait 1 second.")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("\n>>> Listening now! Speak your command into the microphone... <<<")
    audio = recognizer.listen(source, timeout=8, phrase_time_limit=6)

# Step 2: Convert Speech to Text using Pretrained ASR (Google Web Speech API)
try:
    transcript = recognizer.recognize_google(audio).lower()
    print(f"\nASR Transcript: \"{transcript}\"")

    # Step 3 & 4: Three Predefined Voice Commands & Actions
    if "time" in transcript:
        # Command 1: Get current time
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(f"Response: The current time is {current_time}.")

    elif "joke" in transcript:
        # Command 2: Tell a joke
        print("Response: Why do programmers prefer dark mode? Because light attracts bugs!")

    elif "open google" in transcript or "browser" in transcript:
        # Command 3: Open browser
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

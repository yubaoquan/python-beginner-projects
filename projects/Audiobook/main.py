import pyttsx3
from PyPDF2 import PdfReader
import threading
import keyboard  # Import the keyboard library

pdf = None
stop_thread = False  # Variable to signal stopping the playback

def showLanguages(engine):
    voices = engine.getProperty('voices')

    for voice in voices:
        print(f"Voice: {voice.name}")
        print(f"ID: {voice.id}")
        print(f"Languages: {voice.languages}")
        print("-" * 20)
        if "English" in voice.name:
            engine.setProperty('voice', voice.id)
            print(f"Setting English voice: {voice.name}")
            break  # Exit after setting the voice

def play(pdfReader):
    global pdf
    global stop_thread

    speaker = pyttsx3.init()
    showLanguages(speaker)

    for page_num in range(len(pdfReader.pages)):
        text = pdfReader.pages[page_num].extract_text()
        sentences = text.split("\n")
        # forEach sentences, print each sentence and sentence index
        for sentenceIndex, sentence in enumerate(sentences):
            print(f"{sentenceIndex + 1}: {sentence}")
            if stop_thread:
                print("Playback stopped.")
                break  # Exit the loop if stop_thread is True
            speaker.say(sentence)
            speaker.runAndWait()
        if stop_thread:
            print("Outer loop: playback stopped.")
            break  # Exit the loop if stop_thread is True

    speaker.stop()


def stop_playback():
    global stop_thread
    input("Press Enter to stop playback...")
    stop_thread = True  # Set the flag to stop playback


file = input("Enter your PDF file name: ")

while True:
    try:
        pdf = PdfReader(file)
        break
    except Exception as e:
        print("An error occurred:\n", e)
        print("\nEnter the file name again:\n")
        file = input("Enter your PDF file name: ")

# Create a separate thread for playback
playback_thread = threading.Thread(target=play, args=(pdf,))
playback_thread.start()

# Start a thread for stopping playback with keyboard input
keyboard.add_hotkey("q", lambda: stop_playback())
keyboard.wait()  # Wait for the hotkey event
print(111)
# Wait for the playback to finish
playback_thread.join()
print(222)

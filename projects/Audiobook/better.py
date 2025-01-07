import pyttsx3
from PyPDF2 import PdfReader
import threading

stop_event = threading.Event()  # 用于线程间通信的事件

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
            break

def play(pdfReader):
    speaker = pyttsx3.init()
    showLanguages(speaker)

    for page_num in range(len(pdfReader.pages)):
        text = pdfReader.pages[page_num].extract_text()
        sentences = text.split("\n")
        for sentenceIndex, sentence in enumerate(sentences):
            print(f"{sentenceIndex + 1}: {sentence}")
            if stop_event.is_set():
                print("Playback stopped.")
                speaker.stop()
                return
            speaker.say(sentence)
            speaker.runAndWait()

    speaker.stop()
    print("Finished reading all pages.")

def stop_playback():
    input("Press Enter to stop playback...")
    stop_event.set()

file = input("Enter your PDF file name: ")

while True:
    try:
        pdf = PdfReader(file)
        break
    except Exception as e:
        print("An error occurred:\n", e)
        print("\nEnter the file name again:\n")
        file = input("Enter your PDF file name: ")

# 创建播放线程
playback_thread = threading.Thread(target=play, args=(pdf,))
playback_thread.start()

# 创建停止线程
stop_thread = threading.Thread(target=stop_playback)
stop_thread.start()

# 等待线程完成
playback_thread.join()
stop_thread.join()
print("Program terminated.")

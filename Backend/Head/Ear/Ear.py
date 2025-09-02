import speech_recognition as sr
import os
import threading
from mtranslate import translate
from colorama import Fore, Style, init

init(autoreset=True)

def print_loop():
    """Background console animation (non-blocking)."""
    while True:
        print(Fore.LIGHTGREEN_EX + "🎤 I am listening...", end="\r", flush=True)

def Trans_hindi_to_english(txt):
    """Translate Hindi text into English."""
    english_txt = translate(txt, to_language="en")
    return english_txt

def listen():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 4000        # sensitivity (lower -> more sensitive)
    recognizer.pause_threshold = 0.8          # seconds of silence before stopping
    recognizer.non_speaking_duration = 0.5    # wait before considering silence

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)  # calibrate 1 sec
        print(Fore.YELLOW + "🎙️ Speak now...")

        try:
            audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)
            print(Fore.LIGHTYELLOW_EX + "✅ Got it, recognizing...")

            # Recognize speech in Hindi
            recognized_txt = recognizer.recognize_google(audio, language="bn-IN")
            
            if recognized_txt:
                translated_txt = Trans_hindi_to_english(recognized_txt)
                print(Fore.BLUE + f"Mr Soham (Hindi): {recognized_txt}")
                print(Fore.CYAN + f"Translated (English): {translated_txt}")
                return translated_txt
            else:
                return ""

        except sr.UnknownValueError:
            print(Fore.RED + "❌ Could not understand")
            return ""
        except sr.RequestError:
            print(Fore.RED + "⚠️ API request failed")
            return ""

def main():
    # Start background printing animation
    threading.Thread(target=print_loop, daemon=True).start()

    while True:
        text = listen()
        if text:
            if "stop" in text.lower():
                print(Fore.RED + "👋 Stopping assistant.")
                break

if __name__ == "__main__":
    main()



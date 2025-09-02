# import asyncio
# import os
# import threading
# import edge_tts
# import pygame

# # Voice configuration
# VOICE = "en-AU-WilliamNeural"

# # Function to safely remove a file
# def remove_file(file_path):
#     try:
#         if os.path.exists(file_path):
#             os.remove(file_path)
#             print(f"Removed file: {file_path}")
#     except Exception as e:
#         print(f"Error removing file: {e}")

# # Function to play audio
# def play_audio(file_path):
#     try:
#         print("Playing audio...")
#         pygame.init()
#         pygame.mixer.init()
#         sound = pygame.mixer.Sound(file_path)
#         sound.play()
#         while pygame.mixer.get_busy():
#             pygame.time.delay(10)  # Wait 10ms while audio plays
#         pygame.quit()
#         remove_file(file_path)  # Delete after playback
#     except Exception as e:
#         print(f"Error during audio playback: {e}")

# # Async function to generate TTS and play it
# async def generate_tts(TEXT, output_file) -> None:
#     try:
#         print("\033[92mGenerating TTS...\033[0m")
#         communicator = edge_tts.Communicate(TEXT, VOICE)
#         await communicator.save(output_file)
        
#         # Play audio in a separate thread
#         thread = threading.Thread(target=play_audio, args=(output_file,))
#         thread.start()
#         thread.join()  # Wait until playback finishes
        
#     except Exception as e:
#         print(f"\033[91mError during TTS generation: {e}\033[0m")

# # High-level function to speak text
# def speak(TEXT, output_file=None):
#     if output_file is None:
#         output_file = os.path.join(os.getcwd(), "speak.mp3")
#     asyncio.run(generate_tts(TEXT, output_file))

# # Example usage
# if __name__ == "__main__":
#     speak("Hi, welcome to the world of Pico!")
#     speak("This is your AI voice assistant speaking.")



import asyncio
import os
import threading
import edge_tts
import pygame
import time
from queue import Queue

# Voice configuration
VOICE = "en-AU-WilliamNeural"

# Initialize pygame once (not on every call)
pygame.mixer.init()
print("Pygame mixer initialized")

# File management
AUDIO_QUEUE = Queue()
CURRENTLY_PLAYING = False

# Function to safely remove a file
def remove_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"Error removing file: {e}")

# Audio player thread function
def audio_player():
    global CURRENTLY_PLAYING
    while True:
        file_path = AUDIO_QUEUE.get()
        if file_path is None:  # Sentinel value to stop the thread
            break
            
        CURRENTLY_PLAYING = True
        try:
            sound = pygame.mixer.Sound(file_path)
            sound.play()
            while pygame.mixer.get_busy():
                pygame.time.delay(10)
            remove_file(file_path)
        except Exception as e:
            print(f"Error during audio playback: {e}")
        finally:
            CURRENTLY_PLAYING = False
            AUDIO_QUEUE.task_done()

# Start audio player thread
audio_thread = threading.Thread(target=audio_player, daemon=True)
audio_thread.start()

# Async function to generate TTS
async def generate_tts(TEXT, output_file) -> None:
    try:
        communicator = edge_tts.Communicate(TEXT, VOICE)
        await communicator.save(output_file)
        AUDIO_QUEUE.put(output_file)
    except Exception as e:
        print(f"Error during TTS generation: {e}")

# High-level function to speak text
def speak(TEXT, output_file=None):
    if output_file is None:
        output_file = os.path.join(os.getcwd(), f"speak_{int(time.time()*1000)}.mp3")
    
    # Run TTS generation in a separate thread to avoid blocking
    tts_thread = threading.Thread(
        target=lambda: asyncio.run(generate_tts(TEXT, output_file)),
        daemon=True
    )
    tts_thread.start()

# Pre-warm the TTS system by generating a small audio file upfront
def pre_warm_tts():
    """Generate a small audio file to warm up the TTS system"""
    warmup_file = os.path.join(os.getcwd(), "warmup.mp3")
    if not os.path.exists(warmup_file):
        print("Pre-warming TTS system...")
        asyncio.run(generate_tts("Hi", warmup_file))
        # Wait a moment for the file to be generated
        time.sleep(0.5)

# Pre-warm the TTS system when module is imported
pre_warm_tts()

# Cleanup function
def cleanup():
    """Clean up any remaining audio files and stop the audio thread"""
    AUDIO_QUEUE.put(None)  # Signal thread to stop
    # Remove any remaining audio files
    for file in os.listdir(os.getcwd()):
        if file.startswith("speak_") and file.endswith(".mp3"):
            remove_file(file)
    remove_file("warmup.mp3")

# Register cleanup on exit
import atexit
atexit.register(cleanup)

# Example usage
if __name__ == "__main__":
    speak("Hi, welcome to the world of Pico!")
    time.sleep(1)  # Wait a bit for the first message to process
    speak("This is your AI voice assistant speaking.")
    
    # Keep the program running long enough to hear the audio
    time.sleep(5)
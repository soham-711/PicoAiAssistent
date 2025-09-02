from Head.Ear.Ear import listen
from Head.Mouth.Mouth import speak
from Head.Brain.Brain import think

def main():
    while True:
        command = listen()  # Voice input
        if not command:
            continue

        print(f"User: {command}")
        response = think(command)  # <-- Brain + Gemini
        print(f"Jarvis: {response}")
        speak(response)  # Voice output

if __name__ == "__main__":
    main()

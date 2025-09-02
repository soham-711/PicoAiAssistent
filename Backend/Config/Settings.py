import os

# Put your Gemini key in system env: setx GEMINI_API_KEY "your-key"
GEMINI_API_KEY = "AIzaSyArl6e1AkGWn53blXONGLj-KeH3aGKbl2w"

# Common names → executable/command (extend as you like)
APP_ALIASES = {
    "chrome": "chrome",
    "notepad": "notepad",
    "vscode": r"code",     # assumes VS Code on PATH
    "calculator": "calc",
    "spotify": "spotify",
}

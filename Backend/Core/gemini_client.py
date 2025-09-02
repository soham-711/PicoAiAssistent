import google.generativeai as genai

genai.configure(api_key="AIzaSyArl6e1AkGWn53blXONGLj-KeH3aGKbl2w")

model = genai.GenerativeModel("gemini-1.5-flash")

def ask_gemini(query: str) -> str:
    try:
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        return f"[Gemini Error] {str(e)}"

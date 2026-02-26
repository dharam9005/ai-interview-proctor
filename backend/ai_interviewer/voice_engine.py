import pyttsx3

engine = pyttsx3.init('sapi5')  # Windows voice engine

voices = engine.getProperty('voices')

# Select female voice if available
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)

engine.setProperty('rate', 165)
engine.setProperty('volume', 1.0)

def speak(text):
    try:
        print("AI Interviewer:", text)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Voice Error:", e)
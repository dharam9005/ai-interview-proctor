from ai_interviewer.question_generator import generate_questions
from ai_interviewer.voice_engine import speak
from emotion_detection.emotion import start_emotion_detection
import threading

def start_interview(skills):
    # Start emotion detection in parallel (IMPORTANT)
    emotion_thread = threading.Thread(target=start_emotion_detection)
    emotion_thread.daemon = True
    emotion_thread.start()

    intro = "Hello, I am your AI interviewer. I have analyzed your resume. Let's begin the interview."
    speak(intro)

    questions = generate_questions(skills)

    for i, question in enumerate(questions):
        speak(f"Question {i+1}: {question}")

    speak("The interview is completed. Generating your performance feedback.")

    return questions
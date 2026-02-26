def generate_feedback(skills, emotions_detected):
    strong_topics = skills[:2] if len(skills) >= 2 else skills
    weak_topics = ["Advanced concepts", "Communication clarity"]

    confidence_score = 70  # Base score (can be dynamic later)

    if "fear" in emotions_detected or "nervous" in emotions_detected:
        confidence_score -= 15

    report = {
        "confidence_score": confidence_score,
        "strong_topics": strong_topics,
        "weak_topics": weak_topics,
        "emotion_summary": emotions_detected,
        "suggestion": "Improve weak topics and maintain confidence during answering."
    }

    return report
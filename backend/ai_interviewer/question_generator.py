import random

# Skill-based question bank
QUESTION_BANK = {
    "python": [
        "What are Python decorators?",
        "Explain list vs tuple in Python.",
        "What is multithreading in Python?"
    ],
    "java": [
        "Explain OOP concepts in Java.",
        "What is JVM and how it works?",
        "Difference between abstract class and interface?"
    ],
    "sql": [
        "What is normalization in SQL?",
        "Explain joins in SQL.",
        "What is indexing in databases?"
    ],
    "ai": [
        "What is machine learning?",
        "Difference between AI and Deep Learning?",
        "Explain supervised vs unsupervised learning."
    ],
    "data science": [
        "What is data preprocessing?",
        "Explain regression vs classification.",
        "What is feature engineering?"
    ]
}

def generate_questions(skills):
    questions = []
    
    for skill in skills:
        skill_lower = skill.lower()
        if skill_lower in QUESTION_BANK:
            questions.append(random.choice(QUESTION_BANK[skill_lower]))
    
    # Fallback if no skills detected
    if not questions:
        questions = [
            "Tell me about yourself.",
            "What are your strengths?",
            "Why should we hire you?"
        ]

    return questions
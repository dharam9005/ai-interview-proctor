import PyPDF2

def extract_text_from_pdf(file_path):
    text = ""
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
    except Exception as e:
        print("PDF Error:", e)

    return text


def extract_skills(text):
    skills_db = [
        "python", "java", "sql", "ai", "machine learning",
        "data science", "react", "javascript", "c++", "html", "css"
    ]

    found_skills = []
    text_lower = text.lower()

    for skill in skills_db:
        if skill in text_lower:
            found_skills.append(skill)

    if not found_skills:
        found_skills.append("general")

    return found_skills
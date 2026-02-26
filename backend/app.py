from fastapi import FastAPI, UploadFile, File
import shutil
import os
from resume_parser.parser import extract_text_from_pdf, extract_skills
from ai_interviewer.interview_flow import start_interview

# Import our modules
from resume_parser.parser import extract_text_from_pdf, extract_skills
from ai_interviewer.interview_flow import start_interview

# Create FastAPI app FIRST (VERY IMPORTANT)
app = FastAPI()

UPLOAD_FOLDER = "uploads"
latest_skills = []  # global storage for detected skills

# Create uploads folder if not exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.get("/")
def home():
    return {"message": "AI Interview Proctor Backend Running"}


@app.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...)):
    global latest_skills

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    # Save uploaded resume
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract resume text
    resume_text = extract_text_from_pdf(file_path)

    # Extract skills
    skills = extract_skills(resume_text)
    latest_skills = skills  # store for interview

    return {
        "message": "Resume uploaded & analyzed successfully",
        "detected_skills": skills
    }


@app.post("/start-interview/")
def start_ai_interview():
    global latest_skills

    if not latest_skills:
        return {"error": "No resume analyzed yet. Please upload resume first."}

    questions = start_interview(latest_skills)

    return {
        "message": "AI Interview Started",
        "skills_used": latest_skills,
        "questions_asked": questions
    }
# Step 0: Install required libraries before running
# pip install spacy python-docx
# python -m spacy download en_core_web_sm

from docx import Document
import spacy

# -----------------------------
# Step 1: Read DOCX Resume
# -----------------------------
def read_resume(file_path):
    doc = Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

resume_path = "C:/Users/Admin/ResumeScreener/Jagjit_Kaur_CV - Copy.docx"
resume_text = read_resume(resume_path)

# -----------------------------
# Step 2: Extract Skills
# -----------------------------
nlp = spacy.load("en_core_web_sm")

# Keywords to search in the resume
keywords = ["Python", "C++", "AI", "ML", "ROS", "Java", "Cloud", "React"]

def find_skills(text):
    doc = nlp(text)
    found = []
    for token in doc:
        for kw in keywords:
            if kw.lower() in token.text.lower():
                found.append(kw)
    return list(set(found))

skills = find_skills(resume_text)

# -----------------------------
# Step 3: Score Resume
# -----------------------------
skill_points = {"Python":5, "C++":6, "AI":7, "ML":6, "ROS":8, "Java":5, "Cloud":7, "React":6}

def score_resume(skills):
    total = 0
    for skill in skills:
        total += skill_points.get(skill,0)
    return total

resume_score = score_resume(skills)

# -----------------------------
# Step 4: Display Result
# -----------------------------
print("Skills found:", skills)
print("Resume score:", resume_score)

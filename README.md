# Resume-checker
**AI-Powered Resume Screener**

This project automatically reads resumes and extracts key skills, then calculates a score based on predefined skill points. It is designed to help HR teams or recruiters quickly screen resumes for required skills.

**Features**

Reads resumes in DOCX format
Extracts key skills such as Python, C++, AI, ML, ROS, Java, Cloud, React
Calculates a resume score based on skill points
Works locally on your computer with Python
Tech Stack
Python 3.13

****Libraries:

python-docx → read DOCX files
spaCy → process and analyze text
Compatible with Windows 11 (tested on HP laptop)

**Installation**

**Install required libraries:**

pip install spacy python-docx
python -m spacy download en_core_web_sm

**Usage**
Place your resume(s) in DOCX format in the project folder.
Update the resume_path in resume_checker.py or use input prompt:
resume_path = input("Enter the path of your resume: ")


**Run the script:**
python resume_checker.py

You will see output like:
Skills found: ['C++', 'ROS', 'ML', 'Python', 'AI']
Resume score: 32

**Customizing Skills and Scores**

Update the keywords list to include the skills you want to detect:
keywords = ["Python", "C++", "AI", "ML", "ROS", "Java", "Cloud", "React"]


Update skill_points to assign different weights to skills:
skill_points = {"Python":5, "C++":6, "AI":7, "ML":6, "ROS":8, "Java":5, "Cloud":7, "React":6}

**Future Improvements
**
Add support for PDF resumes
Create a web interface using FastAPI to upload resumes online

Export results to CSV or Excel

Integrate AI ranking algorithms for more accurate scoring

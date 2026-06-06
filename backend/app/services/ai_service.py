import os
from groq import Groq
from dotenv import load_dotenv
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_job_description(jd_text: str, resume_text: str = None):
    
    prompt = f"""
You are an expert career coach and job analyst.

Analyze the following job description and return a JSON response with exactly these 4 fields:

1. "jd_summary": A 2-3 sentence plain English summary of the role
2. "required_skills": A list of technical skills required for this job
3. "skill_gaps": A list of skills from required_skills that are NOT in the resume below
4. "resume_suggestions": One paragraph of specific advice on how to tailor the resume for this job

Job Description:
{jd_text}

Resume:
{resume_text if resume_text else "Not provided"}

Return ONLY a valid JSON object. No explanation. No markdown. No extra text.
Example format:
{{
  "jd_summary": "...",
  "required_skills": ["skill1", "skill2"],
  "skill_gaps": ["skill1"],
  "resume_suggestions": "..."
}}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )

    raw = response.choices[0].message.content
    result = json.loads(raw)
    return result
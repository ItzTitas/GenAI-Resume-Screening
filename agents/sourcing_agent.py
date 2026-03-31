# agents/sourcing_agent.py

import random

def source_candidates(job_description):
    # Keyword extraction from job description
    keywords = set(job_description.lower().split())

    # Simulated candidate database
    candidate_pool = [
        {"name": "Alice", "skills": ["Python", "Flask", "Docker"], "experience": 3},
        {"name": "Bob", "skills": ["Java", "Spring", "Microservices"], "experience": 5},
        {"name": "Charlie", "skills": ["JavaScript", "React", "Node.js"], "experience": 2},
        {"name": "Dana", "skills": ["Go", "Kubernetes", "Cloud"], "experience": 4},
        {"name": "Eli", "skills": ["Python", "FastAPI", "PostgreSQL"], "experience": 6},
    ]

    def match_score(candidate):
        return sum(1 for skill in candidate["skills"] if skill.lower() in keywords)

    # Filter and sort candidates based on skill match
    filtered = sorted(candidate_pool, key=match_score, reverse=True)

    return {"status": "success", "candidates": filtered[:3]}  # return top 3 matches

# For demo purposes
if __name__ == "__main__":
    jd = "Looking for backend developer with Python, Flask, and PostgreSQL experience"
    result = source_candidates(jd)
    print("Sourced Candidates:")
    for c in result["candidates"]:
        print(f"- {c['name']} | Skills: {', '.join(c['skills'])} | Experience: {c['experience']} yrs")

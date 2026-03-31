# agents/screening_agent.py

import random

def screen_candidates(candidates, job_description):
    keywords = set(job_description.lower().split())

    def score(candidate):
        skill_match = sum(1 for skill in candidate["skills"] if skill.lower() in keywords)
        experience = candidate.get("experience", 0)
        total_score = skill_match + (experience * 0.5)  # Give partial weight to experience

        feedback_options = [
            "Strong fit based on listed skills.",
            "Moderate alignment with job description.",
            "Skills slightly mismatch; needs further review.",
            "Excellent experience match.",
            "Potential candidate with relevant experience."
        ]
        feedback = random.choice(feedback_options)

        return {
            "name": candidate["name"],
            "score": total_score,
            "experience": experience,
            "feedback": feedback
        }

    return {"screened": [score(c) for c in candidates]}

# For demo purposes
if __name__ == "__main__":
    candidates = [
        {"name": "Rebecca Welton", "skills": ["management", "communication", "leadership"], "experience": 10},
        {"name": "Nathan Shelley", "skills": ["python", "data", "ai"], "experience": 3},
        {"name": "Dani Rojas", "skills": ["teamwork", "energy", "football"], "experience": 5}
    ]
    job_description = "Looking for a leader with strong communication, management and AI skills"

    result = screen_candidates(candidates, job_description)
    print("Screening Results:")
    for r in result["screened"]:
        print(f"- {r['name']} | Score: {r['score']} | Experience: {r['experience']} yrs | Feedback: {r['feedback']}")

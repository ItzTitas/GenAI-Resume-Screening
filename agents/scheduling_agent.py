# agents/scheduling_agent.py

import random
from datetime import datetime, timedelta

def get_random_time():
    times = ["9 AM", "10 AM", "11 AM", "2 PM", "3 PM", "4 PM"]
    return random.choice(times)

def get_random_mode():
    modes = ["Zoom", "Google Meet", "in-person", "Skype", "Microsoft Teams"]
    return random.choice(modes)

def get_random_day():
    days_ahead = random.randint(1, 5)
    return (datetime.now() + timedelta(days=days_ahead)).strftime("%A, %B %d")

def schedule_interview(candidate_name, recruiter_name):
    day = get_random_day()
    time = get_random_time()
    mode = get_random_mode()
    message = (
        f"Interview scheduled between {candidate_name} and {recruiter_name} "
        f"on {day} at {time} via {mode}."
    )
    return {
        "scheduled": True,
        "details": message
    }

# For demo purposes
if __name__ == "__main__":
    candidate = "Jamie Tartt"
    recruiter = "Keeley Jones"
    result = schedule_interview(candidate, recruiter)
    print("Scheduling Result:")
    print(result["details"])

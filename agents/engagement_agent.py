# agents/engagement_agent.py

import random

def get_random_greeting():
    greetings = [
        "Hello", "Hi", "Hey", "Greetings", "Good to connect with you"
    ]
    return random.choice(greetings)

def get_random_message():
    messages = [
        "thanks for showing interest. We'd love to know more about you!",
        "we’re excited to learn more about your background.",
        "it's great to have you here. Let's take the next step together.",
        "we're thrilled to connect. Let’s get started on your journey!",
        "thank you for applying! Let’s chat more about your experience."
    ]
    return random.choice(messages)

def engage_candidate(candidate_name):
    greeting = get_random_greeting()
    message = get_random_message()
    full_message = f"{greeting} {candidate_name}, {message}"
    return {
        "message": full_message
    }

# For demo purposes
if __name__ == "__main__":
    candidate = "Sam Obisanya"
    result = engage_candidate(candidate)
    print("Engagement Message:")
    print(result["message"])

# List of questions

questions = [
    {
        "question": "What is a key benefit of CI/CD pipelines?",
        "options": ["a) Reduces hardware costs", "b) Eliminates the need for testing", "c) Speeds up software delivery", "d) Improves monitoring accuracy"],
        "correct": "c"
    },
    {
        "question": "What is the main goal of Continuous Integration (CI)?",
        "options": ["a) Automate infrastructure setup", "b) Monitor application performance", "c) Frequently merge code changes and run automated tests", "d) Deploy code directly to production"],
        "correct": "c"
    },
    {
        "question": "Which of the following is an example of a CI/CD tool?",
        "options": ["a) Prometheus", "b) Jenkins", "c) Docker", "d) ELK Stack"],
        "correct": "b"
    },
    {
        "question": "Which of the following best describes Blue/Green Deployment?",
        "options": ["a) Gradually rolling out updates to servers", "b) Using two identical environments, one live and one for testing updates", "c) Updating environments directly without backups", "d) Replacing old infrastructure with new containers"],
        "correct": "b"
    },
    {
        "question": "Which deployment strategy prioritizes user feedback for a selected portion of all users in real-world conditions?",
        "options": ["a) Blue/Green Deployment", "b) Canary Deployment", "c) Rolling Deployment", "d) Immutable Infrastructure"],
        "correct": "b"
    },
    {
        "question": "Which type of maintenance involves making changes to enable possible future iterations in deployed software?",
        "options": ["a) Adaptive Maintenance", "b) Corrective Maintenance", "c) Perfective Maintenance", "d) Preventive Maintenance"],
        "correct": "d"
    },
    {
        "question": "What is the role of Logstash in the ELK Stack?",
        "options": ["a) Collects and processes log data", "b) Performs search operations on log data", "c) Visualizes log data", "d) Tracks application metrics"],
        "correct": "a"
    },
    {
        "question": "What is a Jenkinsfile?",
        "options": ["a) A configuration file for Docker containers", "b) A log analysis file", "c) A file defining CI/CD pipeline stages", "d) A monitoring configuration"],
        "correct": "c"
    },
    {
        "question": "Which testing method focuses on individual components of a system?",
        "options": ["a) Unit Testing", "b) Integration Testing", "c) Load Testing", "d) Regression Testing"],
        "correct": "a"
    }
]

# Function to run the quiz
def run_quiz():
    score = 0
    total_marks = 5 #marks for each question

    # Looping through the questions
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q["options"]:
            print(option)

        # Take user's answer
        answer = input("Enter your answer (a, b, c, or d): ").strip().lower()

        # Check if the answer is correct
        if answer == q["correct"]:
            print("Correct!")
            score += total_marks
        else:
            print("Incorrect!")

    # Calculate and display the roral score
    print(f"\nYour total score is: {score}/{len(questions) * total_marks}")

run_quiz()


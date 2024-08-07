def ask_question(question, options):
    """
    Asks a question and returns the user's answer.

    Args:
        question (str): The question to ask.
        options (list): A list of possible answers.

    Returns:
        int: The user's answer.
    """
    print("\n" + question)
    for index, option in enumerate(options, 1):
        print(f"{index}. {option}")
    
    while True:
        try:
            answer = int(input("Enter the number of your answer: "))
            if 1 <= answer <= len(options):
                return answer
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_maturity_score(answers):
    """
    Calculates the maturity score based on the user's answers.

    Args:
        answers (list): A list of the user's answers.

    Returns:
        int: The maturity score.
    """
    maturity_score = sum(answers)
    return maturity_score

def get_result(maturity_score):
    """
    Returns the result based on the maturity score.

    Args:
        maturity_score (int): The maturity score.

    Returns:
        str: The result.
    """
    if maturity_score <= 10:
        return "You have some growing up to do."
    elif 11 <= maturity_score <= 20:
        return "You're somewhat mature, but there's room for improvement."
    elif 21 <= maturity_score <= 30:
        return "You're mature and responsible, but can still learn more."
    else:
        return "You're very mature and handle things well!"

def main():
    questions = [
        {
            "question": "How do you handle conflict?",
            "options": [
                "Avoid it and hope it goes away.",
                "Get angry and argue.",
                "Try to understand the other person's perspective and find a compromise.",
                "Ignore the other person completely."
            ]
        },
        {
            "question": "How do you spend your free time?",
            "options": [
                "Playing video games all day.",
                "Hanging out with friends and partying.",
                "Reading books or learning new things.",
                "Watching TV shows or movies."
            ]
        },
        {
            "question": "How do you react to criticism?",
            "options": [
                "Get defensive and argue back.",
                "Feel hurt and dwell on it.",
                "Consider it and see if there’s any truth to it.",
                "Ignore it completely."
            ]
        },
        {
            "question": "How do you manage your responsibilities?",
            "options": [
                "Procrastinate until the last minute.",
                "Do them when you feel like it.",
                "Make a plan and stick to it.",
                "Forget about them."
            ]
        },
        {
            "question": "How do you handle stress?",
            "options": [
                "Complain about it to everyone.",
                "Ignore it and hope it goes away.",
                "Find healthy ways to manage it, like exercise or meditation.",
                "Take it out on others."
            ]
        },
        {
            "question": "How do you prioritize your goals?",
            "options": [
                "I don't really have any goals.",
                "I have goals, but I don't really prioritize them.",
                "I prioritize my goals, but I don't always follow through.",
                "I prioritize my goals and make a plan to achieve them."
            ]
        },
        {
            "question": "How do you handle change?",
            "options": [
                "I hate change and try to avoid it.",
                "I'm not a fan of change, but I can adapt.",
                "I'm neutral about change.",
                "I love change and see it as an opportunity for growth."
            ]
        },
        {
            "question": "How do you handle difficult decisions?",
            "options": [
                "I avoid making difficult decisions.",
                "I make impulsive decisions without thinking them through.",
                "I take my time and weigh my options carefully.",
                "I seek input and advice from others."
            ]
        },
        {
            "question": "How do you prioritize self-care?",
            "options": [
                "I don't really prioritize self-care.",
                "I prioritize self-care, but only when I have time.",
                "I make time for self-care, but it's not a priority.",
                "I prioritize self-care and make it a regular part of my routine."
            ]
        },
        {
            "question": "How do you handle relationships?",
            "options": [
                "I struggle with relationships and often find myself in conflict.",
                "I have okay relationships, but they could be better.",
                "I have good relationships, but I could improve my communication skills.",
                "I have great relationships and communicate effectively."
            ]
        }
    ]

    answers = []
    for question in questions:
        answer = ask_question(question["question"], question["options"])
        answers.append(answer)

    maturity_score = calculate_maturity_score(answers)
    result = get_result(maturity_score)

    print("\nYour maturity score is:", maturity_score)
    print(result)

if __name__ == "__main__":
    main()

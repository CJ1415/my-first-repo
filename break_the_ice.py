import random

# list of random responses to be given after each answer
responses = [
    "Cool! "
    "Nice! "
    "Wow, great! "
    "Amazing! "
    "Awesome! "
]

# Function to ask a question and provide a random response
def ask_question(question):
    answer = input(question + " ")
    print(random.choice(responses))
    print() # for spacing between questions

# List of questions to be filled in by students
questions = [
    "Whats your favourite hobby?", # example question
    "Whats your favourite movie?",
    "What do you study?",
    "What are your favourite foods?",
]

# Function to randomly select and ask two questions
def icebreaker():
    print("Let's break the ice! I'll ask you two random questions:")
    selected_questions = random.sample(questions, 2) # Randomly select 2 questions
    for question in selected_questions:
        ask_question(question)

# Call the icebreaker function to start the program
icebreaker()
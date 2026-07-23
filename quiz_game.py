import re
import os
import random

class User:
    total_users = 0

    def __init__(self, username):
        self.username = username
        User.total_users += 1

    def get_profile_info(self):
        return f"User: {self.username}"

class Player(User):
    def __init__(self, username, score=0):
        super().__init__(username)
        self.score = score

    def update_score(self, points):
        self.score += points

    def get_profile_info(self):
        return f"Player: {self.username} | Current Score: {self.score}"

class Question:
    def __init__(self, prompt, answer, category):
        self.prompt = prompt
        self.answer = answer.strip().lower()
        self.category = category

    def check_answer(self, user_answer):
        cleaned_user_ans = re.sub(r'\s+', ' ', user_answer.strip().lower())
        return cleaned_user_ans == self.answer

def create_sample_question_file():
    if not os.path.exists("questions.txt"):
        sample_data = (
            "What keyword is used to inherit from a parent class in Python?|super|OOP\n"
            "Which module in Python is used for regular expressions?|re|Libraries\n"
            "What built-in exception is raised when dividing a number by zero?|zerodivisionerror|Exceptions\n"
            "What is the file extension for Python source files?|.py|Basics\n"
            "Which OOP principle hides internal data details?|encapsulation|OOP\n"
        )
        with open("questions.txt", "w") as f:
            f.write(sample_data)

def load_questions():
    create_sample_question_file()
    question_list = []

    try:
        with open("questions.txt", "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    prompt, answer, category = parts
                    question_list.append(Question(prompt, answer, category))
    except IOError:
        print("Error: Could not read the questions file.")

    return question_list

def save_high_score(username, score):
    try:
        with open("high_scores.txt", "a") as file:
            file.write(f"{username},{score}\n")
    except IOError:
        print("Error: Could not save score to file.")

def view_high_scores():
    if not os.path.exists("high_scores.txt"):
        print("\nNo high scores recorded yet.")
        return
    print("\n--- Leaderboard ---")
    try:
        with open("high_scores.txt", "r") as file:
            scores = file.readlines()
            for score_line in scores:
                parts = score_line.strip().split(",")
                if len(parts) == 2:
                    print(f"User: {parts[0]} | Score: {parts[1]}")
    except IOError:
        print("Error reading leaderboard file.")

def main():
    print("=== Welcome to the Python Quiz Bowl Master ===")

    questions = load_questions()
    if not questions:
        print("No questions available to play.")
        return
    
    while True:
        print("\nMenu:")
        print("1. Play Quiz")
        print("2. View Leaderboard")
        print("3. Exit")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            username = input("Enter your player name: ").strip()
            if not username:
                username = "Anonymous"

            current_player = Player(username)
            print(f"\nLet's begin, {current_player.username}! GOOD LUCK.")

            game_questions = random.sample(questions, min(3, len(questions)))

            for i, q in enumerate(game_questions, 1):
                print(f"\nQuestion {i} [{q.category}]")
                print(q.prompt)

                ans = input("Your answer: ")

                if q.check_answer(ans):
                    print("Correct! +10 points.")
                    current_player.update_score(10)
                else:
                    print(f"Incorrect. The correct answer was: {q.answer}")

            print(f"\nQuiz Over! {current_player.get_profile_info()}")
            save_high_score(current_player.username, current_player.score)

        elif choice == "2":
            view_high_scores()

        elif choice == "3":
            print(f"Total user sessions tracked (Class Variable): {User.total_users}")
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
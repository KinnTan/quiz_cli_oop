from random import shuffle
from core.ui_utils import UIManager
from core.file_utils import FileManager

# Handles the process of loading and running a quiz
class QuizManager:
    def __init__(self):
        # Initialize UI and FileManager, and set up tracking variables
        self.ui = UIManager()
        self.file_manager = FileManager(self.ui)
        self.questions = []
        self.correct = 0
        self.progress = 0

    # Load a quiz from a file and randomize its questions
    def load(self):
        data = self.file_manager.select_quiz_file()  # Prompt user to select a quiz file
        if data is None:
            return False  # Exit if no quiz is selected
        shuffle(data)  # Randomize question order
        self.questions = data  # Store questions
        return True

    # Run the quiz by displaying questions and collecting answers
    def run(self):
        while self.progress < len(self.questions):  # Continue until all questions are answered
            self.ui.clear_screen()
            self.ui.display_logo("title_logo")
            self.ui.progress_bar(self.progress, len(self.questions))

            # Display the current question and its choices
            question = self.questions[self.progress]
            print(f"\n\033[97m{question['question']}\033[0m")
            for letter, answer in question['choices'].items():
                print(f"\033[97m\033[01m{letter}. \033[93m{answer}\033[0m")

            # Get user input and validate answer
            user_response = input("\n\033[97mYour answer: \033[0m").strip().lower()
            if user_response in ["a", "b", "c", "d"]:
                if user_response == question['correct_answer']:
                    self.correct += 1  # Track correct answers
                self.progress += 1  # Move to next question
            else:
                print("\033[91mInvalid letter. Try again.\033[0m")

        self.show_result()  # Display final results

    # Show the user's final quiz score with color-coded feedback
    def show_result(self):
        score = self.correct / len(self.questions)
        color = "\033[92m" if score >= 0.8 else "\033[93m" if score >= 0.5 else "\033[91m"
        self.ui.loading_animation(0.3, "\x1b[38;5;37mGetting Results...\x1b[0m")
        self.ui.clear_screen()
        self.ui.display_logo("start_logo")
        print(f"\x1b[38;5;74mQuiz Complete! Your final score: {color}\033[01m{self.correct}/{len(self.questions)}\033[0m")
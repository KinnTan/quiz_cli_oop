from core.ui_utils import UIManager
from core.file_utils import FileManager

class QuizBuilder:
    def __init__(self):
        self.ui = UIManager()
        self.file_manager = FileManager(self.ui)
        self.data = []

    def start(self):
        self.ui.clear_screen()
        self.ui.display_logo("builder_logo")
        while True:
            question = self.get_question()
            if question is None:
                break
            choices = self.get_choices()
            correct = self.get_correct_choice()
            self.data.append({
                "question": question,
                "choices": choices,
                "correct_answer": correct
            })
            self.ui.loading_animation(0.9, "Storing question...")
            self.ui.clear_screen()
            print("\rQuestion stored successfully")
        filename = self.file_manager.save_quiz(self.data)
        print(f"\nSaved quiz to \033[093m{filename}\033[0m")

    def get_question(self):
        while True:
            question = input("Enter the question [type 'exit' to save and quit]:\n")
            if question.lower() == "exit":
                return None
            elif question.strip() == "":
                print("Please enter a question.")
            else:
                return question

    def get_choices(self):
        choices = {}
        for letter in ["a", "b", "c", "d"]:
            choices[letter] = input(f"Choice {letter.upper()}: ")
        return choices

    def get_correct_choice(self):
        while True:
            correct = input("Which is the correct choice (a/b/c/d): ").lower()
            if correct in ["a", "b", "c", "d"]:
                return correct
            else:
                print("Invalid choice. Please enter a, b, c, or d.")

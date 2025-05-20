from random import shuffle
from core.ui_utils import UIManager
from core.file_utils import FileManager

class QuizManager:
    def __init__(self):
        self.ui = UIManager()
        self.file_manager = FileManager(self.ui)
        self.questions = []
        self.correct = 0
        self.progress = 0

    def load(self):
        data = self.file_manager.select_quiz_file()
        if data is None:
            return False
        shuffle(data)
        self.questions = data
        return True

    def run(self):
        while self.progress < len(self.questions):
            self.ui.clear_screen()
            self.ui.display_logo("title_logo")
            self.ui.progress_bar(self.progress, len(self.questions))

            question = self.questions[self.progress]
            print(f"\n\033[97m{question['question']}\033[0m")
            for letter, answer in question['choices'].items():
                print(f"\033[97m\033[01m{letter}. \033[93m{answer}\033[0m")

            user_response = input("\n\033[97mYour answer: \033[0m").strip().lower()
            if user_response in ["a", "b", "c", "d"]:
                if user_response == question['correct_answer']:
                    self.correct += 1
                self.progress += 1
            else:
                print("\033[91mInvalid letter. Try again.\033[0m")

        self.show_result()

    def show_result(self):
        score = self.correct / len(self.questions)
        color = "\033[92m" if score >= 0.8 else "\033[93m" if score >= 0.5 else "\033[91m"
        self.ui.loading_animation(0.3, "\x1b[38;5;37mGetting Results...\x1b[0m")
        self.ui.clear_screen()
        self.ui.display_logo("start_logo")
        print(f"\x1b[38;5;74mQuiz Complete! Your final score: {color}\033[01m{self.correct}/{len(self.questions)}\033[0m")
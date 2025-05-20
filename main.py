from core.ui_utils import UIManager
from core.quiz import QuizManager
from core.quiz_builder import QuizBuilder

def main():
    ui = UIManager()
    while True:
        ui.clear_screen()
        ui.display_logo("start_logo")
        print("\n\033[96mWelcome to QuizCLI!\033[0m")
        print("\033[93m[1]\033[0m Take a Quiz")
        print("\033[93m[2]\033[0m Create a Quiz")
        print("\033[93m[3]\033[0m Exit")

        choice = input("\n\033[96mEnter your choice: \033[0m").strip()

        if choice == "1":
            quiz = QuizManager()
            if quiz.load():
                quiz.run()
            input("\nPress Enter to return to the menu...")
        elif choice == "2":
            builder = QuizBuilder()
            builder.start()
            input("\nPress Enter to return to the menu...")
        elif choice == "3":
            print("\033[91mExiting QuizCLI. Goodbye!\033[0m")
            break
        else:
            print("\033[91mInvalid choice. Please enter 1, 2, or 3.\033[0m")
            input("\nPress Enter to try again...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\033[91m\nExiting...\033[0m")

import os
import json
from core.validator import Validator

class FileManager:
    def __init__(self, ui):
        self.ui = ui
        self.validator = Validator()

    def list_quiz_files(self):
        for files in os.listdir():
            if files.endswith('json'):
                return files

    def unique_filename(self, base="quiz_data.json"):
        if not os.path.exists(base):
            return base
        counter = 1
        while True:
            new_filename = f"quiz_data_{counter}.json"
            if not os.path.exists(new_filename):
                return new_filename
            counter += 1

    def save_quiz(self, data):
        filename = self.unique_filename()
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_quiz(self, filepath):
        with open(filepath, "r") as file:
            return json.load(file)

    def select_quiz_file(self):
        self.ui.clear_screen()
        self.ui.display_logo("start_logo")
        self.ui.loading_animation(0.25, "\x1b[38;5;117mScanning current directory for files...")
        self.ui.clear_screen()
        self.ui.display_logo("start_logo")

        files = self.list_quiz_files()
        if not files:
            print("\033[91mNo quiz files found. Create one using the builder.\033[0m")
            return None

        for number, file in enumerate(files, 1):
            print(f"\033[97m\033[01m{number}. \033[0m\033[093m{file}\033[0m")

        while True:
            try:
                choice = int(input("\nSelect a file by number: "))
                if 1 <= choice <= len(files):
                    filename = files[choice - 1]
                    if error := self.validator.validate_json(filename):
                        print(error)
                        continue
                    data = self.load_quiz(filename)
                    if not self.validator.is_valid_quiz(data):
                        print("\033[91mInvalid quiz structure.\033[0m")
                        continue
                    return data
                else:
                    print("Invalid selection.")
            except ValueError:
                print("\x1b[38;5;74m\033[01mEnter a number.")
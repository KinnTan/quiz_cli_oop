import os
import json
from core.validator import Validator

# FileManager handles saving, loading, listing, and selecting quiz JSON files
class FileManager:
    def __init__(self, ui):
        # Initialize with a UI manager and a Validator instance
        self.ui = ui
        self.validator = Validator()

    # Lists all quiz files in the current directory that end with .json
    def list_quiz_files(self):
        for files in os.listdir():  # Iterate through all files in the current directory
            if files.endswith('json'):  # Check if the file ends with .json
                return files  # Return the filename

    # Ensures the saved file has a unique name (prevents overwriting)
    def unique_filename(self, base="quiz_data.json"):
        # If the base filename does not exist, return it
        if not os.path.exists(base):
            return base
        counter = 1
        # Otherwise, keep trying new numbered filenames until an unused one is found
        while True:
            new_filename = f"quiz_data_{counter}.json"
            if not os.path.exists(new_filename):
                return new_filename
            counter += 1

    # Saves quiz data to a uniquely named JSON file
    def save_quiz(self, data):
        filename = self.unique_filename()  # Generate a unique filename
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)  # Write JSON data to file with indentation
        return filename  # Return the filename used

    # Loads and returns quiz data from the specified JSON file
    def load_quiz(self, filepath):
        with open(filepath, "r") as file:
            return json.load(file)  # Read and parse JSON data

    # Displays quiz files in a list and lets the user choose one
    def select_quiz_file(self):
        self.ui.clear_screen()
        self.ui.display_logo("start_logo")

        # Display a short loading animation while scanning the directory
        self.ui.loading_animation(0.25, "\x1b[38;5;117mScanning current directory for files...")
        self.ui.clear_screen()
        self.ui.display_logo("start_logo")

        # Get a list of available quiz files
        files = self.list_quiz_files()
        if not files:
            print("\033[91mNo quiz files found. Create one using the builder.\033[0m")
            return None  # Exit early if no quiz files found

        # Display the available quiz files with numbers
        for number, file in enumerate(files, 1):
            print(f"\033[97m\033[01m{number}. \033[0m\033[093m{file}\033[0m")

        # Loop to let the user select a quiz file by number
        while True:
            try:
                choice = int(input("\nSelect a file by number: "))
                if 1 <= choice <= len(files):
                    filename = files[choice - 1]

                    # Validate if selected file is a proper JSON
                    if error := self.validator.validate_json(filename):
                        print(error)
                        continue

                    # Load the quiz data
                    data = self.load_quiz(filename)

                    # Validate the structure of the quiz file
                    if not self.validator.is_valid_quiz(data):
                        print("\033[91mInvalid quiz structure.\033[0m")
                        continue

                    return data  # Return valid quiz data
                else:
                    print("Invalid selection.")  # Number out of range
            except ValueError:
                print("\x1b[38;5;74m\033[01mEnter a number.")  # Non-integer input
import json

# Validates quiz JSON files and their internal structure
class Validator:
    # Check if a given file is a readable JSON file
    def validate_json(self, filename):
        if not filename.endswith(".json"):
            return "\033[91mThat is not a JSON file. Please select a file with a .json extension.\033[0m"
        try:
            json.load(open(filename))
        except json.decoder.JSONDecodeError:  # Handle empty or invalid JSON
            return "\033[91mThat JSON file is empty or corrupted. Please select a different file.\033[0m"
        return None # File is valid

    # Checks that the JSON quiz file has the expected structure
    def is_valid_quiz(self, data):
        for question_item in data:
            try:
                (question_item["question"])
            except KeyError:
                return False
            try:
                question_item["choices"]
            except KeyError:
                return False
            try:
                question_item["correct_answer"]
            except KeyError:
                return False
            for choice_letter in question_item["choices"]:
                try:
                    (question_item["choices"][choice_letter])
                except KeyError:
                    return False # Any missing key means invalid quiz structure
        return True

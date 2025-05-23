from assets.logos import get_logo
import os
import time

# Handles all UI-related operations like animations and screen output
class UIManager:
    def __init__(self):
        self.spinner_frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

    # Clears the terminal screen
    def clear_screen(self):
        os.system('cls')

    # Displays an ASCII logo by name
    def display_logo(self, name):
        print(get_logo(name))

    # Displays a loading animation with spinner and message
    def loading_animation(self, duration, message):
        start = time.time()
        while time.time() - start < duration:
            for frame in self.spinner_frames:
                print(f"\r{frame} {message}", end="", flush=True)
                time.sleep(0.1)
                if time.time() - start >= duration:
                    break
        print("\r", end="")  # Clear line after animation ends

    # Shows a visual progress bar for quiz completion
    def progress_bar(self, current, total, bar_length=50):
        percentage = current / total
        filled = int(bar_length * percentage)
        bar = '\x1b[38;5;37m█\033[0m' * filled + '\033[97m-' * (bar_length - filled)
        print(f"\r\x1b[38;5;74mProgress: \033[97m|{bar}| \x1b[38;5;74m{current}/{total} ({percentage*100:.0f}%)\033[0m", flush=True)

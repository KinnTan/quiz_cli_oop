from assets.logos import get_logo
import os
import time

class UIManager:
    def __init__(self):
        self.spinner_frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

    def clear_screen(self):
        os.system('cls')

    def display_logo(self, name):
        print(get_logo(name))

    def loading_animation(self, duration, message):
        start = time.time()
        while time.time() - start < duration:
            for frame in self.spinner_frames:
                print(f"\r{frame} {message}", end="", flush=True)
                time.sleep(0.1)
                if time.time() - start >= duration:
                    break
        print("\r", end="")

    def progress_bar(self, current, total, bar_length=50):
        percentage = current / total
        filled = int(bar_length * percentage)
        bar = '\x1b[38;5;37m█\033[0m' * filled + '\033[97m-' * (bar_length - filled)
        print(f"\r\x1b[38;5;74mProgress: \033[97m|{bar}| \x1b[38;5;74m{current}/{total} ({percentage*100:.0f}%)\033[0m", flush=True)

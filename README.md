# QuizCLI (Builder + Runner)

## Overview

QuizCLI is a complete terminal-based quiz application that lets you **create**, **store**, and **take** multiple-choice quizzes using a user-friendly command-line interface.

It combines the features of:

* **[Quiz Builder CLI](https://github.com/KinnTan/quiz_builder_cli)** — to build quizzes interactively and save them as `.json` files
* **[Quiz CLI](https://github.com/KinnTan/quiz_cli)** — to take saved quizzes with animated UI, progress tracking, and results display

The application is structured using **object-oriented principles** and is fully modular.

## Requirements

* Python 3.x
* No external libraries required (only standard Python modules: `json`, `os`, `time`, `random`)

## Installation

**Option 1: Clone the Repository**

```bash
git clone https://github.com/KinnTan/quiz_cli_oop.git
cd quiz_cli_oop
```

**Option 2: Download from Release**

1. Visit the [Releases](https://github.com/KinnTan/quiz_cli_oop/releases) page.
2. Download the latest `.zip` or `.tar.gz` file.
3. Extract and open the folder in your terminal.

## Usage

### 1. Start the program

Run the main interface:

```bash
python main.py
```

You will be presented with a menu:

```
Welcome to QuizCLI!
[1] Take a Quiz
[2] Create a Quiz
[3] Exit
```

---

### 2. Creating a Quiz

* Choose option `2` from the menu.
* Enter a question and 4 answer choices (A–D).
* Choose the correct answer.
* Type `exit` when finished to save the quiz as a `.json` file.

Example:

```
Enter the question [type 'exit' to save and quit]:
What is the square root of 49?
Enter the choices
Choice A: 6
Choice B: 7
Choice C: 8
Choice D: 9
Which is the correct choice (a/b/c/d): b
Question stored successfully
...
Saved quiz to quiz_data.json
```

---

### 3. Taking a Quiz

* Choose option `1` from the menu.
* Select a `.json` quiz file.
* Answer the questions using letter choices (a–d).
* The interface will show your progress and final score.

Example:

```
Scanning current directory for files...
1. quiz_data.json
2. math_quiz.json

Enter the number corresponding to your quiz file: 1

Question:
What is the capital of Japan?
a. Beijing
b. Tokyo
c. Seoul
d. Osaka

Your answer: b

Progress: |██████████----------------------------| 2/10 (20%)

Quiz Complete! Your final score: 9/10
```

---

## Notes

* All quizzes are stored as `.json` files in the current working directory.
* The program ensures files are valid and structured correctly before loading.
* You can retry another quiz or exit after finishing one.

### JSON Format Example

```json
[
  {
    "question": "What is 2 + 2?",
    "choices": {
      "a": "3",
      "b": "4",
      "c": "5",
      "d": "22"
    },
    "correct_answer": "b"
  }
]
```

---

## Potential Improvements

* Show correct answer after incorrect guesses
* Support for timed quizzes
* Save quiz progress and allow resuming
* Add sound or audio feedback
* Export results to a file
* Automatically create an output folder
* Allow user to choose a filename
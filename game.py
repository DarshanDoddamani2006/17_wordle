import random
from words import WORDS
from feedback import evaluate


class WordleGame:
    def __init__(self, length=None):
        self.length = length
        self.target = (
            random.choice([w for w in WORDS if len(w) == length])
            if length is not None
            else None
        )
        self.history = []
        self.max_guesses = 6

    def choose_length(self):
        modes = {"1": 4, "4": 4, "2": 5, "5": 5, "3": 6, "6": 6}
        print("Select word length:")
        print("1. 4 letters")
        print("2. 5 letters")
        print("3. 6 letters")
        while True:
            try:
                choice = input("> ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                return None
            if choice == "q":
                return None
            if choice in modes:
                return modes[choice]
            print("Invalid choice. Please select 1, 2, or 3.")

    def display_history(self):
        print("History:")
        for idx, (g, fb) in enumerate(self.history, start=1):
            print(f"  Attempt {idx}: {g.upper()} -> {' '.join(fb)}")

    def display_summary(self, status):
        print("\n--- Game Summary ---")
        print(f"Word length: {self.length}")
        print(f"Guesses used: {len(self.history)}/{self.max_guesses}")
        if status == "won":
            print("Result: Won")
            print(f"Target word: {self.target}")
        elif status == "lost":
            print("Result: Lost")
            print(f"The word was: {self.target}")
        elif status == "quit":
            print("Result: Quit")
            print(f"The word was: {self.target}")

        if self.history:
            print("Final History:")
            for idx, (g, fb) in enumerate(self.history, start=1):
                print(f"  Attempt {idx}: {g.upper()} -> {' '.join(fb)}")
        else:
            print("Final History: None")

    def run(self):
        if self.length is None:
            if self.target:
                self.length = len(self.target)
            else:
                self.length = self.choose_length()
                if self.length is None:
                    return
                self.target = random.choice([w for w in WORDS if len(w) == self.length])
        elif not self.target:
            self.target = random.choice([w for w in WORDS if len(w) == self.length])

        print(f"Wordle — {self.length} letters, 6 guesses.")
        while len(self.history) < self.max_guesses:
            try:
                guess = input("> ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                self.display_summary("quit")
                return
            if guess == "q":
                self.display_summary("quit")
                return
            if len(guess) != self.length or not guess.isalpha():
                print("Enter a valid word of the required length.")
                continue
            feedback = evaluate(self.target, guess)
            self.history.append((guess, feedback))
            print(" ".join(feedback))
            self.display_history()
            if guess == self.target:
                print("Solved!")
                self.display_summary("won")
                return
        print("Game over! The word was:", self.target)
        self.display_summary("lost")


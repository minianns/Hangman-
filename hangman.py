import pandas as pd
import random
import os

#import csv
df = pd.read_csv("unigram_freq.csv")
#print(df.head())

#define function
def choose_word(min_length, max_length):
    df = pd.read_csv("unigram_freq.csv")
    words = df[df["word"].str.len().between(min_length, max_length)]["word"].dropna().tolist()
    return random.choice(words) if words else "python"


def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


def hangman():
    print("Select difficulty level: Easy = 1, Medium = 2, Hard = 3")
    difficulty = input("Enter your choice: ")

    if difficulty == "1":
        min_length, max_length = 1, 5
    elif difficulty == "2":
        min_length, max_length = 6, 9
    elif difficulty == "3":
        min_length, max_length = 10, 15
    else:
        print("Invalid choice, defaulting to Medium difficulty.")
        min_length, max_length = 6, 9
    word = choose_word(min_length, max_length)
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 10

#main
    print("Welcome to Hangman!")

    while incorrect_guesses < max_attempts:
        print("\nCurrent word:", display_word(word, guessed_letters))
        print("Guessed letters:", ", ".join(sorted(guessed_letters)))
        print("Incorrect guesses remaining:", max_attempts - incorrect_guesses)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("\033[31mInvalid input. Please enter a single letter.\033[0m")
            continue

        if guess in guessed_letters:
            print("\033[31mYou already guessed that letter. Please try another word.\033[0m")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"\033[36mGood job! '{guess}' is in the word.\033[0m")
            if set(word).issubset(guessed_letters):
                print("\033[36mCongratulations! You guessed the word: \033[0m", word)
                return
        else:
            print(f"\033[31moh oh!, '{guess}' is not in the word.\033[0m")
            incorrect_guesses += 1

    print("\033[31mGame over! The word was:\033[0m", word)


if __name__ == "__main__":
    hangman()


import random


word_list = ["python", "java", "hangman", ...]  # Define the word_list variable
attempts = 6

while attempts > 0:
    # Game logic will go here
    random_word = random.choice(word_list)
    print("_" * len(random_word))
  
guessed_letters = []  # Define the guessed_letters variable

guess = input("Guess a letter: ")

while not game_over:
    # Game logic goes here
    if guess in random_word:
        guessed_letters.append(guess)
    else:
        attempts -= 1

    if set(random_word).issubset(set(guessed_letters)):
        print("Congratulations, you won!")
        game_over = True
    elif attempts == 0:
        print("Sorry, you lost. The word was:", random_word)
        game_over = True

    if game_over:
        break


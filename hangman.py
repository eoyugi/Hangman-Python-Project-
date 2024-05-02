
# Import the random module
import random

# List of words for the game
words = ["python", "java", "hangman", "javascript", "docker"]

random_word = random.choice(words)

# Now you can print underscores for each letter in the random word
print("_" * len(random_word))

guessed_letters = []  # Define the guessed_letters variable

guess = input("Guess a letter: ")
game_over = False
attempts = 7  # Define the attempts variable

while not game_over:
    # Game logic goes here
    if guess in random_word:
        guessed_letters.append(guess)
    else:
        attempts -= 1  # Decrement attempts if the guess is wrong

    if set(random_word).issubset(set(guessed_letters)):
        print("Congratulations, you won!")
        game_over = True
    elif attempts == 0:
        print("Sorry, you lost. The word was:", random_word)
        game_over = True

import random

def hangman():
    # Game variables will be defined here
  
word_list = ["python", "java", "hangman", ...]
random_word = random.choice(word_list)
guessed_letters = []
attempts = 6

while attempts > 0:
    # Game logic will go here
    print("_" * len(random_word))
  
guess = input("Guess a letter: ")


if guess in random_word:
    guessed_letters.append(guess)
else:
    attempts -= 1


if set(random_word).issubset(set(guessed_letters)):
    print("Congratulations, you won!")
    break
elif attempts == 0:
    print("Sorry, you lost. The word was:", random_word)


# End of while loop

hangman()

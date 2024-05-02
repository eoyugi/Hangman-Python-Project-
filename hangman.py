import random

words = ["python", "java", "hangman", "javascript", "docker"]
random_word = random.choice(words)
guessed_letters = []
attempts = 7
game_over = False

while not game_over:
    print("_" * len(random_word))
    guess = input("Guess a letter: ")

    if guess in random_word:
        guessed_letters.append(guess)
    else:
        attempts -= 1

    all_guessed = True
    for letter in random_word:
        if letter not in guessed_letters:
            all_guessed = False

    if all_guessed:
        print("Congratulations, you won!")
        game_over = True
    elif attempts == 0:
        print("Sorry, you lost. The word was:", random_word)
        game_over = True
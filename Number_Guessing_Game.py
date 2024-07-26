import random

PC_guess = random.randint(1, 10)

user_guess = int(input('\nGuess what number I\'m thinking between 1-10: '))

while user_guess != PC_guess:
    if user_guess < PC_guess:
        user_guess = int(input('\nGuess too low. Try again: '))
    else:
        user_guess = int(input('\nGuess too high. Try again: '))

print('\nCorrect Guess!')
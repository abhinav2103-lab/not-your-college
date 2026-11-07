# Guessing Game
import random
number = random.randint(1, 100)
for i in range(10):
    guess = int(input("Guess a number between 1 and 100: "))
    counter = 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number.")
        counter += 1
        print("You guessed the number in", counter, "tries.")
        break

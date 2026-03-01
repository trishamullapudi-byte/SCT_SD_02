import random
print("Number Guessing Game")
# Random number between 1 and 100
number = random.randint(1, 100)
while True:
    guess = int(input("Enter your guess (1-100): "))
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it right!")
        break

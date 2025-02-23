import random
number_to_guess = random.randint(1, 100)
tries = 0

guess = int(input("Guess the number between 1 and 100: "))
tries += 1
while guess != number_to_guess and tries < 10:
    if guess < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess the number between 1 and 100: "))
    tries += 1

if guess == number_to_guess:
    print(f"Congratulations! You guessed the number in {tries} tries.")
else:
    print(f"Sorry, you're out of tries! The number was {number_to_guess}.")

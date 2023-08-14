import random

# TASK 1: The computer will generate a random number, then you will try to guess it.

def guess_random_number(tries: int, start: int, stop: int):
    target = random.randint(start, stop)
    while tries != 0:
        print(f"Number of tries left: {tries}")
        guess = int(input(f"Guess a number between {start} and {stop}:"))
        if guess == target:
            print("You guessed the correct number!")
            return
        elif guess < target and tries > 0:
            print("Guess higher!")
            tries -= 15
        elif guess > target and tries > 0:
            print("Guess lower!")
            tries -= 1
        else:
            print(f"You have failed to guess the number: {target}")
    

guess_random_number(5, 0, 10)

# TASK 2: The computer will generate a random number, then the computer will try to guess it using linear search.



# TASK 3: The computer will generate a random number, then the computer will try to guess it using binary search.
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
            break
    

# guess_random_number(5, 0, 10)

# TASK 2: The computer will generate a random number, then the computer will try to guess it using linear search.

def guess_random_num_linear(tries: int, start: int, stop: int):
    target = random.randint(start, stop)
    print(f"The number for the program to guess is: {target}")
    for num in range(start, stop):
        if tries > 0 and num != target:
            print(f"The program is guessing... {num}")
            print(f"Number of tries left: {tries}")
            tries -= 1
        elif tries > 0 and num == target:
            print(f"The program is guessing... {num}")
            print("The program has guessed the correct number")
            return
        
    print(f"The program has failed to guess the correct number.")   
    


guess_random_num_linear(5, 0, 10)
# TASK 3: The computer will generate a random number, then the computer will try to guess it using binary search.
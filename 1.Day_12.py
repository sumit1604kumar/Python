# Scope( local and global ) Number guessing game 
import random

easy_level = 10
hard_level = 5

def check_answer(guess,answer, turns):
    if guess > answer :
        print("Too high")
        return turns - 1
    elif guess < answer :
        print("Too low")
        return turns - 1
    else:
        print(f"you got it right, the answer was {answer}")

def set_difficulty():
    level = input("Choose a difficulty Level. Type 'easy' or 'hard' : ")
    if level == "easy":
        return easy_level
    else:
        return hard_level

def game():
    print("Welcome to the Number guessing game\nI am thinking of a number between 1 and 100 ")
    answer = random.randint(1, 100)
    print(f"The random number generated is {answer}")
    turns = set_difficulty()
    guess = 0
    while guess!= answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you loose.")
            return
        elif guess!= answer:
            print("Guess again.")

game()
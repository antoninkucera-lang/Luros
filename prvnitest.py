print("Hello, World!")
#I want to create an easy game 
#I want to create a game where you have to guess a number between 1 and 10
import random       
number = random.randint(1, 10)
guess = 0
while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number:
        print("Too low, try again.")
    elif guess > number:
        print("Too high, try again.")
print("Congratulations! You guessed the number.")
print("do you want to play again? (yes/no)")
play_again = input().lower()
if play_again == "yes":
    number = random.randint(1, 10)
    guess = 0
    while guess != number:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
    print("Congratulations! You guessed the number.")


test propojeni s githubem
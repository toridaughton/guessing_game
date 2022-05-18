import random

def number_guess():
    count = 0
    new_player_name = input("Yoo-hoo, what's your name?\n(type in your name) ")
    greeting = print(new_player_name + ", I'm thinking of a number between 1 and 100.")
    computer_number = random.randint(1, 100)
    guess = int(input("Try to guess my number. "))

    while(guess != computer_number):
        count += 1 
        if guess > computer_number:
            print("Sorry! Your guess is too high, try again.")
            guess = int(input("Your new guess? "))
        elif guess < computer_number:
            print("Sorry! Your guess is too low, try again.")
            guess = int(input("Your new guess? "))

    if(guess == computer_number):
        print("Congratulations! You guessed my number! It took you", count, "tries!")

number_guess()
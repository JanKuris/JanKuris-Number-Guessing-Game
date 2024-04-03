import random
from art import logo

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def thinking_number(): 
    random_number = random.randint(1,101)
    return random_number

def guessing_number():
    while True:
        user_number = input("Make a guess:")
        if user_number.isdigit():
            return int(user_number)
        else:
            print("Please enter a valid integer.")

def set_difficulty(): 
    difficulty = input("Choose a difficulty. Type easy or hard: ").lower()
    if difficulty == "easy":
        print(f"You have {EASY_ATTEMPTS} attempts remaining to guess the number.")
        return EASY_ATTEMPTS 
    else:
        print(f"You have {HARD_ATTEMPTS} attempts remaining to guess the number.")
        return HARD_ATTEMPTS

def compare(random_number, user_guess, attempts):
    if random_number > user_guess:
        print('''Too low.
Guess again.''')
        print(f"You have {attempts} attempts remaining to guess the number.")
    elif random_number < user_guess:
        print('''Too high.
Guess again.''')
        print(f"You have {attempts} attempts remaining to guess the number.")
    else:
        print(f"You got it! The answer was: {random_number}")     

def game():     
    print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
        """)
    attempts = set_difficulty()
    random_number = thinking_number()
    guess = False
    while attempts != 0:
        attempts -= 1
        user_guess = guessing_number()
        compare(random_number,user_guess, attempts)
        if random_number == user_guess:
            break
        if attempts == 0:
            print(f"The number was {random_number}")

def main():
    play_again = True
    while play_again:
        print(logo)
        game()
        new_game =  input("Do you want to guess again y/n ???").lower()
        if new_game == "y":
            print(logo)
            game()
        elif new_game == "n":
            play_again = False  
        else:
            play_again = True
main()
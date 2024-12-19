import random

def greetings():
    print('Welcome to Number Guessing Game!')
    name = input('May I ask your name?\n')
    print(f'''\n{name}, we are going to play a game.
I am thinking of a number between 1 and 100.
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)''')

def game(chances):
    print("Let's start the game!")
    number = random.randint(1, 100)
    for chance in range(chances):
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        
        if guess == number:
            print(f"Congratulations! You guessed the correct number in {chance + 1} attempts.")
            break
        elif guess > number:
            print(f"Incorrect! The number is less than {guess}.")
        elif guess < number:
            print(f'Incorrect! The number is greater than {guess}.')
    else:
        print(f"Sorry, you've used all {chances} chances! The correct number was {number}.")

def difficulty(ch):
    if ch == 1:
        print('Great! You have selected the Easy difficulty level.')
        game(10)
        return True
    elif ch == 2:
        print('Great! You have selected the Medium difficulty level.')
        game(5)
        return True
    elif ch == 3:
        print('Great! You have selected the Hard difficulty level.')
        game(3)
        return True
    else:
        print("Invalid choice! Please select a valid difficulty level (1, 2, or 3).")
        return False

def get_play_again_response():
    while True:
        ans = input('Do you want to play again? (yes/no): ').strip().lower()
        if ans == 'yes':
            return True
        elif ans == 'no':
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    greetings()
    while True:
        try:
            choice = int(input('Enter your choice (1, 2, or 3): '))
            if not difficulty(choice):  
                continue
        except ValueError:
            print("Please enter a valid number (1, 2, or 3).")
            continue
        
        if not get_play_again_response():
            print("Thank you for playing! Goodbye!")
            break

main()

import random

NUM_DIGITS = 3
MAX_TRIES = 10
introduction = f"""
Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a {NUM_DIGITS}-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
Pico         One digit is correct but in the wrong position.
Fermi        One digit is correct and in the right position.
Bagels       No digit is correct.
I have thought up a number.
You have {MAX_TRIES} guesses to get it.
"""

def get_input(tries):
    while True:
        guess = input(f"Guess #{tries}: ")
        if guess.isdigit() and len(guess) == NUM_DIGITS:
            return guess
        else:
            print(f"Please enter a valid {NUM_DIGITS}-digit number")

def secret_number():
    return str(random.randint(pow(10, NUM_DIGITS-1), pow(10, NUM_DIGITS) - 1))

def validate_guess(guess, number):
    result = []

    for i, num in enumerate(guess):
        if num in number:
            if number[i] == num:
                result.append("Fermi")
            else:
                result.append("Pico")

    if not result:
        return "Bagel"
    else:
        return ' '.join(result)



def play_game():
    print(introduction)
    number = secret_number()
    tries = 0

    while tries < MAX_TRIES:

        tries +=1

        guess = get_input(tries)

        if guess == number:
            print("You got it")
            break

        print(validate_guess(guess, number))

    if tries == MAX_TRIES:
        print('You ran out of guesses :( ')
        print(f"The answer was {number}")

def play_again():
    while True:
        ans = input("Do you want to play again? (yes or no): ")
        if ans in ['yes', 'no']:
            break

    if ans == 'no':
        print("Thanks for playing!")
    else:
        play_game()



def main():
   play_game()
   play_again()

if __name__ == "__main__":
    main()


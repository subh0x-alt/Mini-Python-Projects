import random

# Welcome the user to the game:
print("+---------------------------------------------+")
print("| Welcome to the Random Number Guessing Game! |")
print("+---------------------------------------------+\n")

top_of_range = input('Enter a number: ')

if (top_of_range.isdigit()):
    top_of_range = int(top_of_range)

    if (top_of_range <= 0):
        print('Enter a number greater than 0 (>0).\n')
        quit()

else:
    print("Enter a valid Integer.\n")

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if (user_guess.isdigit()):
        user_guess = int(user_guess)
    else:
        print("Please enter a valid number [INTEGER type data].\n")
        continue

    if (user_guess == random_number):
        print('\nYou got it!')
        break

    elif (user_guess < random_number):
        print("The number you have guessed is less than the random number.\n")
        continue

    elif (user_guess > random_number):
        print("The number you have guessed is greater than the random number.\n")
        continue


print(f"You got it in {guesses} guesses.")
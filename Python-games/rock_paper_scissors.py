# Welcome the user to the game:
print("+---------------------------------------------+")
print("| Welcome to the Rock, Papers, Scissors Game! |")
print("+---------------------------------------------+")

import random

user_wins = 0
computer_wins = 0
options = ['r', 'p', 's']
opt = ['Rock', ' Paper', 'Scissors']

while True:
    print("\n+----------------------------------+")
    user_input = int(input("| Choose any number for your Pick: |\n+----------------------------------+\n| 0: Rock  \
                        |\n| 1: Paper                         |\n| 2: Scissors                      |\n| 3: Quit                          |\n+----------------------------------+\nYour Choice: "))
    if (user_input < 3):
        # Assigning and Comparing the user and computer inputs.
        random_number = random.randint(0,2)
        computer_pick = options[random_number]
        user_pick =  options[user_input]
        print(f"You have picked: {opt[user_input]}.")
        print(f"Computer picked: {opt[random_number]}.")
        
        if (computer_pick == user_pick):
            print("Round Tied.\n")
        elif (user_pick == 'r') & (computer_pick == 's'):
            print("You won the round!\n")
            user_wins += 1
        elif (user_pick == 'p') & (computer_pick == 'r'):
            print("You won the round!\n")
            user_wins += 1
        elif (user_pick == 's') & (computer_pick == 'p'):
            print("You won the round!\n")
            user_wins += 1
        else:
            print("You Lost the round.")
            computer_wins += 1
        print("+--------------------------------------+")
        print(f"| Your Score: {user_wins} | Computer's Score: {computer_wins} |")
        print("+--------------------------------------+")

    elif (user_input == 3):
        print("+--------------------------------------+")
        print(f"| Your Score: {user_wins} | Computer's Score: {computer_wins}|")
        print("+--------------------------------------+")
        print("\nGoodBye!\n")
        quit()
    else:
        print('Invalid Choice! Choose a proper valid option.\n')
        continue
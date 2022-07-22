# Python Quiz Game (without functions): v1.0

# Welcome the user to the game:
print("+-----------------------------+")
print("| Welcome to the Python Quiz! |")
print("+-----------------------------+\n")
# Retrieve user-input:
print("Do you want to play the game? ")
play = input("[Yes/No] : ")

if ((play.lower() == 'yes' )| (play.lower() == 'y')):
    score = 0
    print("\n+--------------+")
    print("| Let's Begin: |")
    print("+--------------+\n")
    for q in range(1,5):
        if (q==1):
            # Question-1:
            quest = input("When was python created [Enter the year: in YYYY (Example: 2009)]?\n")
            if (str(quest) == "1991"):
                print("Correct!")
                score += 5
                print("You scored: +5")
            else:
                print("Incorrect!")
            print(f"Your current Score: {score}\n")
        
        elif (q==2):
            # Question-2:
            quest = input("Is tuple a mutable datatype?[Enter: Y/N]\n")
            if (str(quest).lower() == "n"):
                print("Correct!")
                score += 5
            else:
                print("Incorrect!")
            print(f"Your current Score: {score}\n")
        
        elif (q==3):
            # Question-3:
            quest = input("What is the current version of python?[eg: If the current version is 2.7.2 then enter: 2.7]\n")
            if (str(quest) == "3.9"):
                print("Correct!")
                score += 5
            else:
                print("Incorrect!")
            print(f"Your current Score: {score}\n")

        elif (q==4):
            # Question-4:
            quest = input("Is string a mutable type data? [Y/N]\n")
            if (str(quest).lower() == "n"):
                print("Correct!")
                score += 5
            else:
                print("Incorrect!")
            print(f"Your current Score: {score}\n")
    print(f"You Scored: {score}/20")
    quit()

elif ((play.lower() == 'no' )| (play.lower() == 'n')):
    quit()

else:
    print('Enter a proper response.')
    quit()

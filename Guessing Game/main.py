print("\nWelcome to Madhav's guessing game! \n \n Rules: \n \n 1. The computer has thought of a number between 1 and 10  \n 2. You have three chances to guess the number and each incorrect guess leads to your chances decrementing by 1 \n \n Good Luck! \n")

def guessing_game():
    import random
    num_chances=3
    number=random.randint(1,10) # This is the number from 1-10 the computer thinks of
    
    try:
        guess=int(input("Guess the number: "))

        if type(guess)!=int:

            print("Please input only an integer")
        if guess==number:
            print("Correct :) You Win!") # If the guess is correct, the game ends'
            print("Thanks for playing!")
            choice=input("Want to play again? (y/n): ")
            if choice=="y": 
                guessing_game()
            elif choice=="n": # This statement is executed if the choice is 'No'
                print("Thanks for playing!")
                exit()  # Program ends
            else:
                print("Please input either y or n")


        else:
            while guess!=number:   # This loop is repeated until either the number is guessed or three chances are used up
                print("Your guess was not correct")
                num_chances-=1
                
                if num_chances!=1:
                    print(f"You have {num_chances} chances left")

                elif num_chances==1:
                    print(f"You have {num_chances} chance left")

                new_guess=int(input("Enter a new guess: "))

                if new_guess==number:
                    print("Correct! You Win!")
                    print("Thanks for playing!")
                    choice=input("Want to play again? (y/n): ")
                    if choice=="y":
                        guessing_game()
                    elif choice=="n":
                        print("Thanks for playing!")
                        exit()   
                    else:
                        print("Please input either y or n")


                if num_chances==1:
                    print("You lost :(") # Three chances are up
                    print(f"The number was {number}")
                    choice=input("Want to play again? (y/n): ")
                    if choice=="y":
                        guessing_game()
                    elif choice=="n": 
                        print("Thanks for playing!")
                        exit()  
                    else:
                        print("Please input either y or n")
                        exit()

    except ValueError:
        print("Please input only an integer")
        guessing_game()




guessing_game()

# Dice_Rolling_Guessing_Game

import random
import time
def Dice_Rolling_Game():
    while (True):
        print("****************✨  (Welcome to Dice Rolling Game) ✨ ****************")
        choose_1 = input("Want to play this game (Yes/No)🙂 : ").title()
        if (choose_1 == "Yes"):
            time.sleep(2)
            dice_option = input("Press (D) to roll a dice🙂 : ").capitalize()
            if (dice_option == "D"):
                Dice_Rolled = random.randint(1,6)
                time.sleep(2)
                print("Dice Rolled👍👍..")
                time.sleep(2)
                print("Now, your turn to guess the number😊😊..")
                guess_number = int(input("Enter your number(1,6) : "))
                if (guess_number == Dice_Rolled):
                    time.sleep(2)
                    print("You, Won the game..✨🏆🏆")
                else:
                    time.sleep(2)
                    print("You, lose the game..😒😒")
                    time.sleep(2)
                    print(f"The Dice number is {Dice_Rolled} and you guessed {guess_number}.")
        else:
            print("**🙌(Exited Game)🙌**")
            break
Dice_Rolling_Game()
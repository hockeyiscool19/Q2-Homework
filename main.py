import numpy as np
from helper_functions import *
from questions import *
from Test import *

def main():
    """
    Main math-test loop
    """
    welcome()
    play_game  = False
    playing = ""
    playing = input("Would you like to take a math test? Type n for yes or n for no: ").lower()
    
    while playing not in ["y","n"]:
        print("Please type y or n: ")

    if playing == "n":
        print("Thanks for stopping by. We hope to see your again")
        return
    
    replay = True

    while replay == True:
        print("Please select which operation you would like to use for your math test: ")
        operation = int(input("1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division: ").replace(" ",""))

        while operation not in [1,2,3,4]:
            print("Please type 1, 2, 3, or 4")
        
        math_test = Test(operation=operation)
        math_test.take_test()

        playing = input("Do you want to play again? Type n for yes or n for no: ").lower()
        
        while playing not in ["y","n"]:
            print("Please type y or n: ")

        if playing == "n":
            print("Thanks for stopping by. We hope to see your again")
            return

if __name__ == '__main__':
    main()
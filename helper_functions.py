import numpy as np

def welcome():
    print("Welcome to your...")
    print(r'''

                             _________  
       /\      /\       /\       |     |     |
      /  \    /  \     /  \      |     |     |
     /    \  /    \   / ___\     |     +-----+
    /      \/      \ /      \    |     |     |

    _________ +-----  +-----+  _________
        |     |       |            |     
        |     +-----  +-----+      |     
        |     |             |      |
        |     +-----  ------+      |
    '''
    )


def tell_score(score, number, target):
    if number == target:
        score += 1
    print(f"\nYou have answered {score} questions correctly.\n")
    return score

def parse(str, operation):

    str = str.replace(" ", "")

    if operation == 1:
        int_array = np.array(str.split("+"))
        int_array = int_array.astype(int)
        return int_array.sum()
            
    if operation == 2:
        int_array = np.array(str.split("-"))
        int_array = int_array.astype(int)
        return int_array[0] - int_array[1:].sum()

    if operation == 3:
        int_array = np.array(str.split("*"))
        int_array = int_array.astype(int)
        return np.prod(int_array)

    if operation == 4:
        int_array = np.array(str.split("/"))
        int_array = int_array.astype(int)
        if len(int_array) == 1:
            return int_array[0]
        return int(int_array[0] / int_array[1])


def parse_operation(str, operation, number = -1):
    if number > -1:
        return number
    try:
        return parse(str=str, operation=operation)
    except:
        new = input("Please input a valid equation: ")
        number = parse_operation(str=new, operation=operation)
        return number


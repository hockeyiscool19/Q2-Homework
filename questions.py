from helper_functions import *
import numpy as np

def one_add(score = 0):
    """
    Function for the first question of addition
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("First question: what does 2 + 2 equal?\n")
    number = parse_operation(number, operation = 1)
    return tell_score(score = score, number = number, target = 4)

def two_add(score = 0):
    """
    Function for the second question of addition
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Second Question: what is 5 + 5? \n")
    number = parse_operation(number, operation = 1)
    return tell_score(score = score, number = number, target = 10)

def three_add(score = 0):
    """
    Function for the third question of addition
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    print("Third question: if John has two apples and Sarah has fifteen apples,")
    number = input("how many apples do John and Sarah have in total? \n")
    number = parse_operation(number, operation = 1)
    return tell_score(score = score, number = number, target = 17)

def four_add(score = 0):
    """
    Function for the fourth question of addition
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Fourth question: what is 2 + 10? \n")
    number = parse_operation(number, operation = 1)
    return tell_score(score = score, number = number, target = 12)

def five_add(score = 0):
    """
    Function for the fifth question of addition
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    print("Fifth question: Eagan scores sixteen goals and Steven scores forty goals.")
    number = input("How many goals do Eagan and Steven score together? \n")
    number = parse_operation(number, operation = 1)
    return tell_score(score = score, number = number, target = 56)

def six_add(score = 0):
    """
    Function for the sixth question of addition
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Sixth question: what is 200 + 300? \n")
    number = parse_operation(number, operation = 1)
    return tell_score(score = score, number = number, target = 500)

def seven_add(score = 0):
    """
    Function for the seventh question of addition
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Seventh question: what is 1984 + 2001 + 3005? \n")
    print("Yes, I do love science fiction and Childish Gambino...")
    number = parse_operation(number, operation = 1)
    return tell_score(score = score, number = number, target = 6990)

def eight_add(score = 0):
    """
    Function for the eighth question of addition
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Eigth question: what is one plus two? \n")
    number = parse_operation(number, operation = 1)
    return tell_score(score = score, number = number, target = 3)

def nine_add(score = 0):
    """
    Function for the ninth question of addition
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Ninth question: what is four plus one? \n")
    number = parse_operation(number, operation = 1)
    return tell_score(score = score, number = number, target = 5)

def ten_add(score = 0):
    """
    Function for the tenth question of addition
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Tenth question: what is twenty plus twenty? \n")
    number = parse_operation(number, operation = 1)
    return tell_score(score = score, number = number, target = 40)


def one_sub(score = 0):
    """
    Function for the first question of subtraction
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("First question: what is two minus one? \n")
    number = parse_operation(number, operation = 2)
    return tell_score(score = score, number = number, target = 1)

def two_sub(score = 0):
    """
    Function for the second question of subtraction
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    print("Second question: John has three apples. Annie steals one apple.")
    number = input("how many apples are left? \n")
    number = parse_operation(number, operation = 2)
    return tell_score(score = score, number = number, target = 2)

def three_sub(score = 0):
    """
    Function for the third question of subtraction
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Third question: what is ten, take five?\n")
    number = parse_operation(number, operation = 2)
    return tell_score(score = score, number = number, target = 5)


def four_sub(score = 0):
    """
    Function for the fourth question of subtraction
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Fourth question: what is twenty, take six and another six? \n")
    number = parse_operation(number, operation = 2)
    return tell_score(score = score, number = number, target = 8)

def five_sub(score = 0):
    """
    Function for the fifth question of subtraction
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    print("Fifth question: you have twenty hockey pucks on the ice. Kevin shoots")
    print("twelve pucks over the glass. Steven steals five pucks from the") 
    number = input("ice. How many pucks are left? \n")
    number = parse_operation(number, operation = 2)
    return tell_score(score = score, number = number, target = 3)

def six_sub(score = 0):
    """
    Function for the sixth question of subtraction
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Sixth question: what is fifteen, take six? \n")
    number = parse_operation(number, operation = 2)
    return tell_score(score = score, number = number, target = 9)

def seven_sub(score = 0):
    """
    Function for the seventh question of subtraction
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Seventh question: what is twenty minus eighteen? \n")
    number = parse_operation(number, operation = 2)
    return tell_score(score = score, number = number, target = 2)

def eight_sub(score = 0):
    """
    Function for the eighth question of subtraction
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Eighth question: what is 123 minus seventy-six? \n")
    number = parse_operation(number, operation = 2)
    return tell_score(score = score, number = number, target = 47)


def nine_sub(score = 0):
    """
    Function for the ninth question of subtraction
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Ninth question: What is thirty minus twenty? \n")
    number = parse_operation(number, operation = 2)
    return tell_score(score = score, number = number, target = 10)


def ten_sub(score = 0):
    """
    Function for the tenth question of subtraction
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Tenth question: what is three minus one? \n")
    number = parse_operation(number, operation = 2)
    return tell_score(score = score, number = number, target = 2)



def one_mult(score = 0):
    """
    Function for the first question of multiplication
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    print("First Question: there are four runners in a race")
    print("what is the number of combinations of placements")
    number = input("the runners can finish in?\n")
    number = parse_operation(number, operation = 3)
    return tell_score(score = score, number = number, target = 24)

def two_mult(score = 0):
    """
    Function for the second question of multiplication
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Second question: what is three times three? \n")
    number = parse_operation(number, operation = 3)
    return tell_score(score = score, number = number, target = 9)


def three_mult(score = 0):
    """
    Function for the third question of multiplication
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Third question: what is 29 times 2? \n")
    number = parse_operation(number, operation = 3)
    return tell_score(score = score, number = number, target = 58)

def four_mult(score = 0):
    """
    Function for the fourth question of multiplication
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    print("Fourth question: we have three groups of five. How many")
    number = input("people do we have? \n")
    number = parse_operation(number, operation = 3)
    return tell_score(score = score, number = number, target = 15)

def five_mult(score = 0):
    """
    Function for the fifth question of multiplication
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Fifth question: what is four times three? \n")
    number = parse_operation(number, operation = 3)
    return tell_score(score = score, number = number, target = 12)

def six_mult(score = 0):
    """
    Function for the sixth question of multiplication
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Sixth question: what is six times ten times eight? \n")
    number = parse_operation(number, operation = 3)
    return tell_score(score = score, number = number, target = 480)

def seven_mult(score = 0):
    """
    Function for the seventh question of multiplication
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Seventh question: what is twenty times two? \n")
    number = parse_operation(number, operation = 3)
    return tell_score(score = score, number = number, target = 40)

def eight_mult(score = 0):
    """
    Function for the eighth question of multiplication
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Eigth question: what is six times five? \n")
    number = parse_operation(number, operation = 3)
    return tell_score(score = score, number = number, target = 30)

def nine_mult(score = 0):
    """
    Function for the ninth question of multiplication
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Ninth question: what is nine times nine? \n")
    number = parse_operation(number, operation = 3)
    return tell_score(score = score, number = number, target = 81)

def ten_mult(score = 0):
    """
    Function for the tenth question of multiplication
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Tenth question: what is 1 times 1? \n")
    number = parse_operation(number, operation = 3)
    return tell_score(score = score, number = number, target = 1)


def one_div(score = 0):
    """
    Function for the first question of division
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    print("First question: we have fifty-four people and must divide")
    number = input("them into six groups. How many people are in each group? \n")
    number = parse_operation(number, operation = 4)
    return tell_score(score = score, number = number, target = 9)

def two_div(score = 0):
    """
    Function for the second question of division
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Second question: what is sixty divided by six? \n")
    number = parse_operation(number, operation = 4)
    return tell_score(score = score, number = number, target = 10)

def three_div(score = 0):
    """
    Function for the third question of division
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Third question: what is twenty-five divided by five? \n")
    number = parse_operation(number, operation = 4)
    return tell_score(score = score, number = number, target = 5)


def four_div(score = 0):
    """
    Function for the fourth question of division
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Fourth question: what is 144 divided by twelve? \n")
    number = parse_operation(number, operation = 4)
    return tell_score(score = score, number = number, target = 12)


def five_div(score = 0):
    """
    Function for the fifth question of division
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Fifth question: what is 200 divided by fifty? \n")
    number = parse_operation(number, operation = 4)
    return tell_score(score = score, number = number, target = 4)


def six_div(score = 0):
    """
    Function for the sixth question of division
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Sixth question: what is 160 divided by four? \n")
    number = parse_operation(number, operation = 4)
    return tell_score(score = score, number = number, target = 40)

def seven_div(score = 0):
    """
    Function for the seventh question of division
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Seventh Question: what is 1000 divided by 100? \n")
    number = parse_operation(number, operation = 4)
    return tell_score(score = score, number = number, target = 10)

def eight_div(score = 0):
    """
    Function for the eighth question of division
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    print("Eigth question: we must split a group of eight people")
    number = input("into groups of four. How many will be in each group? \n")
    number = parse_operation(number, operation = 4)
    return tell_score(score = score, number = number, target = 2)

def nine_div(score = 0):
    """
    Function for the ninth question of division
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    print("Ninth question: there are thirty people on Love island")
    print("split evenly between guys and girls. What is the maximum") 
    print("number of couples that can leave the island, without double")
    number = input("counting?\n")
    number = parse_operation(number, operation = 4)
    return tell_score(score = score, number = number, target = 15)

def ten_div(score = 0):
    """
    Function for the tenth question of division
    Parameters:
    score: refers to the users score we must update
    Returns: int: Description of return value
    """
    number = input("Tenth question: what is two divided by two? \n")
    number = parse_operation(number, operation = 4)
    return tell_score(score = score, number = number, target = 1)
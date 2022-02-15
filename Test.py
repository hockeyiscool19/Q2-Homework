from questions import *

class Test:
    """
    This is a class which will help track all the data
    while people take their tests

    ...

    Attributes
    ----------
    score : int
        the number of correct questions
    percent : float
        the final score of your test
    length : int
        the length of the test
    operation : int
        the type of operation -- addition, subtraction,
        multiplication, division

    Methods
    -------
    add(self, score = 0):
        used to create addition test 

    subtract(self, score = 0):
        used to create addition test 

    multiply(self, score = 0):
        used to multiply addition test 
        
    divide(self, score = 0):
        used to create divide test 
    
    take_test(self, score = 0):
        method used to create the test.
                
    """


    def __init__(self, operation):
        """
        Constructs instance of a Test
        Parameters:
        operation: refers to the test corresponding
        to a specific mathematical operation
        """
        self.score = 0
        self.percent = 0.0
        self.length = 10
        self.operation = operation
    
    def add(self, score = 0):
        """
        used to create addition test and gives an accuracy score
        Parameters:
        score: refers to the users score we must update
        """
        self.score = 0
        self.percent = 0
        print("Since you are adding, you may only use numbers, spaces, and the plus sign,'+'\n")
        
        self.score = one_add(self.score)
        self.score = two_add(self.score)
        self.score = three_add(self.score)
        self.score = four_add(self.score)
        self.score = five_add(self.score)
        self.score = six_add(self.score)
        self.score = seven_add(self.score)
        self.score = eight_add(self.score)
        self.score = nine_add(self.score)
        self.score = ten_add(self.score)

        self.percent = 100 * self.score / self.length 
        print(f"You got {self.percent}%  on your test")

    
    def subtract(self, score = 0):
        """
        used to create subtraction test and gives an accuracy score
        Parameters:
        score: refers to the users score we must update
        """
        self.score = 0
        self.percent = 0
        print("\nSince you are subtracting, you may only use numbers, spaces, and the plus sign,'-'\n")
        
        self.score = one_sub(self.score)
        self.score = two_sub(self.score)
        self.score = three_sub(self.score)
        self.score = four_sub(self.score)
        self.score = five_sub(self.score)
        self.score = six_sub(self.score)
        self.score = seven_sub(self.score)
        self.score = eight_sub(self.score)
        self.score = nine_sub(self.score)
        self.score = ten_sub(self.score)

        self.percent = 100 * self.score / self.length 
        print(f"You got {self.percent}%  on your test")

    def multiply(self, score = 0):
        """
        used to create multiplication test and gives an accuracy score
        Parameters:
        score: refers to the users score we must update
        """
        self.score = 0
        self.percent = 0
        print("\nSince you are multiplying, you may only use numbers, spaces, and the plus sign,'*'\n")

        self.score = one_mult(self.score)
        self.score = two_mult(self.score)
        self.score = three_mult(self.score)
        self.score = four_mult(self.score)
        self.score = five_mult(self.score)
        self.score = six_mult(self.score)
        self.score = seven_mult(self.score)
        self.score = eight_mult(self.score)
        self.score = nine_mult(self.score)
        self.score = ten_mult(self.score)

        self.percent = 100 * self.score / self.length 
        print(f"You got {self.percent}%  on your test")

    def divide(self, score = 0):
        """
        used to create division test and gives an accuracy score
        Parameters:
        score: refers to the users score we must update
        """
        self.score = 0
        self.percent = 0
        print("\nSince you are dividing, you may only use numbers, spaces, and the plus sign,'/'")
        print("Note: this function does not support parenthisis and more advanced order of operations.\n")

        self.score = one_div(self.score)
        self.score = two_div(self.score)
        self.score = three_div(self.score)
        self.score = four_div(self.score)
        self.score = five_div(self.score)
        self.score = six_div(self.score)
        self.score = seven_div(self.score)
        self.score = eight_div(self.score)
        self.score = nine_div(self.score)
        self.score = ten_div(self.score)

        self.percent = 100 * self.score / self.length 
        print(f"You got {self.percent}%  on your test")

    
    def take_test(self):
        """
        used to create the math test
        """
        if self.operation == 1:
            self.add()
            return

        if self.operation == 2:
            self.subtract()
            return

        if self.operation == 3:
            self.multiply()
            return
        
        self.divide()


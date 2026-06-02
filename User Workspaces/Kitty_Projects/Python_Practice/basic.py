# Libraries
import manim
import numpy as np # Right now, both libraries are grey since I've imported them but not used them anywhere in the script.


# Some definitions, constants, and functions

olive = "garden"
pi = 3.14159265358979323846
user_name = input("Enter your name: ")

def multiply_three_numbers(a, b, c):
    return a * b * c
    adder(a, b, c)
# This is a comment.  It is ignored by the interpreter.



#### The Code

#print("Hello, " + user_name + "! Welcome to a a print function.")

#print("Would you like to know the value of pi? (yes/no)")
#answer = input("Enter your answer: ")

# Hey look, a function

# Boolean algebra, boolean logic

#
# This is an "if / else" function.  It does one thing for some condition, and something else for another. 
#if answer == "yes":
#    print("The value of pi is approximately: " + str(pi))
#else:
#    print("Okay, maybe next time!")

### Functions

# This is a function that takes in 2 arguments and returns their sum.
def adder(first_number, second_number, third_number):
    multiply_three_numbers(first_number, second_number, third_number)
    return first_number + second_number + third_number

print(adder(1))







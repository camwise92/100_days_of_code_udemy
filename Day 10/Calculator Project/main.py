"""
Calculator Project (Day 10 of Udemy 100 Days of Code)

File: main.py
Description: A simple calculator that performs basic arithmetic operations.
Author: Cameron Carlisle
Date created: 20/03/2025
Last modified: 20/03/2025
Version: 1.0

This script allows users to perform basic arithmetic operations (addition, subtraction, multiplication, and division).  
Users can continue calculations with the previous result or start a new calculation.  

Usage:
1. Enter the first number.
2. Choose an operation (+, -, *, /).
3. Enter the second number.
4. View the result and decide whether to continue or start over.

Dependencies:
- Requires the `art` module for ASCII art display.

Contact: cameroncarlisle1992@gmail.com
"""


import art

def main():
    calculator()

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    should_accumulate = True
    number_1 = float(input("Please enter the first number: "))

    while should_accumulate:

        operation = input("Please enter the operation you would like to perform (+,-,*,/): ")
        number_2 = float(input("Please enter the second number: "))
        result = operations[f"{operation}"](number_1, number_2)
        print(f"{number_1} {operation} {number_2} = {result}")
        continue_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if continue_calculating == 'y':
            number_1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

if __name__ == "__main__":
    main()


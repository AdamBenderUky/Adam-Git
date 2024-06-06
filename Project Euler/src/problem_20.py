# problem_20.py

import math

def sum_of_factorial_digits(number):
    # Calculate the factorial of the given number
    fact = math.factorial(number)

    # Convert the factorial result to a string, then to a list of digits
    digits = [int(digit) for digit in str(fact)]

    # Sum the digits
    sum_of_digits = sum(digits)

    return sum_of_digits

if __name__ == "__main__":
    number = int(input("Enter the number to calculate the sum of the digits of its factorial: "))
    result = sum_of_factorial_digits(number)
    print(f"The sum of the digits in the number {number}! is: {result}")

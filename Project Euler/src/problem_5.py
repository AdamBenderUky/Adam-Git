# problem_5.py

import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def smallest_multiple(n):
    multiple = 1
    for i in range(1, n + 1):
        multiple = lcm(multiple, i)
    return multiple

if __name__ == "__main__":
    n = 20
    result = smallest_multiple(n)
    print(f"The smallest positive number that is evenly divisible by all of the numbers from 1 to {n} is {result}")

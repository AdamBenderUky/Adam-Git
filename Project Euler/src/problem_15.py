# problem_15.py

import math

def lattice_paths(n):
    return math.comb(2 * n, n)

if __name__ == "__main__":
    n = int(input("Enter the value of n for an NxN grid: "))
    result = lattice_paths(n)
    print(f"The number of routes through a {n}x{n} grid is {result}")

# problem_4.py

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome_product(digits):
    max_num = 10**digits - 1
    min_num = 10**(digits - 1)
    largest_palindrome = 0
    factors = (0, 0)
    
    for i in range(max_num, min_num - 1, -1):
        for j in range(i, min_num - 1, -1):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
                factors = (i, j)
    
    return largest_palindrome, factors

if __name__ == "__main__":
    digits = 3
    result, factors = largest_palindrome_product(digits)
    print(f"The largest palindrome made from the product of two {digits}-digit numbers is {result}, made from the numbers {factors[0]} and {factors[1]}")
# problem_12.py

def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 2  # i and n // i
    if int(n**0.5)**2 == n:
        count -= 1  # Correct the count if n is a perfect square
    return count

def find_triangle_number_with_divisors(limit):
    n = 1
    triangle_number = 0
    while True:
        triangle_number += n
        if count_divisors(triangle_number) > limit:
            return triangle_number
        n += 1

if __name__ == "__main__":
    limit = 500
    result = find_triangle_number_with_divisors(limit)
    print(f"The first triangle number to have over {limit} divisors is {result}")
